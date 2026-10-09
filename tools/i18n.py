"""Übersetzt den App-Quelltext ins Englische.

Ersetzt Phrasen aus i18n_en.json nur innerhalb von Textbereichen:
HTML-Text, JS-Stringliterale und Template-Literal-Text. Code, Regex-Literale,
Kommentare und CSS bleiben unangetastet.
"""
import json, re, sys, pathlib

def regions(src):
    """Liefert (start, end) aller übersetzbaren Textbereiche."""
    out = []
    n = len(src)
    i = 0
    # HTML-Bereiche ausserhalb von <script>/<style>; Scriptbereiche gesondert
    for m in re.finditer(r'<script>(.*?)</script>|<style>.*?</style>', src, re.S):
        pass
    pos = 0
    blocks = []
    for m in re.finditer(r'(<script>)(.*?)(</script>)|<style>.*?</style>', src, re.S):
        blocks.append(('html', pos, m.start()))
        if m.group(1):
            blocks.append(('js', m.start(2), m.end(2)))
        pos = m.end()
    blocks.append(('html', pos, n))
    for kind, a, b in blocks:
        if kind == 'html':
            for t in re.finditer(r'>([^<>]+)<', src[a:b]):
                out.append((a + t.start(1), a + t.end(1)))
            for t in re.finditer(r'(?:placeholder|title|aria-label|content)="([^"]*)"', src[a:b]):
                out.append((a + t.start(1), a + t.end(1)))
        else:
            out += js_regions(src, a, b)
    return out

def js_regions(s, a, b):
    out = []
    i = a
    stack = []          # Template-Verschachtelung: Anzahl offener { je ${
    prev = '('          # letztes signifikantes Zeichen (für Regex-Erkennung)
    prev_word = ''
    def scan_template(i):
        # i zeigt hinter ` oder hinter } eines ${...}; liest Text bis ` oder ${
        start = i
        while i < b:
            c = s[i]
            if c == '\\': i += 2; continue
            if c == '`':
                out.append((start, i)); return i + 1, False
            if c == '$' and s[i+1] == '{':
                out.append((start, i)); return i + 2, True
            i += 1
        return i, False
    while i < b:
        c = s[i]
        if c in ' \t\r\n': i += 1; continue
        if s.startswith('/*i18n-off*/', i):
            j = s.find('/*i18n-on*/', i); i = b if j < 0 else j + 11; continue
        if s.startswith('//', i):
            j = s.find('\n', i); i = b if j < 0 else j; continue
        if s.startswith('/*', i):
            j = s.find('*/', i + 2); i = b if j < 0 else j + 2; continue
        if c in '\'"':
            j = i + 1
            while j < b and s[j] != c:
                j += 2 if s[j] == '\\' else 1
            out.append((i + 1, j)); i = j + 1; prev = 'x'; prev_word = ''; continue
        if c == '`':
            i, opened = scan_template(i + 1)
            if opened: stack.append(0)
            prev = 'x'; continue
        if c == '{' and stack:
            stack[-1] += 1; i += 1; prev = c; continue
        if c == '}' and stack:
            if stack[-1] == 0:
                stack.pop()
                i, opened = scan_template(i + 1)
                if opened: stack.append(0)
                prev = 'x'; continue
            stack[-1] -= 1; i += 1; prev = c; continue
        if c == '/':
            regex_ok = prev in '(,=:[!&|?{};+-*%<>~^' or prev_word in ('return', 'typeof', 'case', 'of', 'in')
            if regex_ok:
                j = i + 1; cls = False
                while j < b:
                    if s[j] == '\\': j += 2; continue
                    if s[j] == '[': cls = True
                    elif s[j] == ']': cls = False
                    elif s[j] == '/' and not cls: break
                    elif s[j] == '\n': break
                    j += 1
                i = j + 1
                while i < b and s[i].isalpha(): i += 1
                prev = 'x'; prev_word = ''; continue
            i += 1; prev = c; continue
        if c.isalnum() or c in '_$':
            j = i
            while j < b and (s[j].isalnum() or s[j] in '_$'): j += 1
            prev_word = s[i:j]; prev = 'x'; i = j; continue
        prev = c; prev_word = ''; i += 1
    return out

GERMAN = re.compile(r'[äöüßÄÖÜ„“]|\b(der|die|das|und|nicht|mit|für|ist|bei|ein|eine|noch|zu|im|auf|aus|Shot|Mahlgrad|Bohne|Zeit|Dosis|Ausbeute|Kurve|Rezept|Ziel|Daten|Vergleich|Befund|Analyse|halten|Stufe|Stufen|Klick|Klicks|sauer|bitter|dünn|spitz|Geschmack|Bewertung|Notiz|Tage|neu|Kurve|Einheit|gesamt|Haupt|erwartet|feiner|gröber|kühler|wärmer|hoch|mittel|niedrig|leicht|deutlich|Beispiel|Wie|Was|Nur|Keine|Kein|Mit|Ohne|Im|Bei|Der|Die|Das|Ein|Eine|Ab|Zum|Für|Vor|Nach|Datum|Temp|Notizen|Gemessen|Hebel|Richtung|Schritt|Nebenwirkung|Durchfluss|Laufzeit|Erster|Fehler|Datei|Dateien|Laden|Löschen|Abbrechen|Übernehmen|Jetzt|Zurücksetzen|Ziele|Verlauf|Speichern|Basis|als|oder|Sekunden|bis|von|vom|nur|diese|dieser|dieses|deine|deinen|deiner|dein|du|dich|dir|sich|wird|werden|wurde|kann|kannst|muss|soll|sind|hat|haben|war|weniger|mehr|etwas|sehr|wenn|dann|auch|oder|über|unter|zur|zum|vor|nach|Röstung|Röstdatum|Mühle|Waage|Puck|Stopp|Tropfen|Kurven|Rückspülen|Entkalken|Pflege|Bezug|Bezüge|Bezügen)\b')

def extract(src):
    segs = []
    for a, b in regions(src):
        t = src[a:b]
        if GERMAN.search(t): segs.append(t)
    return segs

def translate(src, exact, phrases):
    regs = sorted(regions(src))
    phrases = sorted(phrases, key=lambda p: -len(p[0]))
    out = []; pos = 0; left = []
    for a, b in regs:
        if a < pos: continue
        out.append(src[pos:a])
        seg = src[a:b]
        if seg in exact:
            seg = exact[seg]
        else:
            for de, en in phrases:
                if de in seg: seg = seg.replace(de, en)
            if re.search(r'[äöüßÄÖÜ„]', seg) or GERMAN_LEFT.search(seg):
                left.append(seg)
        out.append(seg); pos = b
    out.append(src[pos:])
    return ''.join(out), left

GERMAN_LEFT = re.compile(r'\b(der|die|das|und|nicht|mit|für|ist|noch|Mahlgrad|Bohne|Zeit|Dosis|Ausbeute|Kurve|Rezept|Ziel|Daten|Befund|Stufe|Klick|sauer|dünn|Geschmack|Bewertung|Notiz|Tage|Mühle|Röst\w*|Tropfen|Bezug\w*|Laden|Löschen|Speichern|Basis|weniger|mehr|etwas|sehr|wenn|deine?n?|Pflege|Verlauf|Gemessen|Hebel|Durchfluss|Laufzeit)\b')

if __name__ == '__main__':
    src = pathlib.Path(sys.argv[1]).read_text()
    seen = []
    for s in extract(src):
        if s not in seen: seen.append(s)
    print(json.dumps(seen, ensure_ascii=False, indent=0))
