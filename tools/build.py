"""Baut die App aus src/.

  index.html                 Deutsch (Vercel, /)
  en/index.html              Englisch (Vercel, /en/)
  dist/claude-artifact.html  Deutsch ohne Sprachumschalter (Claude-Vorschau)
"""
import os, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
os.chdir(root)
sys.path.insert(0, str(root / 'tools'))
import i18n, i18n_en

template = open('src/template.html').read()
sample_de = open('src/sample.json').read()
sample_en = open('src/sample_en.json').read()

META = {
    'de': ('Dial-in Kompass: Beanconqueror-Export laden, Shots analysieren, nächsten Espresso berechnen.', 'Sprache'),
    'en': ('Dial-in Kompass: load your Beanconqueror export, analyse shots, work out your next espresso.', 'Language'),
}

def lang_switch(lang):
    links = []
    for code, href in (('de', '/'), ('en', '/en/')):
        cur = ' aria-current="page"' if code == lang else ''
        links.append(f'<a href="{href}" hreflang="{code}" lang="{code}"{cur} onclick="try{{localStorage.setItem(\'dk.lang\',\'{code}\')}}catch(e){{}}">{code.upper()}</a>')
    return f'<nav class="lang" aria-label="{META[lang][1]}">' + ''.join(links) + '</nav>'

# Nicht-deutschsprachige Browser beim ersten Besuch auf /en/ leiten (nur ohne gespeicherte Wahl)
REDIRECT = """<script>try{if(!localStorage.getItem('dk.lang')&&!/^de\\b/i.test(navigator.language||'')&&(location.pathname==='/'||location.pathname==='/index.html'))location.replace('/en/')}catch(e){}</script>"""

def page(src, lang):
    i = src.index('<div class="wrap">')
    head, body = src[:i], src[i:]
    redirect = REDIRECT if lang == 'de' else ''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{META[lang][0]}">
<meta name="theme-color" content="#17675F">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Dial-in">
<link rel="alternate" hreflang="de" href="/">
<link rel="alternate" hreflang="en" href="/en/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='14' fill='%2317675F'/%3E%3Cpath d='M16 6 L19 16 L16 26 L13 16Z' fill='white'/%3E%3C/svg%3E">
{redirect}
{head}<style>html{{color-scheme:light}}:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}@media (prefers-color-scheme: dark){{html{{color-scheme:dark}}}}</style>
</head>
<body>
{body}
</body>
</html>
'''

# Deutsch
de = template.replace('__SAMPLE__', sample_de)
os.makedirs('dist', exist_ok=True)
open('dist/claude-artifact.html', 'w').write(de.replace('<!--LANG-->', ''))
open('index.html', 'w').write(page(de.replace('<!--LANG-->', lang_switch('de')), 'de'))

# Englisch
en_src, left = i18n.translate(template, i18n_en.EXACT, i18n_en.PHRASES)
en = en_src.replace('__SAMPLE__', sample_en).replace('<!--LANG-->', lang_switch('en'))
os.makedirs('en', exist_ok=True)
open('en/index.html', 'w').write(page(en, 'en'))

if left:
    print(f'Hinweis: {len(left)} Textstellen ohne englische Übersetzung:')
    for s in left: print('  ', repr(s[:160]))
else:
    print('Alle Textstellen übersetzt.')
