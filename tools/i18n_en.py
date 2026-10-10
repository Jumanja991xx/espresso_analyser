# English translation table for the Dial-in Kompass.
# EXACT: whole text segment (string literal / template text / HTML text) → English.
# PHRASES: substrings inside longer segments (HTML templates). Keep them specific
# (with tags or several words), so they never hit unrelated text.

EXACT = {
    # Header / reset
    'Beanconqueror · Espresso-Dial-in': 'Beanconqueror · Espresso dial-in',
    'Lädt deinen Beanconqueror-Export samt Waagenkurven, analysiert jeden Shot und rechnet aus Mahlgrad, Zeit, Ausbeute, erstem Tropfen und Geschmack den nächsten Shot aus.':
        'Loads your Beanconqueror export including scale curves, analyses every shot and works out your next shot from grind, time, yield, first drip and taste.',
    'Dateien laden': 'Load files',
    'Alle Daten löschen': 'Delete all data',
    'Alle Shots, Kurven, Rezepte und Zugangsdaten in diesem Browser löschen?': 'Delete all shots, curves, recipes and credentials in this browser?',
    'Löschen': 'Delete',
    'Abbrechen': 'Cancel',
    'Mühle': 'Grinder', 'Zeit': 'Time',
    '), bei ': '), at ', '“': '”',
    'de-DE': 'en-GB',

    # Tastes
    'sauer': 'sour', 'bitter': 'bitter', 'spitz/scharf': 'sharp', 'dünn': 'thin',
    'unausgewogen': 'unbalanced', 'gut/rund': 'good/round',
    'leicht': 'slight', 'mittel': 'medium', 'deutlich': 'strong',
    'hoch': 'high', 'niedrig': 'low',
    'dunkle': 'dark', 'mittlere': 'medium', 'helle': 'light',

    # Import errors
    'Im Export fehlt das Blatt mit den Bezügen (Spalten „Mahlgrad“, „Zeit“, „Bohnensorte“).': 'The export has no brews sheet (columns “Mahlgrad/Grind size”, “Zeit/Time”, “Bohnensorte/Bean”).',
    'Der Export enthält keine Bezüge.': 'The export contains no brews.',
    'Das Backup enthält keine Bezüge.': 'The backup contains no brews.',
    'Kurve': 'curve',
    'Plan': 'plan',

    # Recommendation
    'lief mit ': 'ran ', ' s zu schnell': ' s, too fast', ' s zu lange': ' s, too long',
    'lag mit ': 'was within the time window at ', ' s im Zeitfenster': ' s',
    'hat keine Zeit eingetragen': 'has no time recorded',
    'Sauer und bitter zugleich spricht für Channeling: Ein Teil des Pucks wird über-, ein Teil unterextrahiert.':
        'Sour and bitter at the same time points to channeling: part of the puck is over-extracted, part under-extracted.',
    'Puck-Vorbereitung prüfen: WDT gründlich, Bett eben, gerade tampen, Siebgröße passend zur Dosis. Erst danach weiter am Mahlgrad drehen.':
        'Check puck prep: thorough WDT, level bed, straight tamp, basket size matching the dose. Only then keep adjusting the grind.',
    'Der Shot schmeckte gut und ': 'The shot tasted good and ',
    'Rezept halten. Wenn du feintunen willst: Ratio um ±0,1 verändern und vergleichen.': 'Keep the recipe. To fine-tune: change the ratio by ±0.1 and compare.',
    'Sauer': 'Sour', 'Spitz': 'Sharp',
    ' und zu schnell: klassische Unterextraktion. Feiner mahlen, damit der Shot länger läuft.': ' and too fast: classic under-extraction. Grind finer so the shot runs longer.',
    ', obwohl die Zeit passt: mehr Ausbeute (längere Ratio) zieht mehr Süße und Körper.': ', although the time is right: more yield (longer ratio) pulls more sweetness and body.',
    'Zusätzlich 1 °C wärmer brühen.': 'Also brew 1 °C hotter.',
    ' trotz langer Laufzeit deutet auf ungleichmäßigen Durchfluss oder zu kühles Wasser.': ' despite a long shot time points to uneven flow or water that is too cool.',
    'Puck-Vorbereitung prüfen (WDT, gerade tampen). Die Temperatur leicht anheben.': 'Check puck prep (WDT, straight tamp). Raise the temperature slightly.',
    ': Ausbeute leicht erhöhen.': ': increase the yield slightly.',
    'Bitter und zu lange: Überextraktion. Gröber mahlen, damit der Shot schneller läuft.': 'Bitter and too long: over-extraction. Grind coarser so the shot runs faster.',
    'Bitter bei passender Zeit: Shot früher stoppen (kürzere Ratio).': 'Bitter with the right time: stop the shot earlier (shorter ratio).',
    'Zusätzlich 1 °C kühler brühen.': 'Also brew 1 °C cooler.',
    'Bitter trotz schneller Laufzeit ist untypisch und deutet meist auf Channeling oder eine dunkle Röstung hin.': 'Bitter despite a fast shot is unusual and usually points to channeling or a dark roast.',
    'Puck-Vorbereitung prüfen und die Temperatur um 1–2 °C senken.': 'Check puck prep and lower the temperature by 1–2 °C.',
    'Bitter: Ausbeute leicht reduzieren.': 'Bitter: reduce the yield slightly.',
    'Keine Geschmacksangabe. Der Shot ': 'No taste recorded. The shot ',
    ', die Empfehlung steuert auf die Mitte des Zeitfensters.': ', so the recommendation aims for the middle of the time window.',
    'Dünn und wässrig: etwas mehr Kaffeemehl und eine kürzere Ratio geben mehr Körper.': 'Thin and watery: a little more coffee and a shorter ratio give more body.',
    'Der erste Tropfen kam schon nach ': 'The first drip came after only ',
    ' s. Das Wasser findet sehr schnell einen Weg durch den Puck: Verteilung und Tampen prüfen, eher feiner.': ' s. Water finds a path through the puck very quickly: check distribution and tamping, grind finer.',
    'Der erste Tropfen kam erst nach ': 'The first drip only came after ',
    ' s. Der Puck ist sehr dicht, für die eigentliche Extraktion bleibt wenig Zeit.': ' s. The puck is very dense, leaving little time for the actual extraction.',
    'Die Waagenkurve zeigt bei ': 'The scale curve shows a flow jump at ',
    ' s einen Flow-Sprung um ': ' s of ',
    ' g/s, ein typisches Zeichen für Channeling.': ' g/s, a typical sign of channeling.',
    'Nur leichter Fehlgeschmack: kleine Schritte bei Ratio und Temperatur.': 'Only a slight off-taste: small steps in ratio and temperature.',
    'Deutlicher Fehlgeschmack: größere Schritte bei Ratio und Temperatur.': 'Strong off-taste: bigger steps in ratio and temperature.',
    'Die Daten verlangen eine größere Änderung. Die Empfehlung geht bewusst nur einen Teil des Weges, danach neu bewerten.': 'The data call for a bigger change. The recommendation deliberately goes only part of the way; taste and re-assess.',
    'halten': 'keep', 'gröber': 'coarser', 'feiner': 'finer',

    # Charts
    'Mahlgrad bleibt': 'Grind unchanged',
    'Stufe': 'step', 'Stufen': 'steps', 'Klick': 'click', 'Klicks': 'clicks',
    'gröber ←  Mahlgrad  → feiner': 'coarser ←  grind  → finer',
    'feiner ←  Mahlgrad  → gröber': 'finer ←  grind  → coarser',

    # Effects (calculator)
    '<b>Weniger Kaffeemehl (': '<b>Less coffee (',
    '<b>Mehr Kaffeemehl (': '<b>More coffee (',
    ' g):</b> leichterer, klarerer Espresso mit etwas weniger Körper. Der dünnere Puck bremst weniger, deshalb muss die Mühle feiner. Im 17–19-g-Sieb bleibt bei weniger Dosis mehr Platz über dem Puck, der Puck wird nasser und kann leichter channeln.':
        ' g):</b> lighter, clearer espresso with a little less body. The thinner puck resists less, so the grinder has to go finer. In a 17–19 g basket a smaller dose leaves more headspace; the puck gets wetter and channels more easily.',
    ' g):</b> mehr Körper und Intensität in der Tasse. Der höhere Puck bremst stärker, deshalb muss die Mühle gröber. Darauf achten, dass der Puck die Dusche nicht berührt.':
        ' g):</b> more body and intensity in the cup. The taller puck resists more, so the grinder has to go coarser. Make sure the puck does not touch the shower screen.',
    '<b>Längere Ratio (1:': '<b>Longer ratio (1:',
    '):</b> mehr Extraktion, Säure tritt zurück, mehr Süße. Zu weit gedreht wird es dünner und am Ende bitter-trocken.': '):</b> more extraction, acidity recedes, more sweetness. Pushed too far it gets thinner and bitter-dry at the end.',
    '<b>Kürzere Ratio (1:': '<b>Shorter ratio (1:',
    '):</b> konzentrierter, sirupiger, mehr Körper. Säure und Fruchtigkeit treten stärker hervor.': '):</b> more concentrated, syrupy, more body. Acidity and fruit come forward.',
    '<b>Wärmer (': '<b>Hotter (',
    ' °C):</b> extrahiert stärker. Säure wird runder, Röstaromen und Bitterkeit nehmen zu. Läuft minimal schneller.': ' °C):</b> extracts more. Acidity gets rounder, roast notes and bitterness increase. Runs very slightly faster.',
    '<b>Kühler (': '<b>Cooler (',
    ' °C):</b> extrahiert schwächer. Weniger Bitterkeit und Röstschärfe, dafür mehr Säure. Gut für dunkle Röstungen und Robusta-Anteil.': ' °C):</b> extracts less. Less bitterness and roast harshness, more acidity. Good for dark roasts and robusta blends.',
    '<b>Längere Kontaktzeit (': '<b>Longer contact time (',
    ' s):</b> feiner mahlen erhöht die Extraktion, mehr Süße und Körper, weniger Säure.': ' s):</b> grinding finer increases extraction: more sweetness and body, less acidity.',
    '<b>Kürzere Kontaktzeit (': '<b>Shorter contact time (',
    ' s):</b> gröber mahlen senkt die Extraktion, weniger Bitterkeit, eventuell mehr Säure.': ' s):</b> grinding coarser lowers extraction: less bitterness, possibly more acidity.',
    '<span class="muted">Für eine ': '<span class="muted">For a ',
    ' Röstung liegt der übliche Bereich bei ': ' roast the usual range is ',

    # Goals
    'weniger sauer': 'less sour', 'weniger bitter': 'less bitter', 'mehr Süße': 'more sweetness', 'mehr Körper': 'more body',
    'klarer, leichter': 'clearer, lighter', 'weniger trocken': 'less dry', 'intensiver': 'more intense',
    'Feiner mahlen': 'Grind finer', 'Längere Kontaktzeit extrahiert mehr Süße.': 'Longer contact time extracts more sweetness.',
    'Länger laufen lassen': 'Run it longer', 'Mehr Ausbeute bei gleichem Mahlgrad-Ziel.': 'More yield with the same time target.',
    'Wärmer brühen': 'Brew hotter', 'Mehr Extraktion ohne Rezeptumbau.': 'More extraction without changing the recipe.',
    'Kühler brühen': 'Brew cooler', 'Der schnellste Hebel gegen Bitterkeit und Röstschärfe.': 'The quickest lever against bitterness and roast harshness.',
    'Früher stoppen': 'Stop earlier', 'Die letzten Gramm sind die bittersten.': 'The last grams are the most bitter.',
    'Gröber mahlen': 'Grind coarser', 'Kürzere Kontaktzeit, weniger Extraktion.': 'Shorter contact time, less extraction.',
    'Etwas feiner': 'Slightly finer', 'Süße liegt zwischen sauer und bitter. Ein kleiner Schritt mehr Extraktion.': 'Sweetness sits between sour and bitter. One small step more extraction.',
    'Etwas länger': 'Slightly longer', 'Ratio leicht erhöhen.': 'Raise the ratio a little.',
    '1 °C wärmer': '1 °C hotter', 'Hilft vor allem, wenn noch Säure stört.': 'Helps most if acidity still bothers you.',
    'Kürzere Ratio': 'Shorter ratio', 'Konzentrierter, sirupiger.': 'More concentrated, syrupy.',
    'Mehr Dosis': 'More dose', 'Mehr Kaffee bei gleicher Ratio.': 'More coffee at the same ratio.',
    'Etwas kühler': 'Slightly cooler', 'Bei dunklen Röstungen oft cremiger.': 'Often creamier with dark roasts.',
    'Längere Ratio': 'Longer ratio', 'Weniger konzentriert, Aromen getrennter.': 'Less concentrated, flavours more separated.',
    'Weniger Dosis': 'Less dose', 'Leichterer Espresso bei gleicher Ratio.': 'Lighter espresso at the same ratio.',
    'Etwas wärmer': 'Slightly hotter', 'Mehr Extraktion bei längerer Ratio.': 'More extraction with a longer ratio.',
    'Etwas gröber': 'Slightly coarser', 'Trockenheit kommt oft von zu feinem Mahlgut oder Channeling.': 'Dryness often comes from grinding too fine or from channeling.',
    'Das Ende des Shots trägt die meiste Adstringenz.': 'The end of the shot carries most of the astringency.',
    'Kühler': 'Cooler', 'Weniger herbe Röstnoten.': 'Fewer harsh roast notes.',
    'Mehr gelöste Stoffe pro Gramm.': 'More dissolved solids per gram.',
    '<section class="card"><h2>Rezept-Werkstatt</h2><p class="muted">Dafür braucht es einen Shot mit Mahlgrad, Dosis, Ausbeute und Zeit.</p></section>':
        '<section class="card"><h2>Recipe workshop</h2><p class="muted">This needs a shot with grind, dose, yield and time.</p></section>',
    ' · Mahlgrad ': ' · grind ',
    ' Für deine ': ' For your ',
    ' Röstung ist ': ' roast, ',
    ' °C ein guter Bereich.': ' °C is a good range.',
    'aus deinen Bezügen': 'from your shots',
    'aus einer Faustregel, bis genug Daten da sind': 'from a rule of thumb until there is enough data',
    '1 Klick': '1 click',
    ' s; 1 g weniger Dosis braucht etwa ': ' s; 1 g less dose needs about ',
    ' feiner für dieselbe Zeit.': ' finer for the same time.',
    ' Erster Tropfen: pro ': ' First drip: per ',
    ' feiner ca. ': ' finer about ',
    ' s später.': ' s later.',
    '1–2 Klicks': '1–2 clicks',
    '0,1': '0.1', '0,1–0,2': '0.1–0.2', '0,6 Einheiten': '0.6 units', '3 Klicks': '3 clicks',
    '0,1 Einheit ≈ 1,5 s': '0.1 unit ≈ 1.5 s', '1 Klick ≈ 3 s': '1 click ≈ 3 s',

    # Findings
    'Dosis fehlt': 'Dose missing',
    'Im Shot ist 0 g Kaffeemehl eingetragen. Ratio und Ausbeute-Vergleich sind dadurch nicht aussagekräftig.': 'The shot has 0 g of coffee recorded, so ratio and yield comparisons are meaningless.',
    'Erster Tropfen nicht erfasst': 'First drip not recorded',
    'Mit dem Drip-Timer in Beanconqueror oder einer Waage lässt sich der Puckwiderstand viel genauer beurteilen.': 'With the drip timer in Beanconqueror or a scale, puck resistance can be judged much more precisely.',
    'Erster Tropfen sehr früh (': 'Very early first drip (',
    'Das Wasser bricht schnell durch. Typische Ursachen: zu grob, ungleichmäßige Verteilung, schiefer Tamp.': 'Water breaks through quickly. Typical causes: too coarse, uneven distribution, crooked tamp.',
    'Erster Tropfen früh (': 'Early first drip (',
    'Grenzwertig früh. Läuft der Shot zudem schnell und sauer, feiner mahlen.': 'Borderline early. If the shot also runs fast and sour, grind finer.',
    'Erster Tropfen nach ': 'First drip after ',
    'Passt für eine Maschine ohne Preinfusion.': 'Fine for a machine without pre-infusion.',
    'Erster Tropfen spät (': 'Late first drip (',
    'Der Puck ist recht dicht. Wenn der Shot bitter wird, etwas gröber.': 'The puck is fairly dense. If the shot turns bitter, go a little coarser.',
    'Erster Tropfen sehr spät (': 'Very late first drip (',
    'Der Puck blockiert lange. Für die eigentliche Extraktion bleibt wenig Zeit, eher gröber mahlen.': 'The puck holds back for a long time, leaving little time for extraction. Grind coarser.',
    'Durchfluss Hauptphase ': 'Main-phase flow ',
    'Nah am Zielwert von ': 'Close to the target of ',
    'Schneller': 'Faster', 'Langsamer': 'Slower',
    ' als die ': ' than the ',
    ' g/s, die für ': ' g/s needed for ',
    ' g im Zielfenster nötig sind (': ' g in the time window (',
    'Laufzeit ': 'Shot time ',
    'Unter dem Zielfenster ': 'Below the time window ',
    'Über dem Zielfenster ': 'Above the time window ',
    'Im Zielfenster.': 'Within the time window.',
    'Im Zielbereich.': 'Within the target range.',
    'Länger': 'Longer', 'Kürzer': 'Shorter',
    ' als dein Ziel 1:': ' than your target 1:',
    'Bohnenalter unbekannt': 'Bean age unknown',
    'Röstdatum oben beim Ausgangs-Shot eintragen.': 'Enter the roast date above at the base shot.',
    'Bohne ': 'Beans ',
    ' Tage alt': ' days old',
    'Sehr frisch, starkes Ausgasen kann zu unruhigen Shots führen.': 'Very fresh; strong degassing can make shots erratic.',
    'Im guten Fenster.': 'In the sweet spot.',
    'Älter: läuft schneller, Aromen werden flacher. Feiner mahlen gleicht das teilweise aus.': 'Older: runs faster, flavours get flatter. Grinding finer partly compensates.',
    'Deutlich gealtert. Dial-in wird zunehmend schwierig.': 'Clearly aged. Dialling in gets harder and harder.',
    'Temperatur ': 'Temperature ',
    ' °C unplausibel': ' °C implausible',
    'Vermutlich ein Tippfehler, der Wert wird ignoriert.': 'Probably a typo; the value is ignored.',
    'Extraktion ': 'Extraction ',
    'Unter 18 %: eher unterextrahiert.': 'Below 18 %: likely under-extracted.',
    'Über 22 %: eher überextrahiert.': 'Above 22 %: likely over-extracted.',
    'Im klassischen Bereich von 18–22 %.': 'In the classic 18–22 % range.',
    'Unruhiger Flow (Schwankung ': 'Unsteady flow (variation ',
    'Der Durchfluss schwankt in der Hauptphase stark. Häufig ein Zeichen für ungleichmäßige Verteilung.': 'Flow varies a lot during the main phase, often a sign of uneven distribution.',
    'Gleichmäßiger Flow (Schwankung ': 'Steady flow (variation ',
    'Der Puck hält gleichmäßig.': 'The puck holds evenly.',
    'Flow-Sprung bei ': 'Flow jump at ',
    'Der Durchfluss steigt innerhalb einer Sekunde um ': 'Flow rises within one second by ',
    ' g/s. Typisch für Channeling.': ' g/s. Typical of channeling.',
    'Flow steigt zum Ende stark an': 'Flow rises sharply towards the end',
    'Im letzten Viertel ': 'In the last quarter ',
    ' % schneller als in der Mitte. Der Puck baut ab, die letzten Gramm schmecken dann oft dünn oder bitter.': ' % faster than in the middle. The puck is breaking down; the last grams often taste thin or bitter.',
    'Spitzenflow ': 'Peak flow ',
    'Sehr hoch für Espresso.': 'Very high for espresso.',
    'Druckspitze ': 'Pressure peak ',
    'Über 10 bar. OPV-Einstellung der Maschine prüfen.': 'Above 10 bar. Check the machine’s OPV setting.',

    # Analysis metrics
    'Mahlgrad': 'Grind', 'Dosis → Ausbeute': 'Dose → yield', 'Laufzeit': 'Shot time', 'Erster Tropfen': 'First drip',
    'aus Waagenkurve': 'from scale curve', 'Ø Flow gesamt': 'Avg flow overall', 'Ø Flow Hauptphase': 'Avg flow main phase',
    '15–90 % der Ausbeute': '15–90 % of yield', 'nach 1. Tropfen': 'after first drip', 'Temperatur': 'Temperature',
    'Bohnenalter': 'Bean age', ' Tage': ' days', 'Bewertung': 'Rating', 'Spitzenflow': 'Peak flow', 'bei ': 'at ',
    '1 g/s erreicht': '1 g/s reached', 'Flow-Schwankung': 'Flow variation', 'Hauptphase': 'main phase', 'Druck': 'Pressure',
    'Spitze ': 'peak ', 'Ausbeute': 'Yield', 'Geschmack': 'Taste',
    'Dieser Shot': 'This shot', 'Vorheriger': 'Previous', 'Gewählter Vergleich': 'Chosen comparison', 'Referenz (beste Bewertung)': 'Reference (best rated)',
    ' · Kurve': ' · curve', 'Vergleich': 'Comparison', 'Referenz': 'Reference',
    ', aus Gewicht berechnet': ', calculated from weight',
    ' Laut Backup existiert für diesen Bezug eine Kurve auf deinem Gerät.': ' According to the backup, a curve for this shot exists on your phone.',
    'Ist dein Rezept': 'Is your recipe', 'Als Rezept merken': 'Save as recipe',
    '>Vergleich: ': '>Compare: ',
    'Datum': 'Date', 'Bohne': 'Beans', 'Dosis': 'Dose', 'Temp': 'Temp', 'Notiz': 'Note',
    'Basis': 'Base', 'als Basis': 'use as base',
    'In die Zwischenablage kopiert.': 'Copied to the clipboard.',
    'Wirklich löschen?': 'Really delete?', 'Wirklich entfernen?': 'Really remove?',
    'Kopiert': 'Copied', 'Gespeichert. Neue Empfehlung oben.': 'Saved. New recommendation above.',

    # Insights
    'Einheit': 'unit',
    'mit dieser Bohne': 'with these beans', 'aller Bohnen': 'of all beans',
    'Die Bezüge auf dieser Mühle widersprechen sich (feiner gemahlen lief teils schneller). Häufige Ursachen: unterschiedliche Bohnenalter, Dosis oder Puck-Vorbereitung. Prüfe auch, ob „höhere Zahl = gröber“ für deine Mühle stimmt.':
        'The shots on this grinder contradict each other (finer sometimes ran faster). Common causes: different bean ages, dose or puck prep. Also check whether “higher number = coarser” is right for your grinder.',
    'Noch zu wenige Bezüge mit unterschiedlichem Mahlgrad.': 'Not enough shots with different grind settings yet.',
    'Tendenz Unterextraktion: eher feiner, länger, wärmer.': 'Leaning under-extracted: finer, longer, hotter.',
    'Tendenz Überextraktion: eher gröber, kürzer, kühler.': 'Leaning over-extracted: coarser, shorter, cooler.',
    'Sauer und bitter halten sich die Waage, das spricht für ungleichmäßige Extraktion.': 'Sour and bitter are balanced, which points to uneven extraction.',
    '× sauer · ': '× sour · ', '× bitter · ': '× bitter · ',
    'Die Bohne war beim letzten Bezug ': 'At the last shot the beans were ',
    ' Tage alt. Sehr frischer Kaffee gast stark aus und läuft unruhig, einige Tage Ruhe helfen.': ' days old. Very fresh coffee degasses strongly and runs erratically; a few days of rest help.',
    ' Tage alt. Älterer Kaffee läuft schneller und schmeckt flacher, du wirst nach und nach feiner mahlen müssen.': ' days old. Older coffee runs faster and tastes flatter; you will gradually need to grind finer.',
    ' Tage alt und liegt im guten Fenster.': ' days old, in the sweet spot.',
    'Die Bezüge stammen aus ': 'The shots come from ',
    ' Packungen': ' bags', ' (Röstung ': ' (roasted ', ' und ': ' and ',
    '. Unterschiedlich alte Bohnen verschieben den passenden Mahlgrad.': '. Beans of different ages shift the right grind setting.',
    'Entkoffeinierter Kaffee ist meist löslicher und läuft schneller. Wird er bitter, lieber 1–2 °C kühler brühen als gröber mahlen.': 'Decaf is usually more soluble and runs faster. If it turns bitter, brew 1–2 °C cooler rather than grinding coarser.',
    ' Bezüge seit Rückspülen': ' shots since backflush', 'Rückspülen nicht erfasst': 'Backflush not recorded',
    ' Bezüge seit dem Entkalken. ': ' shots since descaling. ',
    '× Dosis 0 g': '× dose 0 g', '× unplausible Temperatur': '× implausible temperature', '× ohne Zeit': '× no time', '× ohne Bewertung': '× no rating',
    '× gut</span><p>': '× good</span><p>',

    # Table / status / welcome
    ' Bezüge': ' shots', ' neu': ' new', ' Mühlen': ' grinders', ' Bohnen · ': ' beans · ',
    'Noch keine Daten geladen': 'No data loaded yet',
    '<div class="card empty">Für diese Kombination gibt es noch keine Bezüge.</div>': '<div class="card empty">No shots for this combination yet.</div>',
    ' · neu erfasst': ' · added here',
    ' Tage nach Röstung': ' days after roasting',
    ' · erster Tropfen nach ': ' · first drip after ',
    'Mahlgrad nicht numerisch': 'Grind is not numeric',
    '<br>Waage stoppen bei ': '<br>stop the scale at ',
    ': Mahlgrad ': ': grind ',
    'Der Mahlgrad ist aus deinen eigenen Bezügen errechnet (Durchfluss in g/s je Mahlgrad-Stufe, neuere Bezüge zählen stärker).': 'The grind is calculated from your own shots (flow in g/s per grind step; newer shots count more).',
    'Der Mahlgrad folgt einer Faustregel (': 'The grind follows a rule of thumb (',
    '), weil die Daten noch keinen klaren Zusammenhang zeigen.': ') because the data do not show a clear relationship yet.',
    'Waagenkurven': 'scale curves', 'eingetragenen Shots': 'logged shots',
    ': nach dem Stoppen kommen im Schnitt noch ': ': after stopping, on average another ',
    ' g in die Tasse.</span>': ' g ends up in the cup.</span>',
    '> nur ': '> only ',

    # Import / sync
    'Die Excel-Bibliothek konnte nicht geladen werden. Prüfe die Internetverbindung und lade die Seite neu.': 'The Excel library could not be loaded. Check your internet connection and reload the page.',
    'Visualizer ist von dieser Seite aus nicht erreichbar. Der Cloud-Sync funktioniert nur in der selbst gehosteten Version (z. B. auf Vercel), nicht in der Claude-Vorschau.': 'Visualizer cannot be reached from this page. Cloud sync only works in the self-hosted version (e.g. on Vercel), not in the Claude preview.',
    'Anmeldung bei Visualizer fehlgeschlagen. E-Mail und Passwort prüfen.': 'Visualizer sign-in failed. Check email and password.',
    'Visualizer bremst gerade (zu viele Anfragen). In einer Minute erneut versuchen.': 'Visualizer is rate-limiting (too many requests). Try again in a minute.',
    'Visualizer antwortet mit Fehler ': 'Visualizer responded with error ',
    'Bitte E-Mail und Passwort deines Visualizer-Kontos eintragen.': 'Please enter the email and password of your Visualizer account.',
    'Verbinde …': 'Connecting …', 'Lade Shot ': 'Loading shot ', ' von ': ' of ',
    'Cloud-Sync: ': 'Cloud sync: ', ' neue Shots, ': ' new shots, ', ' Waagenkurven': ' scale curves',
    ' ohne Beanconqueror-Daten übersprungen': ' skipped (no Beanconqueror data)',
    ' Noch ': ' Another ', ' weitere, nochmal synchronisieren.': ' remaining; sync again.',
    'ZIP-Bibliothek nicht geladen': 'ZIP library not loaded',
    'Kein Beanconqueror-Backup im ZIP gefunden': 'No Beanconqueror backup found in the ZIP',
    'unbekanntes JSON-Format': 'unknown JSON format',
    ' Bezüge geladen.': ' shots loaded.',
    ': keine verwertbaren Messwerte': ': no usable measurements',
    ': kein passender Shot gefunden': ': no matching shot found',
    'Waagenkurve ': 'Scale curve ', ' → Shot ': ' → shot ',
    '. Falls falsch: in der Analyse verschieben.': '. If wrong: move it in the analysis.',
    'Nicht importiert: ': 'Not imported: ', 'Import abgeschlossen': 'Import complete', 'Nichts importiert.': 'Nothing imported.',
    'Backup ': 'Backup ', 'Export ': 'Export ',
    'Beispieldaten': 'Sample data',
    '<summary>Cloud-Sync mit Visualizer': '<summary>Cloud sync with Visualizer',
    ' <span class="muted" style="font-weight:400">· zuletzt ': ' <span class="muted" style="font-weight:400">· last ',
    'Datenqualität': 'Data quality',
}

PHRASES = [
    # SVG / chart text
    ('aria-label="Extraktionskarte: Zeit gegen Ratio"', 'aria-label="Extraction map: time vs ratio"'),
    ('>← schneller: eher sauer</text>', '>← faster: tends sour</text>'),
    ('>langsamer: eher bitter →</text>', '>slower: tends bitter →</text>'),
    ('>Zeit (s)</text>', '>Time (s)</text>'),
    ('<title>Nächster Shot</title>', '<title>Next shot</title>'),
    ('aria-label="Mahlgrad gegen Laufzeit"', 'aria-label="Grind vs shot time"'),
    ('<title>Mahlgrad ', '<title>Grind '),
    ('>Zielbereich</text>', '>Target</text>'),
    ('>Zeitfenster ', '>Time window '),
    ('<title>Empfehlung</title>', '<title>Recommendation</title>'),
    ('<title>Flow-Sprung</title>', '<title>Flow jump</title>'),
    ('aria-label="Mahlgradskala"', 'aria-label="Grind scale"'),
    ('aria-label="Zeitlicher Ablauf des Shots"', 'aria-label="Shot timeline"'),
    ('>1. Tropfen ', '>First drip '), ('>1. Tropfen<', '>First drip<'),
    ('>Stopp ', '>Stop '),
    ('>Zielfenster ', '>Time window '),
    ('aria-label="Waagenkurve: Gewicht und Durchfluss"', 'aria-label="Scale curve: weight and flow"'),
    ('>Druck (0–12 bar)<', '>Pressure (0–12 bar)<'),
    ('>Gewicht (g)<', '>Weight (g)<'), ('>Durchfluss (g/s)', '>Flow (g/s)'),

    # Workshop
    ('<h2 id="hWs">Rezept-Werkstatt</h2>', '<h2 id="hWs">Recipe workshop</h2>'),
    ('>Ausgangspunkt: ', '>Starting point: '),
    ('<h3>Geschmack gezielt verändern</h3>', '<h3>Change the taste on purpose</h3>'),
    ('">In Rechner</button>', '">To calculator</button>'),
    ('<span class="num opt-plan">Mahlgrad ', '<span class="num opt-plan">Grind '),
    ('Immer nur einen Hebel pro Shot ändern, dann bewerten. Die Reihenfolge entspricht der Wirksamkeit für dieses Ziel.', 'Change only one lever per shot, then taste. The order reflects how effective each lever is for this goal.'),
    ('<h3>Rechner: was passiert, wenn …</h3>', '<h3>Calculator: what happens if …</h3>'),
    ('>Dosis g<', '>Dose g<'), ('>Ausbeute g<', '>Yield g<'), ('>Zielzeit s<', '>Target time s<'),
    ('>Ausbeute an Dosis anpassen (1:', '>Match yield to dose (1:'),
    ('>Zurücksetzen<', '>Reset<'),
    ('<span class="k">Mahlgrad</span>', '<span class="k">Grind</span>'),
    ('<span class="k">Ohne Mühlenänderung</span>', '<span class="k">Without grinder change</span>'),
    ('<span class="k">Mit neuem Mahlgrad</span>', '<span class="k">With new grind</span>'),
    ('<span class="d">Ziel ', '<span class="d">Target '),
    ('Werte ändern, um die Wirkung zu sehen.', 'Change values to see the effect.'),
    ('>Als Ziel für den nächsten Shot setzen<', '>Set as target for the next shot<'),
    ('Rechnung: Der Durchfluss sinkt etwa im Verhältnis zur Puckhöhe (Dosis), die Mahlgrad-Wirkung kommt ', 'Method: flow drops roughly in proportion to puck height (dose); the grind effect comes '),
    ('. Temperatur ändert die Laufzeit kaum.', '. Temperature barely changes the shot time.'),
    ('<h3>Mühlen-Kalibrierung · ', '<h3>Grinder calibration · '),
    ('>Erwartete Laufzeit je Mahlgrad für Ratio 1:', '>Expected shot time per grind setting at ratio 1:'),
    (' und drei Dosen. Grün liegt im Zielfenster ', ' and three doses. Green is within the time window '),
    ('<th>Mahlgrad</th><th>Durchfluss</th>', '<th>Grind</th><th>Flow</th>'),
    ('<th>Gemessen</th>', '<th>Measured</th>'),
    (' <span class="badge">jetzt</span>', ' <span class="badge">now</span>'),
    ('<summary>Alle Hebel im Überblick</summary>', '<summary>All levers at a glance</summary>'),
    ('<th>Hebel</th><th>Richtung</th><th>Geschmack</th><th>Typischer Schritt</th><th>Nebenwirkung</th>', '<th>Lever</th><th>Direction</th><th>Taste</th><th>Typical step</th><th>Side effect</th>'),
    ('<td>Mahlgrad</td><td>feiner</td><td>weniger sauer, mehr Süße und Körper; zu weit: bitter, trocken</td>', '<td>Grind</td><td>finer</td><td>less sour, more sweetness and body; too far: bitter, dry</td>'),
    ('<td>längere Zeit, späterer erster Tropfen</td>', '<td>longer time, later first drip</td>'),
    ('<td>Ratio</td><td>länger</td><td>weniger Säure, mehr Süße, dünner; zu weit: bitter-trocken</td><td>0,1–0,2 (2–4 g)</td><td>längere Zeit bei gleichem Mahlgrad</td>', '<td>Ratio</td><td>longer</td><td>less acidity, more sweetness, thinner; too far: bitter-dry</td><td>0.1–0.2 (2–4 g)</td><td>longer time at the same grind</td>'),
    ('<td>Ratio</td><td>kürzer</td><td>mehr Körper und Intensität, mehr Säure</td><td>0,1–0,2</td><td>kürzere Zeit</td>', '<td>Ratio</td><td>shorter</td><td>more body and intensity, more acidity</td><td>0.1–0.2</td><td>shorter time</td>'),
    ('<td>Temperatur</td><td>wärmer</td><td>Säure runder, mehr Röst- und Bitternoten</td><td>1–2 °C</td><td>kaum Einfluss auf die Zeit</td>', '<td>Temperature</td><td>hotter</td><td>rounder acidity, more roast and bitter notes</td><td>1–2 °C</td><td>barely affects time</td>'),
    ('<td>Temperatur</td><td>kühler</td><td>weniger bitter, weicher, Säure deutlicher</td><td>1–2 °C</td><td>dunkle Röstungen profitieren oft</td>', '<td>Temperature</td><td>cooler</td><td>less bitter, softer, acidity more pronounced</td><td>1–2 °C</td><td>dark roasts often benefit</td>'),
    ('<td>Dosis</td><td>mehr</td><td>mehr Körper (bei gleicher Ratio)</td><td>0,5–1 g</td><td>gröber nötig, weniger Platz zur Dusche</td>', '<td>Dose</td><td>more</td><td>more body (at the same ratio)</td><td>0.5–1 g</td><td>coarser needed, less headspace</td>'),
    ('<td>Dosis</td><td>weniger</td><td>leichter, klarer</td><td>0,5–1 g</td><td>feiner nötig, nasserer Puck</td>', '<td>Dose</td><td>less</td><td>lighter, clearer</td><td>0.5–1 g</td><td>finer needed, wetter puck</td>'),
    ('<td>Puck-Vorbereitung</td><td>WDT, gerade tampen</td><td>weniger sauer-bitter gleichzeitig</td><td>bei jedem Shot gleich</td><td>gleichmäßigerer Flow</td>', '<td>Puck prep</td><td>WDT, level tamp</td><td>less sour and bitter at once</td><td>same every shot</td><td>steadier flow</td>'),
    ('<td>Bohnenalter</td><td>älter</td><td>flacher, weniger Aroma</td><td>–</td><td>läuft schneller, nach und nach feiner</td>', '<td>Bean age</td><td>older</td><td>flatter, less aroma</td><td>–</td><td>runs faster, gradually go finer</td>'),

    # Analysis
    ('>Kurve gehört zu einem anderen Shot?</label>', '>Curve belongs to another shot?</label>'),
    ('>verschieben nach …</option>', '>move to …</option>'),
    ('>Kurve entfernen</button>', '>Remove curve</button>'),
    ('<h2 id="hAna">Shot-Analyse</h2>', '<h2 id="hAna">Shot analysis</h2>'),
    ('aria-label="älterer Shot"', 'aria-label="older shot"'), ('aria-label="Shot wählen"', 'aria-label="Choose shot"'),
    ('title="Als Rezept für diese Bohne und Mühle merken"', 'title="Save as recipe for these beans and this grinder"'),
    ('aria-label="Vergleichen mit"', 'aria-label="Compare with"'), ('>Vergleich: bester Shot</option>', '>Compare: best shot</option>'),
    ('aria-label="neuerer Shot"', 'aria-label="newer shot"'),
    ('<div class="note">„', '<div class="note">“'),
    ('“</div>', '”</div>'),
    ('Keine Waagenkurve für diesen Shot. In Beanconqueror lässt sich in der Detailansicht eines Bezugs das Flowprofil als JSON oder Excel herunterladen (oder die Visualizer-Datei). Leg die Datei hier ab, sie wird automatisch dem passenden Shot zugeordnet.',
     'No scale curve for this shot. In Beanconqueror you can download the flow profile of a brew as JSON or Excel from its detail view (or the Visualizer file). Drop the file here and it is matched to the right shot automatically.'),
    ('<h3>Befund</h3>', '<h3>Findings</h3>'),
    ('<h3>Vergleich</h3>', '<h3>Comparison</h3>'),
    ('In Klammern: Unterschied dieses Shots zur jeweiligen Spalte.', 'In brackets: difference of this shot to that column.'),

    # Context bar
    ('<label for="selBean">Bohne</label>', '<label for="selBean">Beans</label>'),
    ('<label for="selGrinder">Mühle</label>', '<label for="selGrinder">Grinder</label>'),
    ('> höhere Zahl = gröber</label>', '> higher number = coarser</label>'),
    ('<label for="tDose">Dosis g</label>', '<label for="tDose">Dose g</label>'),
    ('<label for="tMin">Zeitfenster s</label>', '<label for="tMin">Time window s</label>'),
    ('>Ziele zurücksetzen</button>', '>Reset targets</button>'),

    # Insights
    ('<span class="eyebrow">Dein Referenz-Shot</span>', '<span class="eyebrow">Your reference shot</span>'),
    (' – „', ' – “'),
    ('<span class="eyebrow">Mühlen-Empfindlichkeit</span>', '<span class="eyebrow">Grinder sensitivity</span>'),
    (' s</span><p>Gemessen an ', ' s</span><p>Measured from '),
    (' Bezügen ', ' shots '), (' auf der ', ' on the '),
    (' g Ausbeute.</p></div>', ' g yield.</p></div>'),
    (' Bis dahin rechnet die Empfehlung mit einer Faustregel.</p></div>', ' Until then the recommendation uses a rule of thumb.</p></div>'),
    ('<span class="eyebrow">Geschmackstrend (letzte ', '<span class="eyebrow">Taste trend (last '),
    ('<span class="eyebrow">Bohne', '<span class="eyebrow">Beans'),
    ('<span class="eyebrow">Erster Tropfen & Hauptphase</span>', '<span class="eyebrow">First drip & main phase</span>'),
    (' g/s</span><p>Zeit bis zum ersten Tropfen über ', ' g/s</span><p>Time to first drip over '),
    (' Shots, danach der Durchfluss bis zum Stopp. Für dein Ziel passen etwa 5–10 s und ', ' shots, then the flow until stopping. For your target about 5–10 s and '),
    ('<span class="eyebrow">Röstdatum fehlt</span><p>Für ', '<span class="eyebrow">Roast date missing</span><p>For '),
    (' kennt der Kompass kein Röstdatum. Trag es oben beim Ausgangs-Shot ein, dann fließt das Bohnenalter in Analyse und Hinweise ein.</p></div>', ' there is no roast date. Enter it above at the base shot so bean age feeds into the analysis and tips.</p></div>'),
    ('<span class="eyebrow">Pflege</span>', '<span class="eyebrow">Maintenance</span>'),
    ('Zählt alle erfassten Bezüge seit dem letzten Klick.</p>', 'Counts all recorded shots since the last click.</p>'),
    ('>Heute rückgespült</button>', '>Backflushed today</button>'), ('>Heute entkalkt</button>', '>Descaled today</button>'),
    ('<span class="eyebrow">Datenqualität</span>', '<span class="eyebrow">Data quality</span>'),
    ('Diese Werte fließen nicht in die Berechnung ein. Bewertung und Geschmacksnotiz bei jedem Shot machen die Empfehlung deutlich treffsicherer.', 'These values are left out of the calculation. A rating and taste note for every shot make the recommendation much more accurate.'),

    # History table
    ('<th>Datum</th>', '<th>Date</th>'), ('<th>Bohne</th><th>Mühle</th>', '<th>Beans</th><th>Grinder</th>'),
    ('<th>Mahlgrad</th><th>Dosis</th><th>Ausbeute</th><th>Ratio</th><th>Zeit</th><th>1. Tropfen</th><th>g/s gesamt</th><th>g/s Haupt</th><th>Temp</th><th>Alter</th><th>Bewertung</th><th>Geschmack</th><th>Notiz</th>',
     '<th>Grind</th><th>Dose</th><th>Yield</th><th>Ratio</th><th>Time</th><th>First drip</th><th>g/s overall</th><th>g/s main</th><th>Temp</th><th>Age</th><th>Rating</th><th>Taste</th><th>Note</th>'),
    ('<span class="src">neu</span>', '<span class="src">new</span>'),
    ('title="Waagenkurve vorhanden">Kurve</span>', 'title="Scale curve available">curve</span>'),
    ('title="Dosis fehlt"', 'title="Dose missing"'), ('title="unplausibel"', 'title="implausible"'),
    ('">Analyse</button>', '">Analyse</button>'),
    ('aria-label="Eintrag löschen"', 'aria-label="Delete entry"'),

    # Welcome
    ('<h2 id="hWel">Willkommen beim Dial-in Kompass</h2>', '<h2 id="hWel">Welcome to Dial-in Kompass</h2>'),
    ('<p>Der Kompass liest deine Bezüge aus Beanconqueror, analysiert jeden Shot und sagt dir, wie du Mühle, Dosis, Ausbeute und Temperatur für den nächsten Espresso einstellst. Deine Daten bleiben in diesem Browser.</p>',
     '<p>Dial-in Kompass reads your brews from Beanconqueror, analyses every shot and tells you how to set grinder, dose, yield and temperature for your next espresso. Your data stays in this browser.</p>'),
    ('<li><b>Daten aus Beanconqueror holen.</b> Den Excel-Export oder das Backup (ZIP) speichern. Flowprofile einzelner Bezüge gehen auch.</li>',
     '<li><b>Get your data from Beanconqueror.</b> Save the Excel export or the backup (ZIP). Flow profiles of single brews work too.</li>'),
    ('<li><b>Hier laden.</b> Über „Dateien laden“ oder die Datei einfach auf die Seite ziehen.</li>',
     '<li><b>Load it here.</b> Use “Load files” or simply drag the file onto the page.</li>'),
    ('<li><b>Optional: Cloud-Sync.</b> Mit Visualizer-Upload in Beanconqueror kommen neue Shots automatisch hierher.</li>',
     '<li><b>Optional: cloud sync.</b> With Visualizer upload enabled in Beanconqueror, new shots arrive here automatically.</li>'),
    ('>Dateien laden</label>', '>Load files</label>'),
    ('>Mit Beispieldaten ausprobieren</button>', '>Try with sample data</button>'),
    ('>Cloud-Sync einrichten</button>', '>Set up cloud sync</button>'),
    ('Du siehst erfundene Beispieldaten. Lade deinen eigenen Beanconqueror-Export, um mit deinen Shots zu arbeiten. ', 'You are looking at made-up sample data. Load your own Beanconqueror export to work with your shots. '),
    ('>Beispiel schließen</button>', '>Close sample</button>'),
    ('>Ausblenden</button>', '>Dismiss</button>'),

    # Base shot card
    ('<h2 id="hLast">Ausgangs-Shot</h2>', '<h2 id="hLast">Base shot</h2>'),
    ('<span class="k">Dosis</span>', '<span class="k">Dose</span>'),
    ('<span class="k">Ausbeute</span>', '<span class="k">Yield</span>'),
    ('<span class="k">Zeit</span>', '<span class="k">Time</span>'),
    ('<span class="k">Bewertung</span>', '<span class="k">Rating</span>'),
    ('<label for="roastIn">Röstdatum von <b>', '<label for="roastIn">Roast date of <b>'),
    ('</b> fehlt:</label>', '</b> is missing:</label>'),
    ('>Übernehmen</button>', '>Apply</button>'),
    ('<div class="muted" style="font-size:13px">Bohne beim Bezug ', '<div class="muted" style="font-size:13px">Beans at this shot: '),
    ('>Röstdatum ändern</button>', '>Change roast date</button>'),
    ('<label>Wie hat er geschmeckt?</label>', '<label>How did it taste?</label>'),
    ('<span class="muted">Wie deutlich?</span>', '<span class="muted">How strong?</span>'),
    ('>Aus Notiz übernehmen</button>', '>Take from note</button>'),
    ('Vorauswahl aus deiner Notiz und Bewertung. Antippen, um zu korrigieren.', 'Pre-selected from your note and rating. Tap to correct.'),

    # Next shot card
    ('<h2 id="hRec">Nächster Shot</h2>', '<h2 id="hRec">Next shot</h2>'),
    ('">Sicherheit ', '">Confidence '),
    ('<span class="d">s erwartet</span>', '<span class="d">s expected</span>'),
    ('<b>Dein Rezept</b> für ', '<b>Your recipe</b> for '),
    ('<br><span class="muted">Die Bohne ist seit dem Rezept ', '<br><span class="muted">The beans have aged '),
    (' Tage älter geworden. Älterer Kaffee läuft schneller, rechne eher mit einer feineren Einstellung.</span>', ' days since this recipe. Older coffee runs faster, so expect a finer setting.</span>'),
    ('>Rezept kopieren</button>', '>Copy recipe</button>'), ('>Rezept entfernen</button>', '>Remove recipe</button>'),
    ('>Nachlauf gelernt aus ', '>Post-stop drip learned from '),

    # Charts cards
    ('<h2 id="hMap">Extraktionskarte</h2>', '<h2 id="hMap">Extraction map</h2>'),
    ('</i>sauer/spitz</span>', '</i>sour/sharp</span>'), ('</i>bitter</span>', '</i>bitter</span>'), ('</i>gut</span>', '</i>good</span>'),
    ('</i>gemischt/dünn</span>', '</i>mixed/thin</span>'), ('</i>ohne Angabe</span>', '</i>not rated</span>'),
    ('</svg>nächster Shot</span>', '</svg>next shot</span>'),
    ('<h2 id="hGrind">Mahlgrad und Laufzeit</h2>', '<h2 id="hGrind">Grind and shot time</h2>'),
    ('>Linie: erwartete Zeit bei ', '>Line: expected time at '),

    # Sections
    ('<h2 id="hIns">Was deine Daten zeigen</h2>', '<h2 id="hIns">What your data show</h2>'),
    ('<h2 id="hAdd">Shot eintragen</h2>', '<h2 id="hAdd">Log a shot</h2>'),
    ('Vorausgefüllt mit der Empfehlung. Nach dem Speichern wird er zur neuen Basis.', 'Pre-filled with the recommendation. After saving it becomes the new base.'),
    ('<label for="fGrind">Mahlgrad</label>', '<label for="fGrind">Grind</label>'),
    ('<label for="fDose">Dosis g</label>', '<label for="fDose">Dose g</label>'),
    ('<label for="fYield">Ausbeute g</label>', '<label for="fYield">Yield g</label>'),
    ('<label for="fTime">Zeit s</label>', '<label for="fTime">Time s</label>'),
    ('<label for="fDrip">1. Tropfen s</label>', '<label for="fDrip">First drip s</label>'),
    ('<label for="fRating">Bewertung /', '<label for="fRating">Rating /'),
    ('<label>Geschmack</label>', '<label>Taste</label>'),
    ('<label for="fNotes">Notiz</label>', '<label for="fNotes">Note</label>'),
    ('placeholder="z. B. süßer, noch leicht spitz im Abgang"', 'placeholder="e.g. sweeter, still slightly sharp in the finish"'),
    ('>Shot speichern</button>', '>Save shot</button>'),
    ('>Neue Einträge kopieren (', '>Copy new entries ('),
    ('>Neue Einträge löschen</button>', '>Delete new entries</button>'),
    ('<h2 id="hHist">Verlauf</h2>', '<h2 id="hHist">History</h2>'),
    ('<summary>So rechnet der Kompass</summary>', '<summary>How the Kompass calculates</summary>'),
    ('<li>Basis ist dein letzter Shot dieser Bohnen-Mühlen-Kombination (oder der, den du im Verlauf als Basis wählst).</li>', '<li>The base is your latest shot for this bean/grinder combination (or the one you pick as base in the history).</li>'),
    ('<li>Aus allen Bezügen mit Zeit und Ausbeute wird der Durchfluss (g/s) je Mahlgrad als gewichtete Regression geschätzt. Neuere Bezüge zählen mehr, weil Bohnen mit dem Alter schneller laufen. Reichen die Daten einer Bohne nicht, nutzt der Kompass die Bezüge aller Bohnen auf derselben Mühle.</li>',
     '<li>From all shots with time and yield, flow (g/s) per grind setting is estimated with a weighted regression. Newer shots count more because beans run faster as they age. If one bean has too little data, shots of all beans on the same grinder are used.</li>'),
    ('<li>Der Geschmack entscheidet, was sich ändert: sauer und schnell → feiner; sauer bei passender Zeit → längere Ratio und wärmer; bitter und langsam → gröber; bitter bei passender Zeit → kürzere Ratio und kühler; sauer und bitter → Puck-Vorbereitung.</li>',
     '<li>Taste decides what changes: sour and fast → finer; sour with the right time → longer ratio and hotter; bitter and slow → coarser; bitter with the right time → shorter ratio and cooler; sour and bitter → puck prep.</li>'),
    ('<li>Große Sprünge werden begrenzt (', '<li>Big jumps are capped ('),
    ('), damit du dich in Schritten annäherst. Dosisfehler (0 g) und unplausible Temperaturen werden ignoriert.</li>', ') so you approach the target step by step. Dose errors (0 g) and implausible temperatures are ignored.</li>'),
    ('<li>Die Shot-Analyse nutzt den ersten Tropfen, den Durchfluss danach (Hauptphase), das Bohnenalter und, falls vorhanden, die Waagenkurve: Spitzenflow, Schwankung des Flows, plötzliche Flow-Sprünge (Channeling) und Druck.</li>',
     '<li>The shot analysis uses the first drip, the flow after it (main phase), bean age and, if available, the scale curve: peak flow, flow variation, sudden flow jumps (channeling) and pressure.</li>'),
    ('<li>Importierbar sind: der Excel-Export, das vollständige Backup (ZIP mit Beanconqueror.json, enthält Röstdaten und Millisekunden), Flowprofile einzelner Bezüge als JSON oder Excel sowie Visualizer-Dateien. Mehrere Dateien gleichzeitig ablegen geht auch.</li>',
     '<li>You can import: the Excel export, the full backup (ZIP with Beanconqueror.json, includes roast dates and milliseconds), flow profiles of single brews as JSON or Excel, and Visualizer files. Several files at once work too.</li>'),
    ('<li>Daten bleiben in diesem Browser. Nichts wird hochgeladen.</li>', '<li>Data stays in this browser. Nothing is uploaded.</li>'),

    # Sync box
    ('<p>Beanconqueror kann jeden Bezug samt Waagenkurve automatisch zu visualizer.coffee hochladen. Der Kompass holt sie von dort ab. Einmalig in Beanconqueror die Visualizer-Anbindung mit automatischem Upload aktivieren, dann hier dieselben Zugangsdaten eintragen.</p>',
     '<p>Beanconqueror can upload every brew including its scale curve to visualizer.coffee automatically. The Kompass fetches them from there. Enable the Visualizer connection with automatic upload in Beanconqueror once, then enter the same credentials here.</p>'),
    ('<label for="sEmail">E-Mail</label>', '<label for="sEmail">Email</label>'),
    ('<label for="sPw">Passwort</label>', '<label for="sPw">Password</label>'),
    ('> auf diesem Gerät merken</label>', '> remember on this device</label>'),
    ('>Jetzt synchronisieren</button>', '>Sync now</button>'),
    ('Die Zugangsdaten gehen nur direkt an visualizer.coffee. Mit „merken“ liegen sie im Browserspeicher dieses Geräts, und der Abgleich läuft bei jedem Öffnen automatisch. Ohne Premium liefert Visualizer die Shots der letzten 30 Tage, das reicht fürs Dial-in.',
     'Credentials are only sent directly to visualizer.coffee. With “remember” they are kept in this device’s browser storage and sync runs automatically on every visit. Without premium, Visualizer returns the last 30 days of shots, which is enough for dialling in.'),

    # Header (static HTML)
    ('>Alle Daten löschen</button>', '>Delete all data</button>'),
    ('<span>Alle Shots, Kurven, Rezepte und Zugangsdaten in diesem Browser löschen?</span>', '<span>Delete all shots, curves, recipes and credentials in this browser?</span>'),
    ('>Löschen</button>', '>Delete</button>'), ('>Abbrechen</button>', '>Cancel</button>'),
    ('>Export hier ablegen<', '>Drop export here<'),
]

EXACT.update({
    ' s und ': ' s and ',
    'Danach liefen noch ': 'Another ',
    ' g nach, die Tasse endete bei ': ' g ran into the cup afterwards; it ended at ',
    'Pumpe aus (geschätzt)': 'Pump off (estimated)',
    'Pumpe aus': 'pump off',
    'Nachlauf': 'Post-stop drip',
    'Pumpe aus bei ca. ': 'Pump off at about ',
    'in ': 'in ',
    '. Für ': '. For ',
    ' g in der Tasse bei ca. ': ' g in the cup, switch off at about ',
    ' g ausschalten. Je schneller der Shot läuft, desto mehr läuft nach.</p></div>': ' g. The faster the shot runs, the more drips through afterwards.</p></div>',
    ', beim geplanten Durchfluss etwa ': '; at the planned flow about ',
    'Waagenkurve': 'scale curve',
    'Spanne ': 'range ',
    ', ca. ': ', about ',
})
PHRASES += [
    ('<br>ausschalten bei ', '<br>switch off at '),
    ('<b>Ausschalten bei ', '<b>Switch off at '),
    (' g auf der Waage.</b> Nach dem Ausschalten laufen bei dir im Schnitt noch ', ' g on the scale.</b> After switching off, on average another '),
    (' g nach', ' g drips through'),
    ('<span class="eyebrow">Nachlauf deiner Maschine</span>', '<span class="eyebrow">Your machine’s post-stop drip</span>'),
    ('<p>Aus ', '<p>From '),
    ('<span class="muted">Gelernt aus ', '<span class="muted">Learned from '),
    ('<title>Pumpe aus</title>', '<title>Pump off</title>'),
]

EXACT.update({'Fertig': 'Done', 'Aus Notiz': 'From note', 'Geschmack bearbeiten': 'Edit taste', '+ Geschmack': '+ taste'})

EXACT.update({
    'salzig': 'salty', 'flach/leer': 'flat/hollow', 'trocken/pelzig': 'dry/astringent', 'verbrannt/aschig': 'burnt/ashy',
    'zu stark': 'too strong', 'süß': 'sweet', 'voller Körper': 'full body', 'schokoladig': 'chocolatey', 'nussig': 'nutty',
    'fruchtig': 'fruity', 'würzig': 'spicy', 'Fehler': 'Faults', 'Gelungen': 'Good', 'Aromen': 'Flavours',
    'Salzig': 'Salty', 'Flach': 'Flat',
    'Zu stark: eine längere Ratio verdünnt den Espresso, ohne die Extraktion zu verschlechtern.': 'Too strong: a longer ratio dilutes the espresso without hurting extraction.',
    'Verbrannt oder aschig: Die Temperatur ist für diese Röstung meist zu hoch. Kühler brühen hilft am schnellsten.': 'Burnt or ashy: the temperature is usually too high for this roast. Brewing cooler helps fastest.',
    'Trocken oder pelzig im Abgang entsteht oft durch Channeling oder zu viel Feinanteil. Puck-Vorbereitung prüfen; hilft das nicht, minimal gröber oder früher stoppen.': 'A dry or furry finish often comes from channeling or too many fines. Check puck prep; if that does not help, go slightly coarser or stop earlier.',
    'Flacher Geschmack passt zum Bohnenalter (': 'A flat taste fits the bean age (',
    ' Tage). Aromen bauen ab, mehr Extraktion hilft nur begrenzt.': ' days). Aromas fade; more extraction only helps so much.',
    'Salzig ist ein deutliches Zeichen für Unterextraktion: Der Shot braucht mehr Kontaktzeit.': 'Salty is a clear sign of under-extraction: the shot needs more contact time.',
    'sauer/flach Ø ': 'sour/flat avg ', 'gelungen Ø ': 'good avg ', 'bitter/trocken Ø ': 'bitter/dry avg ',
    'Gelungene Shots lagen bei ': 'Good shots ran ',
    ', Mahlgrad ': ', grind ',
    'Dein Sweet Spot liegt vermutlich dazwischen, bei etwa ': 'Your sweet spot is probably in between, at about ',
    '“ kam am deutlichsten bei Ø ': '” came through most at avg ',
    ' s und 1:': ' s and 1:',
})
PHRASES += [
    ('<span class="eyebrow">Geschmack nach Laufzeit</span>', '<span class="eyebrow">Taste by shot time</span>'),
    ('<span class="eyebrow">Aromen</span>', '<span class="eyebrow">Flavours</span>'),
    ('<p>„', '<p>“'),
]
EXACT.update({'„': '“'})

EXACT.update({' am ': ' on '})

EXACT.update({
    'zu stark': 'too strong', 'schwer · intensiv': 'heavy · intense', 'zu schwach': 'too weak', 'dünn · wässrig': 'thin · watery',
    'sauer · unterextrahiert': 'sour · under-extracted', 'bitter · überextrahiert': 'bitter · over-extracted',
    'Punkt ziehen, um den Geschmack einzuordnen.': 'Drag the point to place the taste.',
    'deutlich sauer': 'clearly sour', 'leicht sauer': 'slightly sour', 'deutlich bitter': 'clearly bitter', 'leicht bitter': 'slightly bitter',
    'deutlich zu stark': 'clearly too strong', 'etwas zu stark': 'a bit too strong', 'deutlich zu dünn': 'clearly too thin', 'etwas zu dünn': 'a bit too thin',
    'ausgewogen': 'balanced',
    'Im Kompass ausgewogen und der Shot ': 'Balanced on the compass and the shot ',
    '. Rezept halten.': '. Keep the recipe.',
    'Kompass: ': 'Compass: ',
    '. Mehr Extraktion nötig, Zielzeit ': '. More extraction needed, target time ',
    '. Weniger Extraktion nötig, Zielzeit ': '. Less extraction needed, target time ',
    '. Die Extraktion passt, nur die Stärke ändert sich.': '. Extraction is fine; only the strength changes.',
    'Eine längere Ratio macht ihn milder und extrahiert gleichzeitig mehr, das hilft doppelt.': 'A longer ratio makes it milder and extracts more at the same time, which helps twice.',
    'Zu stark: längere Ratio. Damit die Extraktion nicht kippt, wird die Zielzeit angepasst.': 'Too strong: longer ratio. The target time is adjusted so extraction does not tip over.',
    'Eine kürzere Ratio macht ihn kräftiger und nimmt gleichzeitig Bitterkeit weg.': 'A shorter ratio makes it stronger and removes bitterness at the same time.',
    'Zu schwach: kürzere Ratio. Damit er nicht sauer wird, läuft er dafür etwas länger.': 'Too weak: shorter ratio. To keep it from turning sour, it runs a little longer.',
    'Weil die Abweichung groß ist, zusätzlich 1 °C wärmer.': 'Because the deviation is large, also 1 °C hotter.',
    'Weil die Abweichung groß ist, zusätzlich 1 °C kühler.': 'Because the deviation is large, also 1 °C cooler.',
    'Alternative zur kürzeren Ratio: 0,5–1 g mehr Kaffeemehl bei gleicher Ratio. Dann muss die Mühle etwas gröber.': 'Alternative to a shorter ratio: 0.5–1 g more coffee at the same ratio. The grinder then needs to go a little coarser.',
    'Von dir gesetzt. Die Empfehlung rechnet mit diesem Punkt.': 'Set by you. The recommendation uses this point.',
    'Geschätzt aus den Geschmacksangaben. Punkt ziehen oder in die Fläche tippen, um ihn festzulegen.': 'Estimated from the taste tags. Drag the point or tap the area to set it.',
    '<button class="btn small" type="button" id="cmpReset" style="align-self:flex-start">Kompass zurücksetzen</button>': '<button class="btn small" type="button" id="cmpReset" style="align-self:flex-start">Reset compass</button>',
})
PHRASES += [
    ('aria-label="Dial-in-Kompass: Geschmack verschieben"', 'aria-label="Dial-in compass: move the taste"'),
    ('<span class="eyebrow">Dial-in-Kompass</span>', '<span class="eyebrow">Dial-in compass</span>'),
    ('Waagerecht: Extraktion. Senkrecht: Stärke. Ziel ist die Mitte. Graue Punkte zeigen deine letzten Shots.', 'Horizontal: extraction. Vertical: strength. Aim for the centre. Grey dots show your last shots.'),
]

EXACT.update({
    'Sauer trotz langer Laufzeit: Mehr Zeit allein hilft hier nicht. Wärmer brühen und die Puck-Vorbereitung prüfen (ungleichmäßiger Durchfluss lässt Teile des Pucks unterextrahiert).': 'Sour despite a long shot: more time alone will not help. Brew hotter and check puck prep (uneven flow leaves parts of the puck under-extracted).',
    'Bitter trotz kurzer Laufzeit deutet auf Channeling oder eine sehr dunkle Röstung. Kühler brühen und Puck-Vorbereitung prüfen.': 'Bitter despite a short shot points to channeling or a very dark roast. Brew cooler and check puck prep.',
    'Das Zeitfenster allein reicht nicht für die nötige Extraktion, deshalb zusätzlich ': 'The time window alone is not enough for the extraction needed, so also ',
    ' °C wärmer.': ' °C hotter.',
    'Das Zeitfenster allein reicht nicht, um die Extraktion zu senken, deshalb zusätzlich ': 'The time window alone is not enough to lower extraction, so also ',
    ' °C kühler.': ' °C cooler.',
})

EXACT.update({'wie zuletzt': 'same as last', '<span class="d">Mahlgrad nicht numerisch</span>': '<span class="d">Grind is not numeric</span>'})

EXACT.update({'besser als der vorherige Shot': 'better than the previous shot', 'schlechter als der vorherige Shot': 'worse than the previous shot',
  ' <span class="cmpkey better">grün</span> näher am Ziel als der vorherige Shot, <span class="cmpkey worse">rot</span> weiter weg.': ' <span class="cmpkey better">green</span> closer to target than the previous shot, <span class="cmpkey worse">red</span> further away.'})

EXACT.update({
  'Synchronisiere …': 'Syncing …', 'Konto': 'Account', 'Anmelden': 'Sign in', 'Registrieren': 'Sign up',
  'Konto anlegen': 'Create account', 'Schließen': 'Close', 'Neues Passwort': 'New password',
  'Fehler beim Abgleich: ': 'Sync error: ', 'Zuletzt abgeglichen ': 'Last synced ',
  'current-password': 'current-password', 'new-password': 'new-password',
  'Schon ein Konto? Anmelden': 'Already have an account? Sign in', 'Noch kein Konto? Registrieren': 'No account yet? Sign up',
  '<button class="linkbtn" type="button" id="acctMagic">Anmeldelink per E-Mail</button><button class="linkbtn" type="button" id="acctForgot">Passwort vergessen</button>': '<button class="linkbtn" type="button" id="acctMagic">Email me a sign-in link</button><button class="linkbtn" type="button" id="acctForgot">Forgot password</button>',
  'Bitte zuerst die E-Mail-Adresse eintragen.': 'Please enter your email address first.',
  'Anmeldelink gesendet. Öffne ihn auf diesem Gerät.': 'Sign-in link sent. Open it on this device.',
  'E-Mail zum Zurücksetzen gesendet.': 'Password reset email sent.',
  'Konto angelegt, du bist angemeldet.': 'Account created, you are signed in.',
  'Fast geschafft: Bitte bestätige die E-Mail, die wir dir geschickt haben.': 'Almost done: please confirm the email we sent you.',
  'E-Mail oder Passwort stimmt nicht.': 'Email or password is incorrect.',
  'Passwort gespeichert.': 'Password saved.', 'Abgemeldet.': 'Signed out.',
  'Alle Shots, Kurven, Rezepte und Einstellungen in diesem Browser und in deinem Konto löschen?': 'Delete all shots, curves, recipes and settings in this browser and in your account?',
})
PHRASES += [
  ('>Anmelden</button>', '>Sign in</button>'),
  ('<label for="aNewPw">Neues Passwort</label>', '<label for="aNewPw">New password</label>'),
  ('>Passwort speichern</button>', '>Save password</button>'),
  ('<p style="margin:0">Angemeldet als <b>', '<p style="margin:0">Signed in as <b>'),
  ('</b>. Shots, Waagenkurven, Rezepte und Einstellungen werden automatisch in deinem Konto gespeichert und auf allen Geräten abgeglichen.</p>', '</b>. Shots, scale curves, recipes and settings are saved to your account automatically and synced across all your devices.</p>'),
  ('>Jetzt abgleichen</button>', '>Sync now</button>'), ('>Abmelden</button>', '>Sign out</button>'),
  ('Beim Abmelden werden die Daten auf diesem Gerät entfernt, im Konto bleiben sie erhalten. Visualizer-Zugangsdaten bleiben immer nur auf dem Gerät.', 'Signing out removes the data from this device; it stays in your account. Visualizer credentials always stay on the device only.'),
  ('Mit einem Konto sind deine Shots auf iPad, Handy und Computer gleich. Ohne Konto bleibt alles nur in diesem Browser.', 'With an account your shots are the same on iPad, phone and computer. Without one, everything stays in this browser only.'),
  ('<label for="aEmail">E-Mail</label>', '<label for="aEmail">Email</label>'), ('<label for="aPw">Passwort</label>', '<label for="aPw">Password</label>'),
  ('<h2>Dein Konto</h2>', '<h2>Your account</h2>'),
]
PHRASES += [
  ('id="acctClose">Schließen</button>', 'id="acctClose">Close</button>'),
  ('<h2>Neues Passwort</h2>', '<h2>New password</h2>'),
]

EXACT.update({' · für diesen Shot 1:': ' · for this shot 1:', ' wegen des Geschmacks': ' because of the taste'})
PHRASES += [('<div class="targetline">Dein Ziel: <b>', '<div class="targetline">Your target: <b>')]

EXACT.update({' als die Ziel-Einstellung': ' than the target setting', 'Mahlgrad wie bei der Ziel-Einstellung': 'Same grind as the target setting',
  '<span class="muted" style="font-size:13px">Ausgehend von deinem Ziel: Mahlgrad ': '<span class="muted" style="font-size:13px">Starting from your target: grind ',
  ' g in ~': ' g in ~', ' s. Alle Optionen bleiben im Zeitfenster ': ' s. All options stay within the time window '})

PHRASES += [('">Rezept-Werkstatt</button>', '">Recipe workshop</button>'), ('id="goWs">Ziel ändern</button>', 'id="goWs">Change target</button>'),
  ('aria-label="Ansicht"', 'aria-label="View"')]

PHRASES += [('<span class="k">Erster Tropfen</span>', '<span class="k">First drip</span>'),
  ('Bohnenalter aus deinem Röstdatum · ', 'Bean age from your roast date · ')]
PHRASES += [('<span class="k">Bohnenalter</span>', '<span class="k">Bean age</span>')]

EXACT.update({'minimal sauer': 'barely sour', 'merklich sauer': 'noticeably sour', 'sehr sauer': 'very sour',
  'minimal bitter': 'barely bitter', 'merklich bitter': 'noticeably bitter', 'sehr bitter': 'very bitter',
  'minimal zu stark': 'barely too strong', 'merklich zu stark': 'noticeably too strong', 'viel zu stark': 'much too strong',
  'minimal zu dünn': 'barely too thin', 'merklich zu dünn': 'noticeably too thin', 'viel zu dünn': 'much too thin'})
EXACT.update({' · Stärke ': ' · Strength ', ' (Skala −10 bis +10)': ' (scale −10 to +10)'})

# Channeling-Check
EXACT.update({
  '). Erst die Puck-Vorbereitung verbessern, sonst sagt der Mahlgrad wenig aus. Details in der Shot-Analyse.': '). Fix the puck prep first, otherwise the grind setting tells you little. Details in the shot analysis.',
  'Leichte Channeling-Hinweise in der Kurve (Index ': 'Mild signs of channeling in the curve (index ',
  ' Flow-Sprünge (': ' flow spikes (',
  'Der Durchfluss steigt plötzlich um bis zu ': 'Flow suddenly rises by up to ',
  ' g/s innerhalb einer Sekunde. So sieht es aus, wenn sich im Puck ein Kanal öffnet.': ' g/s within one second. This is what it looks like when a channel opens in the puck.',
  'Der Durchfluss zittert in der Hauptphase stärker als üblich. Ein gleichmäßig durchströmter Puck liefert eine ruhige Kurve.': 'Flow wobbles more than usual in the main phase. An evenly saturated puck gives a calm curve.',
  'Früher Flow-Ausschlag (': 'Early flow surge (',
  'Kurz nach dem ersten Tropfen schießt der Flow weit über den späteren Durchschnitt. Das Wasser findet sofort einen bequemen Weg durch den Puck.': 'Right after the first drip, flow shoots far above its later average. The water immediately finds an easy path through the puck.',
  'Früher Ausschlag': 'Early surge',
  'Der Puck verliert gegen Ende Widerstand. Das ist oft Erosion oder ein Kanal, der sich langsam weitet.': 'The puck loses resistance towards the end. Often erosion or a channel that slowly widens.',
  'Der Druck fällt, während der Flow steigt: Der Widerstand im Puck bricht ein. Das ist das deutlichste Zeichen für einen Kanal.': 'Pressure drops while flow rises: puck resistance collapses. This is the clearest sign of a channel.',
  'Daten': 'Data',
  'Das Wasser ist sehr schnell durch. Bei ungleichmäßiger Verteilung findet es den kürzesten Weg.': 'Water came through very quickly. With uneven distribution it takes the shortest path.',
  'Etwas früh für eine Maschine ohne lange Preinfusion.': 'A bit early for a machine without long pre-infusion.',
  'Bei Mahlgrad ': 'At grind ',
  ' laufen deine anderen Shots im Mittel ': ' your other shots average ',
  ' g/s. Gleiche Mühle, gleiche Dosis, trotzdem weniger Widerstand: ein Hinweis auf einen Kanal.': ' g/s. Same grinder, same dose, yet less resistance: a hint of a channel.',
  'Sehr frische Bohne (': 'Very fresh beans (',
  ' Tage)': ' days)',
  'Viel CO₂ im Puck macht die Extraktion unruhiger und begünstigt Kanäle.': 'Lots of CO₂ in the puck makes extraction uneven and encourages channels.',
  'Sauer und bitter zugleich': 'Sour and bitter at once',
  'Klassisches Geschmacksbild von Channeling: Ein Teil des Kaffees wird überextrahiert (Kanal), der Rest bleibt unterextrahiert.': 'Classic channeling taste: part of the coffee is over-extracted (the channel), the rest stays under-extracted.',
  'Ein unruhiges, zerrissenes Geschmacksbild passt zu ungleichmäßiger Extraktion.': 'A choppy, disjointed taste fits uneven extraction.',
  'Adstringenz im Abgang entsteht häufig, wenn ein Teil des Pucks stark überextrahiert wird.': 'Astringency in the finish often comes from part of the puck being heavily over-extracted.',
  'Sauer trotz langer Laufzeit': 'Sour despite a long shot time',
  'Lange Kontaktzeit und trotzdem sauer: Das Wasser hat einen großen Teil des Pucks umgangen.': 'Long contact time and still sour: the water bypassed a large part of the puck.',
  'Dünn bei normaler Zeit': 'Thin at normal time',
  'Wenig Körper trotz passender Laufzeit kann auf einen Kanal hindeuten, durch den das Wasser vorbeifließt.': 'Little body despite a good shot time can point to a channel the water flows through.',
  'WDT gründlich bis zum Siebboden, besonders an den Rändern. Klumpen auflösen.': 'Thorough WDT down to the bottom of the basket, especially at the edges. Break up clumps.',
  'Gerade tampen (Level-Tamper oder Wasserwaage) und danach nicht mehr gegen den Siebträger klopfen.': 'Tamp level (levelling tamper or spirit level) and do not knock the portafilter afterwards.',
  'Sanfter starten: Preinfusion oder langsamer Druckaufbau, falls die Maschine das kann. Bleibt der erste Tropfen früh, etwas feiner mahlen.': 'Start gentler: pre-infusion or a slow pressure ramp if your machine can do it. If the first drip stays early, grind a little finer.',
  'Puck baut zum Ende ab: Dosis passend zur Siebgröße wählen (genug Mehl im Sieb) und eventuell etwas kürzer ziehen.': 'Puck breaks down at the end: match the dose to the basket size (enough coffee in it) and consider a slightly shorter shot.',
  'Ein Puck-Screen oben drauf verteilt das Wasser gleichmäßiger. Duschsieb und Siebe sauber und trocken halten.': 'A puck screen on top spreads the water more evenly. Keep shower screen and baskets clean and dry.',
  'Die Bohne ein paar Tage länger ruhen lassen.': 'Let the beans rest a few more days.',
  'Shot unter gleichen Bedingungen wiederholen. Läuft er wieder normal, war es die Vorbereitung und nicht der Mahlgrad.': 'Repeat the shot under the same conditions. If it runs normally again, it was the prep, not the grind.',
  'Erst die Vorbereitung stabil bekommen, dann weiter am Mahlgrad drehen. Sonst jagst du einem Zufallswert hinterher.': 'Get your prep consistent first, then keep adjusting the grind. Otherwise you are chasing a random result.',
  'möglich': 'possible',
  ' · mit Kurve': ' · with curve',
  'Grundlage: Waagenkurve, Shot-Daten und Geschmack': 'Based on: scale curve, shot data and taste',
  'Grundlage: nur Shot-Daten und Geschmack. Mit Waagenkurve wird die Aussage deutlich sicherer.': 'Based on shot data and taste only. With a scale curve the result is much more reliable.',
  'Die Kurve läuft ruhig und ohne Sprünge.': 'The curve is calm with no spikes.',
  'Lade die Waagenkurve dazu, um es genauer zu prüfen.': 'Add the scale curve to check it more precisely.',
})
PHRASES += [('aria-label="Channeling-Index der letzten Shots"', 'aria-label="Channeling index of recent shots"')]
PHRASES += [
  ("kind: 'Flow-Sprung'", "kind: 'Flow spike'"),
  ("kind: 'Druckeinbruch'", "kind: 'Pressure drop'"),
  (" g/s bei ${fmt(an.tPeak,0)} s)`", " g/s at ${fmt(an.tPeak,0)} s)`"),
  ("`Flow steigt zum Ende (+${", "`Flow rises towards the end (+${"),
  ("`Druckeinbruch bei ${", "`Pressure drop at ${"),
  ("`Schneller als sonst bei dieser Einstellung (+${", "`Faster than usual at this setting (+${"),
  ("const CH_LABEL = { low:'gering', mid:'möglich', high:'wahrscheinlich' }", "const CH_LABEL = { low:'unlikely', mid:'possible', high:'likely' }"),
  ('aria-label="Channeling-Index">', 'aria-label="Channeling index">'),
  ('margin-top:6px">Letzte Shots</span>', 'margin-top:6px">Recent shots</span>'),
  ('<h3 style="margin-top:14px">Was hilft</h3>', '<h3 style="margin-top:14px">What helps</h3>'),
  ("${x.pts} P.</span>", "${x.pts} pts</span>"),
  ('title="${fmtDate(h.x.date)} · Index ${h.c.score}', 'title="${fmtDate(h.x.date)} · index ${h.c.score}'),
  ("<span>Channeling <b>${CH_LABEL[ch.level]}</b></span>", "<span>Channeling <b>${CH_LABEL[ch.level]}</b></span>"),
  ("hints.unshift(`Channeling wahrscheinlich (Index ${", "hints.unshift(`Channeling likely (index ${"),
]
EXACT.update({
  'Channeling wahrscheinlich (Index ': 'Channeling likely (index ',
  '/100). Auf saubere Verteilung achten.': '/100). Pay attention to even distribution.',
  'Flow-Sprung': 'Flow spike', ' g/s bei ': ' g/s at ', 'Flow steigt zum Ende (+': 'Flow rises towards the end (+',
  'Druckeinbruch bei ': 'Pressure drop at ', 'Druckeinbruch': 'Pressure drop',
  'Schneller als sonst bei dieser Einstellung (+': 'Faster than usual at this setting (+', ' g/s, dieser ': ' g/s, this one ',
  'Unausgewogen': 'Unbalanced', 'Trocken oder pelzig': 'Dry or astringent',
  'gering': 'unlikely', 'wahrscheinlich': 'likely', ' · Index ': ' · index ', ' P.</span></span></li>': ' pts</span></span></li>',
  '<p class="muted" style="margin:0;font-size:14px">Keine Hinweise auf Channeling. ': '<p class="muted" style="margin:0;font-size:14px">No signs of channeling. ',
})
EXACT.update({'Details und Gegenmaßnahmen im Channeling-Check unten.': 'Details and fixes in the channeling check below.', ' (Index ': ' (index '})
PHRASES += [('C = Channeling-Hinweis', 'C = channeling sign')]
EXACT.update({
  ' (nicht gewertet)': ' (not counted)', 'extrem großer Sprung': 'extremely large jump', 'Gewicht springt zurück': 'weight jumps back',
  'Druck fällt um mehr als 3,5 bar, eher Profil oder Hebel': 'pressure drops by more than 3.5 bar, more likely a profile or lever',
  ' · <span class="muted">nicht gewertet': ' · <span class="muted">not counted',
  'Waagenkurve, Shot-Daten und Geschmack': 'scale curve, shot data and taste',
  'nur Shot-Daten und Geschmack, mit Waagenkurve deutlich sicherer': 'shot data and taste only, much more reliable with a scale curve',
  'Die markierten Ausreißer sind nicht gewertet.': 'The marked outliers are not counted.',
  '<span class="eyebrow">Markierungen in der Kurve</span>': '<span class="eyebrow">Marks in the curve</span>',
  'sofort wieder abgefallen': 'dropped straight back', 'Gewichtssprung': 'weight jump', 'extrem hoher Ausschlag': 'extremely high surge',
  ', vermutlich manuell': ', probably manual', 'doch werten': 'count it', 'ignorieren': 'ignore', 'letzte ': 'last ',
})
EXACT.update({' Shots</span></div>': ' shots</span></div>'})
EXACT.update({' bei ': ' at '})
EXACT.update({' · Ausreißer': ' · outlier'})
PHRASES += [('<span class="chcap">letzte ', '<span class="chcap">last ')]

# Röstgrad
EXACT.update({
  ' Röstung: ': ' roast: ', ' °C liegt unter dem üblichen Bereich von ': ' °C is below the usual range of ', ' °C, deshalb wärmer.': ' °C, so brew hotter.',
  ' °C liegt über dem üblichen Bereich von ': ' °C is above the usual range of ', ' °C, deshalb kühler.': ' °C, so brew cooler.',
  'Helle Röstungen lösen sich schwer. Die Temperatur ist hier der wirksamste Hebel, deshalb 1 °C wärmer.': 'Light roasts are hard to extract. Temperature is the most effective lever here, so 1 °C hotter.',
  'Dunkle Röstungen extrahieren leicht. Kühler brühen nimmt Bitterkeit am schnellsten heraus, deshalb 1 °C kühler.': 'Dark roasts extract easily. Brewing cooler removes bitterness fastest, so 1 °C cooler.',
  'Helle Röstung: eine längere Ratio (üblich 1:': 'Light roast: a longer ratio (typically 1:', ') bringt mehr Süße als nur mehr Zeit.': ') brings more sweetness than just more time.',
  'Dunkle Röstung: eine kürzere Ratio (üblich 1:': 'Dark roast: a shorter ratio (typically 1:', ') nimmt die bitteren letzten Gramm weg.': ') cuts the bitter last grams.',
  'Für eine ': 'For a ', ' Röstung sind Ratios von 1:': ' roast, ratios from 1:', ' bis 1:': ' to 1:', ' üblich. Dein Ziel 1:': ' are typical. Your target 1:',
  ' liegt ': ' is ', 'darunter': 'below', 'darüber': 'above', '. Das kann gewollt sein, ist aber ein möglicher Hebel.': '. That may be intended, but it is a possible lever.',
  'Sauer bei einer dunklen Röstung ist ungewöhnlich. Oft ist das Wasser zu kühl, der Shot läuft ungleichmäßig, oder die Bohne ist heller als gedacht.': 'Sour with a dark roast is unusual. Often the water is too cool, the shot runs unevenly, or the bean is lighter than assumed.',
  'Bitter bei einer hellen Röstung kommt meist von zu feinem Mahlgut (Feinanteil) oder Channeling, seltener von zu viel Extraktion.': 'Bitter with a light roast usually comes from too many fines or channeling, less often from too much extraction.',
  'hell': 'light', 'mittel-hell': 'medium-light', 'mittelhelle': 'medium-light', 'mittel-dunkel': 'medium-dark', 'mitteldunkle': 'medium-dark', 'dunkel': 'dark',
  'Löst sich schwer. Heiß brühen, längere Ratio, eher feiner und länger. Säure ist hier normal, Ziel ist sie süß einzubinden.': 'Hard to extract. Brew hot, longer ratio, finer and longer. Acidity is normal here, the goal is to make it sweet.',
  'Extrahiert leicht und wird schnell bitter. Kühler brühen, kürzere Ratio, eher gröber. Körper und Schokolade statt Säure.': 'Extracts easily and turns bitter quickly. Brew cooler, shorter ratio, coarser. Body and chocolate rather than acidity.',
  'Etwas wärmer und eine etwas längere Ratio holen Süße und Frucht heraus.': 'A bit hotter and a slightly longer ratio bring out sweetness and fruit.',
  'Klassischer Bereich. Kleine Schritte bei Temperatur und Ratio reichen meist.': 'Classic range. Small steps in temperature and ratio are usually enough.',
  'Eher kühler und kürzer. Bitterkeit kommt schnell, wenn der Shot zu lange läuft.': 'Rather cooler and shorter. Bitterness comes quickly if the shot runs too long.',
  ' Bei einer ': ' For a ', ' Röstung der wirksamste Hebel.': ' roast, the most effective lever.',
  'für ': 'for ', 'geschätzt aus den Bohnendaten, antippen zum Festlegen': 'estimated from the bean data, tap to set', 'antippen zum Festlegen': 'tap to set',
  ' Üblich: ': ' Typical: ',
})
PHRASES += [('<span class="k">Röstgrad</span>', '<span class="k">Roast level</span>'), ('aria-label="Röstgrad"', 'aria-label="Roast level"')]

# KI-Analyse
EXACT.update({
  'Du bist ein erfahrener Barista. Werte die folgenden Daten aus meiner Espresso-App gemeinsam aus: Muster über mehrere Shots, Röstgrad, Bohnenalter, Channeling, Geschmack. Gib einen konkreten nächsten Shot an (Mahlgrad in den Einheiten der Mühle, Dosis, Ausbeute, Zeit, Temperatur) und sag, ob du der Empfehlung der App zustimmst. Erfinde keine Daten. Antworte knapp, gegliedert in: Kurzfazit, Was die Daten zeigen, Nächster Shot, Danach, Datenlage.':
    'You are an experienced barista. Evaluate the following data from my espresso app as a whole: patterns across several shots, roast level, bean age, channeling, taste. Give a concrete next shot (grind in the grinder’s units, dose, yield, time, temperature) and say whether you agree with the app’s recommendation. Do not invent data. Answer concisely, structured as: Summary, What the data shows, Next shot, After that, Data quality.',
  ' · <b>seitdem gibt es einen neueren Ausgangs-Shot</b>': ' · <b>there is a newer base shot since then</b>',
  ' · heute noch ': ' · ', 'Analyse': 'analysis', 'Analysen': 'analyses', ' frei': ' left today',
  '. Auch der Butler kann danebenliegen, vergleiche mit der Empfehlung oben.</span>': '. The Butler can be wrong too, compare with the recommendation above.</span>',
  '<p class="muted" style="margin:0;font-size:14px">Der Butler ist deine KI für den Dial-in. Er liest deine Shots, die Waagenkurven, den Röstgrad und deine Geschmacksangaben gemeinsam und schreibt eine Einschätzung mit konkretem Vorschlag für den nächsten Shot. Er sieht auch die Empfehlung der App, sagt, ob er zustimmt, und prüft, ob die letzte Empfehlung gewirkt hat.</p>':
    '<p class="muted" style="margin:0;font-size:14px">The Butler is your AI for dialling in. He reads your shots, scale curves, roast level and taste notes together and writes an assessment with a concrete suggestion for the next shot. He also sees the app’s recommendation, says whether he agrees, and checks whether the last recommendation worked.</p>',
  'Analysiere …': 'Analysing …', 'Anmelden für den Butler': 'Sign in for the Butler', 'Neu analysieren': 'Analyse again', 'Analyse erstellen': 'Create analysis',
  '<button class="btn" type="button" id="aiDel">Analyse entfernen</button>': '<button class="btn" type="button" id="aiDel">Remove analysis</button>',
  '<span class="muted" style="font-size:12.5px">Die KI-Analyse in der App braucht ein Konto. Ohne Konto kannst du die Daten kopieren und selbst in Claude einfügen.</span>': '<span class="muted" style="font-size:12.5px">The in-app AI analysis needs an account. Without one you can copy the data and paste it into Claude yourself.</span>',
  'Der Butler ist noch nicht eingerichtet: Im Server fehlt der API-Schlüssel. Bis dahin funktioniert „Daten für Claude kopieren“.': 'The Butler is not set up yet: the server is missing its API key. Until then, “Copy data for Claude” works.',
  'Tageslimit erreicht (': 'Daily limit reached (', ' Analysen in 24 Stunden). Morgen geht es weiter.': ' analyses in 24 hours). Try again tomorrow.',
  'Die Anmeldung ist abgelaufen. Bitte neu anmelden.': 'Your session has expired. Please sign in again.',
  'Der Butler hat nicht geantwortet': 'The Butler did not respond', 'Die Analyse ist fehlgeschlagen': 'The analysis failed',
  'Keine Verbindung zum Server. Bitte später noch einmal versuchen.': 'No connection to the server. Please try again later.',
  'Kopiert. Jetzt in Claude einfügen.': 'Copied. Now paste it into Claude.', 'Kopieren:': 'Copy:',
})
PHRASES += [
  ('<h2 id="hAi">Butler</h2><span class="muted" style="font-size:13px">deine KI-Analyse: wertet alle Shots dieser Bohne zusammen aus: Mühle, Röstgrad, Kurven, Channeling und Geschmack</span>', '<h2 id="hAi">Butler</h2><span class="muted" style="font-size:13px">your AI analysis: evaluates all shots of this bean together: grinder, roast level, curves, channeling and taste</span>'),
  ('<span class="muted" style="font-size:12.5px">Erstellt am ', '<span class="muted" style="font-size:12.5px">Created '),
  ('title="Datenpaket und Anleitung in die Zwischenablage, zum Einfügen in Claude">Daten für Claude kopieren</button>', 'title="Data package and instructions to the clipboard, for pasting into Claude">Copy data for Claude</button>'),
]

# Eigener API-Schlüssel
EXACT.update({'Du bist der Butler des Dial-in Kompass: ein erfahrener Barista und Kaffee-Wissenschaftler. Du bekommst die Daten aus der App "Dial-in Kompass" als JSON: Bohne, Röstgrad, Bohnenalter, Mühle und deren Skala, Ziele (Dosis, Ratio, Zeitfenster), ein gelerntes Modell Durchfluss je Mahlgrad-Stufe, die letzten Shots (Mahlgrad, Dosis, Ausbeute, Zeit, erster Tropfen, Temperatur, Bewertung, Geschmack, Notizen, Dial-in-Kompass, Channeling-Index, Kennzahlen der Waagenkurve), den Vergleich des letzten Shots mit der Empfehlung, die für ihn galt, und die neue Empfehlung, die die App selbst berechnet hat.\n\nDeine Aufgabe: Werte alles gemeinsam aus und gib eine fundierte, ehrliche Einschätzung, wie der nächste Espresso besser wird.\n- Erkenne Muster über mehrere Shots (Trends, Widersprüche, Ausreißer), nicht nur den letzten Shot.\n- Beziehe Röstgrad, Bohnenalter, Channeling und Geschmack ein. Unterscheide, ob ein Problem an Extraktion, Stärke oder Puck-Vorbereitung liegt.\n- Gib einen konkreten nächsten Shot an: Mahlgrad in den Einheiten der Mühle, Dosis, Ausbeute, erwartete Zeit, Temperatur. Ändere möglichst nur einen oder zwei Hebel.\n- Sag, ob du der Empfehlung der App zustimmst. Wenn nicht, begründe kurz.\n- Erfinde keine Daten. Wenn etwas fehlt oder unsicher ist, sag es.\n- Antworte auf Deutsch, knapp und direkt, höchstens etwa 350 Wörter. Keine Tabellen, nur Überschriften, Absätze und Listen.\n\nGliederung (Markdown):\n## Kurzfazit\n## Was die Daten zeigen\n## Nächster Shot\n## Danach\n## Datenlage': 'You are the Butler of the Dial-in Kompass: an experienced barista and coffee scientist. You receive data from the "Dial-in Kompass" app as JSON: bean, roast level, bean age, grinder and its scale, targets (dose, ratio, time window), a learned model of flow per grind step, the recent shots (grind, dose, yield, time, first drip, temperature, rating, taste, notes, dial-in compass, channeling index, scale-curve metrics), the comparison of the last shot with the recommendation that applied to it, and the new recommendation the app computed itself.\n\nYour task: evaluate everything together and give a well-founded, honest assessment of how to make the next espresso better.\n- Look for patterns across several shots (trends, contradictions, outliers), not just the last shot.\n- Take roast level, bean age, channeling and taste into account. Distinguish whether a problem is about extraction, strength or puck prep.\n- Give a concrete next shot: grind in the grinder’s own units, dose, yield, expected time, temperature. Change only one or two levers if possible.\n- Say whether you agree with the app’s recommendation. If not, briefly explain why.\n- Do not invent data. If something is missing or uncertain, say so.\n- Answer in English, concise and direct, at most about 350 words. No tables, only headings, paragraphs and lists.\n\nStructure (Markdown):\n## Summary\n## What the data shows\n## Next shot\n## After that\n## Data quality', 'Sonnet 5.5 (empfohlen)': 'Sonnet 5.5 (recommended)', 'Opus 5.5 (gründlicher, teurer)': 'Opus 5.5 (more thorough, pricier)', 'Haiku 5.5 (schnell, günstig)': 'Haiku 5.5 (fast, cheap)', '<span class="muted" style="font-size:12.5px">Für den Butler in der App brauchst du ein Konto oder einen eigenen API-Schlüssel. Oder du kopierst die Daten und fügst sie selbst in Claude ein.</span>': '<span class="muted" style="font-size:12.5px">The in-app Butler needs an account or your own API key. Or copy the data and paste it into Claude yourself.</span>', 'Eigener API-Schlüssel aktiv <span class="num muted">(…': 'Own API key active <span class="num muted">(…', 'Eigenen API-Schlüssel verwenden': 'Use your own API key', 'neuen Schlüssel einfügen, um ihn zu ersetzen': 'paste a new key to replace it', '<button class="btn small" type="button" id="aiKeyDel">Schlüssel entfernen</button>': '<button class="btn small" type="button" id="aiKeyDel">Remove key</button>', 'Hier sind meine Daten:': 'Here is my data:', 'Anthropic lehnt den Schlüssel ab. Bitte prüfen, ob er stimmt und aktiv ist.': 'Anthropic rejects the key. Please check that it is correct and active.', 'Das gewählte Modell ist für deinen Schlüssel nicht verfügbar. Wähle ein anderes Modell.': 'The selected model is not available for your key. Choose another model.', 'Zu viele Anfragen oder Guthaben aufgebraucht. Bitte später erneut versuchen oder das Anthropic-Konto prüfen.': 'Too many requests or credit used up. Try again later or check your Anthropic account.', 'Claude ist gerade überlastet. Bitte in ein paar Minuten nochmal versuchen.': 'Claude is overloaded right now. Please try again in a few minutes.', 'Keine Verbindung zu Anthropic. Bitte später noch einmal versuchen.': 'No connection to Anthropic. Please try again later.', 'Bitte einen API-Schlüssel einfügen.': 'Please paste an API key.', 'Das sieht nicht nach einem Anthropic-Schlüssel aus (beginnt mit sk-ant-).': 'That does not look like an Anthropic key (starts with sk-ant-).'})
PHRASES += [('Mit eigenem Schlüssel von Anthropic geht die Anfrage direkt aus diesem Browser an Claude, ohne Umweg über den Server und ohne Tageslimit. Die Kosten laufen über dein Anthropic-Konto, meist ein paar Cent pro Analyse. Den Schlüssel erstellst du unter ', 'With your own Anthropic key the request goes straight from this browser to Claude, without the server and without a daily limit. Costs go to your Anthropic account, usually a few cents per analysis. Create a key at '), ('aria-label="API-Schlüssel"', 'aria-label="API key"'), ('aria-label="Modell"', 'aria-label="Model"'), ('id="aiKeySave">Speichern</button>', 'id="aiKeySave">Save</button>'), ('Der Schlüssel bleibt nur in diesem Browser auf diesem Gerät. Er wird nicht mit deinem Konto synchronisiert und nirgends sonst gespeichert. Auf einem geteilten Gerät besser nicht hinterlegen.', 'The key stays only in this browser on this device. It is not synced with your account and not stored anywhere else. Better not to save it on a shared device.')]

EXACT.update({'Haiku 5.5 (empfohlen, sehr günstig)': 'Haiku 5.5 (recommended, very cheap)', 'Sonnet 5.5 (gründlicher)': 'Sonnet 5.5 (more thorough)', 'Opus 5.5 (am gründlichsten, teurer)': 'Opus 5.5 (most thorough, pricier)'})

EXACT.update({'Der Butler hat keinen Text geliefert': 'The Butler returned no text', ', die Antwort war zu lang. Bitte nochmal versuchen.': ', the answer was too long. Please try again.', '. Bitte nochmal versuchen.': '. Please try again.'})

# KI-Assistent statt Claude, Spinner
EXACT.update({
  'Der Butler ist noch nicht eingerichtet: Im Server fehlt der API-Schlüssel. Bis dahin funktioniert „Daten für KI-Assistenten kopieren“.': 'The Butler is not set up yet: the server is missing its API key. Until then, “Copy data for AI assistant” works.',
  'Kopiert. Jetzt im KI-Assistenten einfügen.': 'Copied. Now paste it into your AI assistant.',
  '<span class="muted" style="font-size:12.5px">Für den Butler in der App brauchst du ein Konto oder einen eigenen API-Schlüssel. Oder du kopierst die Daten und fügst sie in einen KI-Assistenten deiner Wahl ein, zum Beispiel Claude oder ChatGPT.</span>': '<span class="muted" style="font-size:12.5px">The in-app Butler needs an account or your own API key. Or copy the data and paste it into an AI assistant of your choice, for example Claude or ChatGPT.</span>',
})
PHRASES += [
  ('<span>Der Butler liest deine Shots und schreibt seine Analyse. Das dauert meist 10–30 Sekunden.</span>', '<span>The Butler is reading your shots and writing his analysis. This usually takes 10–30 seconds.</span>'),
  ('title="Datenpaket und Anleitung in die Zwischenablage, zum Einfügen in Claude, ChatGPT, Gemini oder einen anderen KI-Assistenten">Daten für KI-Assistenten kopieren</button>', 'title="Data package and instructions to the clipboard, for pasting into Claude, ChatGPT, Gemini or another AI assistant">Copy data for AI assistant</button>'),
]
PHRASES += [('</span>Analysiere …', '</span>Analysing …')]
EXACT.update({'keine Bewertung': 'no rating', 'Bewertung bearbeiten': 'Edit rating', '+ Bewertung': '+ rating', 'Original': 'Original'})
EXACT.update({'hell / mittel-hell / mittel / mittel-dunkel / dunkel': 'light / medium-light / medium / medium-dark / dark'})

# Temperatur-Modus der Maschine
EXACT.update({
  'In 0,5-°C-Schritten': 'In 0.5 °C steps', 'In 1-°C-Schritten': 'In 1 °C steps', 'In Stufen (z. B. niedrig, mittel, hoch)': 'In levels (e.g. low, medium, high)', 'Gar nicht oder ohne Anzeige': 'Not at all or without a display',
  'eine Stufe': 'one level', 'eine Stufe wärmer': 'one level hotter', 'eine Stufe kühler': 'one level cooler', 'Stufe wie zuletzt': 'same level as last', '▲ wärmer': '▲ hotter', '▼ kühler': '▼ cooler',
  'Die Temperatur lässt sich an deiner Maschine nicht einstellen, deshalb übernimmt die Ratio den Rest.': 'Your machine has no adjustable temperature, so the ratio takes over the rest.',
  'Deine Maschine hat keine einstellbare Temperatur. Die Empfehlung arbeitet deshalb nur mit Mahlgrad, Ratio und Dosis. Kleiner Trick: Siebträger und Tasse gut vorheizen hilft bei sauren Shots, ein kurzer Leerbezug vor dem Shot kühlt bei bitteren.': 'Your machine has no adjustable temperature, so the recommendation works only with grind, ratio and dose. Small trick: preheating portafilter and cup well helps with sour shots, a short flush before the shot cools things down for bitter ones.',
  'an „': 'on “', 'an deiner Maschine': 'on your machine',
  '<div class="tile"><span class="k">Temp</span><span class="v">–</span><span class="d">an der Maschine nicht einstellbar</span></div>': '<div class="tile"><span class="k">Temp</span><span class="v">–</span><span class="d">not adjustable on the machine</span></div>',
  '<div class="muted" style="font-size:12.5px">Temperatur an der Maschine: ': '<div class="muted" style="font-size:12.5px">Machine temperature: ',
  ' · <button class="linkbtn" type="button" id="tmodeEdit">ändern</button></div>': ' · <button class="linkbtn" type="button" id="tmodeEdit">change</button></div>',
})
PHRASES += [
  ('<b id="tqTitle">Wie stellst du die Brühtemperatur ', '<b id="tqTitle">How do you set the brew temperature '),
  (' ein?</b>\n          <span class="muted" style="font-size:12.5px">Damit die Empfehlung nur Temperaturen vorschlägt, die du auch einstellen kannst.</span>', '?</b>\n          <span class="muted" style="font-size:12.5px">So the recommendation only suggests temperatures you can actually set.</span>'),
]
EXACT.update({'Nachwirkung eines Ausreißers': 'after-effect of an outlier'})

# Packung geöffnet
EXACT.update({
  'Die offene Packung läuft bei dir pro Tag etwa ': 'Your opened bag runs about ', ' g/s schneller (gelernt aus ': ' g/s faster per day (learned from ',
  ' Shots). Seit dem Ausgangs-Shot ': ' shots). Since the base shot ', 'ist rund ein Tag': 'about one day has', 'sind rund ': 'about ',
  ' vergangen, das ist eingerechnet.': ' passed, this is factored in.',
  'Die Packung ist seit ': 'The bag has been open for ', 'Tag': 'day', 'Tagen': 'days', ' offen, der Ausgangs-Shot ist ': ', the base shot is ',
  ' alt. Offene Bohnen verlieren CO₂ und laufen meist etwas schneller. Läuft der nächste Shot zu schnell, 0,1 feiner. Nach ein paar Shots lernt die App den Effekt selbst.': ' old. Opened beans lose CO₂ and usually run a little faster. If the next shot runs too fast, go 0.1 finer. After a few shots the app learns the effect itself.',
  'Packung noch zu': 'bag still sealed', 'Packung ': 'bag open ', ' T. offen': ' d', 'Packung offen': 'Bag open', 'zu': 'sealed',
  '<div class="openrow">Packung geöffnet am <b>': '<div class="openrow">Bag opened on <b>',
  'Ausgangs-Shot noch aus der verschlossenen Packung': 'base shot still from the sealed bag', 'beim Ausgangs-Shot ': 'at the base shot ', ' offen': ' open', ', heute ': ', today ',
  ' · <button class="linkbtn" type="button" id="openEdit">ändern</button></div>': ' · <button class="linkbtn" type="button" id="openEdit">change</button></div>',
  '<div class="openrow"><label for="openIn">Packung geöffnet am</label><input type="date" id="openIn" max="': '<div class="openrow"><label for="openIn">Bag opened on</label><input type="date" id="openIn" max="',
  '<button class="btn small" type="button" id="openDel">Entfernen</button>': '<button class="btn small" type="button" id="openDel">Remove</button>',
  '<span class="muted" style="font-size:12px">Ab dem Öffnen gast die Bohne schneller aus.</span></div>': '<span class="muted" style="font-size:12px">Once opened, the beans degas faster.</span></div>',
})
PHRASES += [('id="openToday">Heute</button>', 'id="openToday">Today</button>')]
EXACT.update({'Tage': 'days'})

EXACT.update({' <span class="muted">Die Kurve ist ruhig, deshalb nur halb gewertet.</span>': ' <span class="muted">The curve is calm, so this counts only half.</span>'})

# Systemprompt v2 (Abgleich mit der App)
EXACT.update({'Du bist der Butler des Dial-in Kompass: ein erfahrener Barista und Kaffee-Wissenschaftler. Du bekommst die Daten aus der App "Dial-in Kompass" als JSON: Bohne, Röstgrad, Bohnenalter, Öffnung der Packung, Mühle und deren Skala, Maschine, Ziele (Dosis, Ratio, Zeitfenster), das gelernte Modell der App (Durchfluss je Mahlgrad-Stufe und erwartete Zeiten je Mahlgrad), die letzten Shots (Mahlgrad, Dosis, Ausbeute, Zeit, erster Tropfen, Temperatur, Bewertung, Geschmack, Notizen, Dial-in-Kompass, Channeling-Index mit Belegen, Kennzahlen der Waagenkurve), den Vergleich des letzten Shots mit der Empfehlung, die für ihn galt, und die neue Empfehlung, die die App selbst berechnet hat.\n\nDeine Rolle: Du prüfst und ergänzt die App, du ersetzt sie nicht.\n- Die Zahlen der App sind die Grundlage: erwartete Zeiten je Mahlgrad, Channeling-Index samt Belegen, Kompass. Rechne sie nicht neu und widersprich ihnen nicht ohne konkreten Datenpunkt.\n- Die Empfehlung der App ist der Ausgangspunkt. Bestätige sie, wenn die Daten nicht klar dagegen sprechen. Weiche nur ab, wenn du einen konkreten Shot oder Wert als Beleg nennen kannst, und dann höchstens um eine Mahlgrad-Stufe oder bei einem einzigen Hebel.\n- Ergänze, was die App nicht sieht: Muster über mehrere Shots, Notizen, erster Shot des Tages, Packung frisch geöffnet, Widersprüche in den Angaben.\n- Channeling nur behaupten, wenn die Kurve es belegt. Hinweise nur aus Geschmack sind schwach.\n- Schlage nur Temperaturen vor, die die Maschine einstellen kann.\n- Erfinde keine Daten. Antworte auf Deutsch, knapp und direkt, höchstens etwa 350 Wörter. Keine Tabellen, nur Überschriften, Absätze und Listen.\n\nGliederung (Markdown):\n## Abgleich mit der App\n(ein bis zwei Sätze: zugestimmt oder angepasst, und warum)\n## Was die Daten zeigen\n## Nächster Shot\n## Danach\n## Datenlage\n\nSchließe mit genau einem JSON-Codeblock für die App, ohne weiteren Text danach:\n\\`\\`\\`json\n{"agree": true, "grind": "8,2", "dose": 18, "yield": 36, "timeSec": 23, "temp": "92 °C", "reason": "ein kurzer Satz"}\n\\`\\`\\`\n"agree" ist true, wenn dein nächster Shot der Empfehlung der App entspricht.': 'You are the Butler of the Dial-in Kompass: an experienced barista and coffee scientist. You receive data from the "Dial-in Kompass" app as JSON: bean, roast level, bean age, bag opening, grinder and its scale, machine, targets (dose, ratio, time window), the app’s learned model (flow per grind step and expected times per grind setting), the recent shots (grind, dose, yield, time, first drip, temperature, rating, taste, notes, dial-in compass, channeling index with evidence, scale-curve metrics), the comparison of the last shot with the recommendation that applied to it, and the new recommendation the app computed itself.\n\nYour role: you review and complement the app, you do not replace it.\n- The app’s numbers are the basis: expected times per grind setting, channeling index with its evidence, compass. Do not recompute them and do not contradict them without a concrete data point.\n- The app’s recommendation is the starting point. Confirm it unless the data clearly speaks against it. Deviate only if you can name a concrete shot or value as evidence, and then by at most one grind step or on a single lever.\n- Add what the app cannot see: patterns across several shots, notes, first shot of the day, freshly opened bag, contradictions in the inputs.\n- Only claim channeling if the curve shows it. Signs from taste alone are weak.\n- Only suggest temperatures the machine can actually set.\n- Do not invent data. Answer in English, concise and direct, at most about 350 words. No tables, only headings, paragraphs and lists.\n\nStructure (Markdown):\n## Check against the app\n(one or two sentences: agreed or adjusted, and why)\n## What the data shows\n## Next shot\n## After that\n## Data quality\n\nEnd with exactly one JSON code block for the app, with no text after it:\n\\`\\`\\`json\n{"agree": true, "grind": "8.2", "dose": 18, "yield": 36, "timeSec": 23, "temp": "92 °C", "reason": "one short sentence"}\n\\`\\`\\`\n"agree" is true if your next shot matches the app’s recommendation.'})
EXACT.update({'✓ Der Butler bestätigt die Empfehlung der App': '✓ The Butler confirms the app’s recommendation', '≠ Der Butler schlägt eine Anpassung vor': '≠ The Butler suggests an adjustment',
  '<button class="btn small" type="button" id="aiTake">Butler-Vorschlag ins Formular „Shot eintragen“</button>': '<button class="btn small" type="button" id="aiTake">Put Butler suggestion into “Log a shot”</button>',
  'Übernommen. Nach dem Shot Zeit und Geschmack ergänzen.': 'Done. After the shot, add time and taste.'})
PHRASES += [('<th>App</th><th>Butler</th>', '<th>App</th><th>Butler</th>')]

EXACT.update({'Den Vergleich findest du oben bei „Nächster Shot“.': 'You’ll find the comparison above under “Next shot”.', 'Zum nächsten Shot': 'To next shot', 'Zum Vergleich': 'To comparison'})
PHRASES += [('data-goto="hAi">Zum Butler</button>', 'data-goto="hAi">To the Butler</button>')]

EXACT.update({'✓ Der Butler bestätigt diese Empfehlung': '✓ The Butler confirms this recommendation'})
PHRASES += [('data-goto="hAi">Zum Butler</button></span></div>', 'data-goto="hAi">To the Butler</button></span></div>')]
PHRASES += [('<b>✓ Der Butler bestätigt diese Empfehlung</b>', '<b>✓ The Butler confirms this recommendation</b>')]
EXACT.update({
  'Die Ausbeute bleibt bei etwa 1:': 'The yield stays at about 1:', ' statt zurück auf dein Ziel 1:': ' instead of going back to your target 1:',
  'Weniger Ausbeute würde die Extraktion senken, der Shot war aber zu sauer.': 'Less yield would lower extraction, but the shot was too sour.',
  'Mehr Ausbeute würde die Extraktion erhöhen, der Shot war aber zu bitter.': 'More yield would raise extraction, but the shot was too bitter.',
  ' Immer nur einen Hebel pro Shot.': ' Only one lever per shot.',
  'Zu schwach: eine etwas kürzere Ratio macht ihn kräftiger.': 'Too weak: a slightly shorter ratio makes it stronger.',
  'Etwas dünn, aber auch sauer: eine kürzere Ratio würde die Extraktion senken. Deshalb bleibt die Ratio, mehr Körper kommt mit der höheren Extraktion.': 'A bit thin, but also sour: a shorter ratio would lower extraction. So the ratio stays; more body comes with the higher extraction.',
  'Für dein Zeitfenster müsste die Mühle gröber, das senkt aber die Extraktion und der Shot war sauer. Der Mahlgrad bleibt, die Zeit liegt dann bei etwa ': 'Your time window would need a coarser grind, but that lowers extraction and the shot was sour. The grind stays; the time will be about ',
  'Für dein Zeitfenster müsste die Mühle feiner, das erhöht aber die Extraktion und der Shot war bitter. Der Mahlgrad bleibt, die Zeit liegt dann bei etwa ': 'Your time window would need a finer grind, but that raises extraction and the shot was bitter. The grind stays; the time will be about ',
  ' s. Geschmack geht vor.': ' s. Taste comes first.',
})

EXACT.update({'. Mehr Extraktion nötig.': '. More extraction needed.', '. Weniger Extraktion nötig.': '. Less extraction needed.'})

# Systemprompt v3 (unabhängig, gemeinsame Regeln)
EXACT.update({'Du bist der Butler des Dial-in Kompass: ein erfahrener Barista und Kaffee-Wissenschaftler. Du bekommst die Daten aus der App "Dial-in Kompass" als JSON: Bohne, Röstgrad, Bohnenalter, Öffnung der Packung, Mühle und deren Skala, Maschine, Ziele (Dosis, Ratio, Zeitfenster), das gelernte Mühlenmodell der App (Durchfluss je Mahlgrad-Stufe und erwartete Zeiten je Mahlgrad), die letzten Shots (Mahlgrad, Dosis, Ausbeute, Zeit, erster Tropfen, Temperatur, Bewertung, Geschmack, Notizen, Dial-in-Kompass, Channeling-Index mit Belegen, Kennzahlen der Waagenkurve), den Vergleich des letzten Shots mit der Empfehlung, die für ihn galt, und die neue Empfehlung, die die App selbst berechnet hat.\n\nDeine Rolle: Du beurteilst die Daten unabhängig und kommst zu deinem eigenen Schluss. Du musst der App nicht zustimmen. Die Messwerte und das Mühlenmodell sind Daten, die Empfehlung der App ist nur eine Meinung.\n\nDie App arbeitet nach diesen Dial-in-Regeln. Wende sie ebenfalls an, damit eure Ergebnisse vergleichbar sind. Wenn du eine Regel im konkreten Fall für falsch hältst, sag es ausdrücklich:\n1. Geschmack vor Uhr: Bei sauer nie kürzer ziehen oder gröber mahlen, bei bitter nie länger ziehen oder feiner mahlen, auch wenn das Zeitfenster es verlangt.\n2. Möglichst ein Hebel pro Shot. Bei sauer zuerst feiner (solange die Zeit höchstens knapp über dem Fenster liegt), sonst wärmer oder etwas mehr Ausbeute. Bei bitter zuerst gröber, sonst kühler oder etwas weniger Ausbeute. Bei dunklen Röstungen ist die Temperatur oft der beste erste Hebel, bei hellen ebenfalls, nur in die andere Richtung.\n3. Zu dünn ohne Säure: kürzere Ratio oder 0,5–1 g mehr Dosis. Zu stark: längere Ratio. Ist der Shot gleichzeitig sauer, die Ratio nicht kürzen.\n4. Weicht die letzte Ausbeute vom Ziel ab, nicht gegen den Geschmack aufs Ziel zurückspringen.\n5. Channeling nur, wenn die Waagenkurve es zeigt. Dann zuerst die Puck-Vorbereitung verbessern, nicht den Mahlgrad.\n6. Der erste Shot des Tages und Shots am Tag des Öffnens der Packung sind weniger aussagekräftig. Nicht allein darauf nachjustieren.\n7. Nur Temperaturen vorschlagen, die die Maschine einstellen kann, und die übliche Spanne der Röstung beachten.\n\nWeitere Vorgaben:\n- Ergänze, was die App nicht sieht: Muster über mehrere Shots, Notizen, Widersprüche in den Angaben.\n- Erfinde keine Daten. Antworte auf Deutsch, knapp und direkt, höchstens etwa 350 Wörter. Keine Tabellen, nur Überschriften, Absätze und Listen.\n\nGliederung (Markdown):\n## Abgleich mit der App\n(ein bis zwei Sätze: gleicher Schluss oder anderer, und warum)\n## Letzter Shot vs. Empfehlung\n(zwei bis vier Sätze, aus lastShotVsRecommendation: Wurde die Empfehlung umgesetzt? Hat sie im Geschmack gewirkt? Stimmte die vorhergesagte Zeit, und was sagt eine Abweichung über das Mühlenmodell, die Bohne oder die Puck-Vorbereitung? Fehlt der Vergleich, schreib das in einem Satz.)\n## Was die Daten zeigen\n## Nächster Shot\n## Danach\n## Datenlage\n\nSchließe mit genau einem JSON-Codeblock für die App, ohne weiteren Text danach:\n\\`\\`\\`json\n{"agree": true, "grind": "8,2", "dose": 18, "yield": 36, "timeSec": 23, "temp": "92 °C", "reason": "ein kurzer Satz"}\n\\`\\`\\`\n"agree" ist true, wenn dein nächster Shot der Empfehlung der App entspricht.': 'You are the Butler of the Dial-in Kompass: an experienced barista and coffee scientist. You receive data from the "Dial-in Kompass" app as JSON: bean, roast level, bean age, bag opening, grinder and its scale, machine, targets (dose, ratio, time window), the app’s learned grinder model (flow per grind step and expected times per grind setting), the recent shots (grind, dose, yield, time, first drip, temperature, rating, taste, notes, dial-in compass, channeling index with evidence, scale-curve metrics), the comparison of the last shot with the recommendation that applied to it, and the new recommendation the app computed itself.\n\nYour role: you judge the data independently and reach your own conclusion. You do not have to agree with the app. The measurements and the grinder model are data; the app’s recommendation is just an opinion.\n\nThe app works by these dial-in rules. Apply them too so your results are comparable. If you think a rule is wrong in this specific case, say so explicitly:\n1. Taste before the clock: if sour, never pull shorter or grind coarser; if bitter, never pull longer or grind finer, even if the time window asks for it.\n2. One lever per shot where possible. If sour, first go finer (as long as the time stays at most just above the window), otherwise hotter or a little more yield. If bitter, first go coarser, otherwise cooler or a little less yield. For dark roasts temperature is often the best first lever, for light roasts too, just the other way.\n3. Too thin without sourness: shorter ratio or 0.5–1 g more dose. Too strong: longer ratio. If the shot is also sour, do not shorten the ratio.\n4. If the last yield differs from the target, do not jump back to the target against the taste.\n5. Channeling only if the scale curve shows it. Then improve puck prep first, not the grind.\n6. The first shot of the day and shots on the day the bag was opened are less meaningful. Do not adjust based on them alone.\n7. Only suggest temperatures the machine can actually set, and respect the usual range for the roast.\n\nFurther guidance:\n- Add what the app cannot see: patterns across several shots, notes, contradictions in the inputs.\n- Do not invent data. Answer in English, concise and direct, at most about 350 words. No tables, only headings, paragraphs and lists.\n\nStructure (Markdown):\n## Check against the app\n(one or two sentences: same conclusion or a different one, and why)\n## Last shot vs. recommendation\n(two to four sentences, from lastShotVsRecommendation: Was the recommendation followed? Did it work in the cup? Was the predicted time right, and what does a deviation say about the grinder model, the bean or puck prep? If the comparison is missing, say so in one sentence.)\n## What the data shows\n## Next shot\n## After that\n## Data quality\n\nEnd with exactly one JSON code block for the app, with no text after it:\n\\`\\`\\`json\n{"agree": true, "grind": "8.2", "dose": 18, "yield": 36, "timeSec": 23, "temp": "92 °C", "reason": "one short sentence"}\n\\`\\`\\`\n"agree" is true if your next shot matches the app’s recommendation.'})
PHRASES += [('<li>Geschmack vor Uhr: Bei sauer nie kürzer ziehen oder gröber mahlen, bei bitter nie länger ziehen oder feiner mahlen, auch wenn das Zeitfenster es verlangt.</li>', '<li>Taste before the clock: if sour, never pull shorter or grind coarser; if bitter, never pull longer or grind finer, even if the time window asks for it.</li>'), ('<li>Möglichst ein Hebel pro Shot. Bei sauer zuerst feiner (solange die Zeit höchstens knapp über dem Fenster liegt), sonst wärmer oder etwas mehr Ausbeute. Bei bitter zuerst gröber, sonst kühler oder etwas weniger Ausbeute. Bei dunklen Röstungen ist die Temperatur oft der beste erste Hebel, bei hellen ebenfalls, nur in die andere Richtung.</li>', '<li>One lever per shot where possible. If sour, first go finer (as long as the time stays at most just above the window), otherwise hotter or a little more yield. If bitter, first go coarser, otherwise cooler or a little less yield. For dark roasts temperature is often the best first lever, for light roasts too, just the other way.</li>'), ('<li>Zu dünn ohne Säure: kürzere Ratio oder 0,5–1 g mehr Dosis. Zu stark: längere Ratio. Ist der Shot gleichzeitig sauer, die Ratio nicht kürzen.</li>', '<li>Too thin without sourness: shorter ratio or 0.5–1 g more dose. Too strong: longer ratio. If the shot is also sour, do not shorten the ratio.</li>'), ('<li>Weicht die letzte Ausbeute vom Ziel ab, nicht gegen den Geschmack aufs Ziel zurückspringen.</li>', '<li>If the last yield differs from the target, do not jump back to the target against the taste.</li>'), ('<li>Channeling nur, wenn die Waagenkurve es zeigt. Dann zuerst die Puck-Vorbereitung verbessern, nicht den Mahlgrad.</li>', '<li>Channeling only if the scale curve shows it. Then improve puck prep first, not the grind.</li>'), ('<li>Der erste Shot des Tages und Shots am Tag des Öffnens der Packung sind weniger aussagekräftig. Nicht allein darauf nachjustieren.</li>', '<li>The first shot of the day and shots on the day the bag was opened are less meaningful. Do not adjust based on them alone.</li>'), ('<li>Nur Temperaturen vorschlagen, die die Maschine einstellen kann, und die übliche Spanne der Röstung beachten.</li>', '<li>Only suggest temperatures the machine can actually set, and respect the usual range for the roast.</li>'), ('<li><b>Dial-in-Regeln</b> (gelten für App und Butler):<ol class="rules">', '<li><b>Dial-in rules</b> (shared by app and Butler):<ol class="rules">')]
EXACT.update({
  'Bei einer hellen Röstung ist die Temperatur der wirksamste erste Hebel: 1 °C wärmer, Mahlgrad und Zeit bleiben.': 'With a light roast, temperature is the most effective first lever: 1 °C hotter, grind and time stay.',
  'Bei einer dunklen Röstung ist die Temperatur der wirksamste erste Hebel: 1 °C kühler, Mahlgrad und Zeit bleiben.': 'With a dark roast, temperature is the most effective first lever: 1 °C cooler, grind and time stay.',
  ' bei einer hellen Röstung: 1 °C wärmer ist hier der wirksamste Hebel. Mahlgrad und Ausbeute bleiben.': ' with a light roast: 1 °C hotter is the most effective lever here. Grind and yield stay.',
  ', obwohl die Zeit passt: etwas feiner, damit er länger läuft und mehr Süße zieht.': ' although the time fits: a little finer so it runs longer and pulls more sweetness.',
  ', und die Zeit ist schon am oberen Rand deines Fensters: 1 °C wärmer zieht mehr Extraktion, ohne die Zeit zu verlängern.': ', and the time is already at the top of your window: 1 °C hotter extracts more without lengthening the shot.',
  ', die Zeit ist am oberen Rand: etwas mehr Ausbeute (längere Ratio) zieht mehr Süße.': ', the time is at the top of the window: a little more yield (longer ratio) pulls more sweetness.',
  ' trotz langer Laufzeit: 1 °C wärmer statt noch länger. Oft ist das Wasser etwas zu kühl oder der Puck ungleichmäßig.': ' despite a long shot time: 1 °C hotter instead of even longer. Often the water is a bit too cool or the puck uneven.',
  ' trotz langer Laufzeit: etwas mehr Ausbeute statt noch länger.': ' despite a long shot time: a little more yield instead of even longer.',
  'Puck-Vorbereitung prüfen (WDT, gerade tampen).': 'Check puck prep (WDT, level tamp).',
  'Bitter bei einer dunklen Röstung: 1 °C kühler ist hier der wirksamste Hebel. Mahlgrad und Ausbeute bleiben.': 'Bitter with a dark roast: 1 °C cooler is the most effective lever here. Grind and yield stay.',
  'Bitter bei passender Zeit: etwas gröber, damit er kürzer läuft und weniger Bitterstoffe löst.': 'Bitter at a fitting time: a little coarser so it runs shorter and dissolves fewer bitter compounds.',
  'Bitter, und die Zeit ist schon am unteren Rand deines Fensters: 1 °C kühler senkt die Extraktion, ohne die Zeit zu verkürzen.': 'Bitter, and the time is already at the bottom of your window: 1 °C cooler lowers extraction without shortening the shot.',
  'Bitter, die Zeit ist am unteren Rand: Shot früher stoppen (kürzere Ratio).': 'Bitter, the time is at the bottom of the window: stop the shot earlier (shorter ratio).',
  'Der Ausgangs-Shot war der erste des Tages. Maschine und Mühle sind dann oft noch nicht ganz durchgewärmt, und altes Mahlgut aus der Mühle landet mit im Sieb. Er zählt im Modell deshalb nur halb, die Empfehlung bleibt vorsichtig.': 'The base shot was the first of the day. Machine and grinder are often not fully warmed up then, and old grounds from the grinder end up in the basket. It therefore counts only half in the model, and the recommendation stays cautious.',
})

# Einfach-Ansicht, Kurve lesen, KI annehmen
EXACT.update({
  'Butler-Vorschlag übernommen': 'Butler suggestion applied', '<span class="muted">App: ': '<span class="muted">App: ',
  '<div class="aicmp ok slim"><b>✓ Butler-Vorschlag übernommen</b><span>Die Werte oben stammen jetzt vom Butler. <button class="linkbtn" type="button" id="aiUndo">Zur App-Empfehlung zurück</button></span></div>': '<div class="aicmp ok slim"><b>✓ Butler suggestion applied</b><span>The values above now come from the Butler. <button class="linkbtn" type="button" id="aiUndo">Back to the app’s recommendation</button></span></div>',
  '<button class="btn small primary" type="button" id="aiTake">Butler-Vorschlag annehmen</button>': '<button class="btn small primary" type="button" id="aiTake">Accept Butler suggestion</button>',
  'Druck baut sich kaum auf (max. ': 'Pressure barely builds (max. ', 'Der Puck bremst zu wenig. Das ist ein deutlich zu grober Mahlgrad.': 'The puck gives too little resistance. The grind is clearly too coarse.',
  'Druck fällt zum Ende um ': 'Pressure drops towards the end by ',
  'Der Puck verliert hinten Widerstand. Meist ein Zeichen für einen leicht zu groben Mahlgrad. Hat es gut geschmeckt, kannst du so lassen.': 'The puck loses resistance at the end. Usually a sign of a slightly too coarse grind. If it tasted good, you can leave it.',
  'Treppenstufe im Druck (': 'Step in the pressure (',
  'Das ist eine Preinfusion mit niedrigem Druck. Kein Fehler, aber sie verlängert die Gesamtzeit. Achte darauf, dass sie bei allen Shots gleich eingestellt ist.': 'That is a low-pressure pre-infusion. Not a fault, but it lengthens the total time. Make sure it is set the same for all shots.',
  'Fluss stockt ': 'Flow stalls for ', ' s und schießt dann los': ' s and then shoots up',
  'Der Puck ist zu dicht und „erstickt“ erst, dann bricht das Wasser durch. Das gibt eine ungleichmäßige Extraktion. Etwas gröber mahlen.': 'The puck is too dense and “chokes” first, then the water breaks through. That gives uneven extraction. Grind a little coarser.',
  'Fluss bleibt sehr klein (Ø ': 'Flow stays very low (avg. ', 'Das Wasser kommt kaum durch den Puck. Das ist ein deutlich zu feiner Mahlgrad.': 'Water barely gets through the puck. The grind is clearly too fine.',
  'Fluss läuft schnell hoch (Ø ': 'Flow climbs fast (avg. ', 'Für dein Ziel wären etwa ': 'For your target about ', ' g/s passend. Der Puck bremst zu wenig, eher etwas feiner mahlen.': ' g/s would fit. The puck gives too little resistance, grind a little finer.',
  'Unruhige Kurve (Channeling-Index ': 'Unsteady curve (channeling index ',
  'Sprünge im Fluss deuten auf Kanäle im Puck. Zuerst die Vorbereitung verbessern: gleichmäßig verteilen, gerade tampen.': 'Jumps in the flow point to channels in the puck. Improve prep first: distribute evenly, tamp level.',
  'Saubere Kurve': 'Clean curve', 'Erst füllt sich der Puck, dann steigt der Fluss gleichmäßig an. Genau so soll es aussehen.': 'First the puck fills, then the flow rises steadily. That is exactly how it should look.',
  'Lecker': 'Tasty', 'Zu sauer': 'Too sour', 'Zu bitter': 'Too bitter', 'Zu dünn': 'Too thin', 'Zu stark': 'Too strong',
  'Der Mahlgrad passt.': 'The grind is right.', 'Deutlich zu grob.': 'Way too coarse.', 'Ein gutes Stück zu grob.': 'Quite a bit too coarse.', 'Etwas zu grob.': 'A little too coarse.',
  'Deutlich zu fein.': 'Way too fine.', 'Ein gutes Stück zu fein.': 'Quite a bit too fine.', 'Etwas zu fein.': 'A little too fine.',
  'Lass die Mühle so, wie sie ist.': 'Leave the grinder as it is.', 'Stell die Mühle ': 'Set the grinder ',
  'Du hast zuletzt von ': 'You last turned from ', ' gedreht und bist übers Ziel hinaus. Dreh nur etwa die Hälfte zurück.': ' and overshot. Turn back only about half way.',
  'Nach dem Verstellen ein paar Gramm durchmahlen, damit kein altes Mahlgut mehr in der Mühle ist.': 'After changing the setting, grind a few grams through so no old grounds remain in the grinder.',
  'Immer nur eine Sache ändern, dann probieren.': 'Change only one thing at a time, then taste.',
  'Die Zeit liegt etwas außerhalb deines Ziels. Weil der Geschmack wichtiger ist, bleibt der Mahlgrad.': 'The time is a little outside your target. Because taste matters more, the grind stays.',
  '<div class="aicmp ok slim"><b>✓ Butler-Vorschlag übernommen</b><span><button class="linkbtn" type="button" data-aiundo="1">Zur App-Empfehlung zurück</button></span></div>': '<div class="aicmp ok slim"><b>✓ Butler suggestion applied</b><span><button class="linkbtn" type="button" data-aiundo="1">Back to the app’s recommendation</button></span></div>',
  '✓ Der Butler sieht es genauso.': '✓ The Butler sees it the same way.', '≠ Der Butler schlägt etwas anderes vor:': '≠ The Butler suggests something else:', 'Mühle ': 'Grinder ',
  ' <button class="btn small primary" type="button" data-aiaccept="1">Annehmen</button>': ' <button class="btn small primary" type="button" data-aiaccept="1">Accept</button>',
  ' g rein → ': ' g in → ', ' g raus in ': ' g out in ',
  '<span class="sbtn own" aria-pressed="true"><b>Eigenes Rezept</b><span>aus der Rezept-Werkstatt</span></span>': '<span class="sbtn own" aria-pressed="true"><b>Own recipe</b><span>from the recipe workshop</span></span>',
  ' s bei ': ' s at ', ' g, Ziel ': ' g, target ', ' und Druck (gestrichelt)': ' and pressure (dashed)',
  '<span class="d">bei ': '<span class="d">stop at ', ' g ausschalten</span>': ' g</span>',
})
PHRASES += [
  ('<h2 id="hSimple">Was trinkst du?</h2><span class="muted" style="font-size:13px">Ziel: ', '<h2 id="hSimple">What are you drinking?</h2><span class="muted" style="font-size:13px">Target: '),
  ('<h2 id="hSLast">Dein letzter Shot</h2>', '<h2 id="hSLast">Your last shot</h2>'),
  ('<span class="k">Mühle</span>', '<span class="k">Grinder</span>'), ('<span class="k">Rein</span>', '<span class="k">In</span>'), ('<span class="k">Raus</span>', '<span class="k">Out</span>'),
  ('<h2 id="hSGrind">Mahlgrad</h2>', '<h2 id="hSGrind">Grind</h2>'),
  ('<h2 id="hSCurve">Was die Kurve sagt</h2><span class="muted" style="font-size:13px">Durchfluss', '<h2 id="hSCurve">What the curve says</h2><span class="muted" style="font-size:13px">Flow'),
  (' deines letzten Shots</span></div>', ' of your last shot</span></div>'),
  ('<h2 id="hSNext">So machst du den nächsten</h2>', '<h2 id="hSNext">How to pull the next one</h2>'),
  ('<h2 id="hSLog">Shot gezogen? Kurz eintragen</h2>', '<h2 id="hSLog">Pulled a shot? Log it quickly</h2>'),
  ('<label for="sGrind">Mühle</label>', '<label for="sGrind">Grinder</label>'), ('<label for="sDose">Rein g</label>', '<label for="sDose">In g</label>'), ('<label for="sYield">Raus g</label>', '<label for="sYield">Out g</label>'),
  ('<label for="sTime">Zeit s</label>', '<label for="sTime">Time s</label>'), ('placeholder="z. B. 27"', 'placeholder="e.g. 27"'),
  ('<button class="btn primary" type="submit">Speichern</button>\n    </form>', '<button class="btn primary" type="submit">Save</button>\n    </form>'),
  ('Danach oben angeben, wie er geschmeckt hat. Die App sagt dir dann, was du als Nächstes änderst.', 'Then tell it above how it tasted. The app will then tell you what to change next.'),
  ('aria-label="Mahlgrad-Feedback"', 'aria-label="Grind feedback"'), ('aria-label="Durchfluss-Kurve"', 'aria-label="Flow curve"'),
  ('fill="var(--bitter)">zu fein</text>', 'fill="var(--bitter)">too fine</text>'), ('fill="var(--good)">perfekt</text>', 'fill="var(--good)">perfect</text>'), ('fill="var(--sour)">zu grob</text>', 'fill="var(--sour)">too coarse</text>'),
  ('>Einfach</button>', '>Simple</button>'),
  ('Danach oben bei „Dein letzter Shot“ angeben, wie er geschmeckt hat. Die App sagt dir dann, was du als Nächstes änderst.', 'Then tell it under “Your last shot” above how it tasted. The app will then tell you what to change next.'),
  ('<label>Wie hat er geschmeckt? <span class="muted" style="font-weight:400">Mehrere möglich</span>', '<label>How did it taste? <span class="muted" style="font-weight:400">Pick several if needed</span>'),
  ('<span class="was">vorher ', '<span class="was">was '),
  ('Rot umrandet = ', 'Red outline = '), ('<summary>Genauer beschreiben</summary>', '<summary>Describe in more detail</summary>'), (', alles andere bleibt wie beim letzten Shot.', ', everything else stays as in the last shot.'),
  ('<p class="slegend">Alles bleibt wie beim letzten Shot.</p>', '<p class="slegend">Everything stays as in the last shot.</p>'),
]
EXACT.update({'Dünn und sauer zusammen ist typisch für Unterextraktion. Der Schritt gegen die Säure gibt auch mehr Körper, deshalb bleiben Dosis und Ratio.': 'Thin and sour together is typical of under-extraction. The step against the sourness also adds body, so dose and ratio stay.', 'Dünn bei zu kurzer Laufzeit ist typisch für Unterextraktion. Der Schritt zu mehr Extraktion gibt auch mehr Körper, deshalb bleiben Dosis und Ratio.': 'Thin with too short a run time is typical of under-extraction. The step towards more extraction also adds body, so dose and ratio stay.', 'diesen Wert ändern': 'change this value', 'diese Werte ändern': 'change these values'})
EXACT.update({'1:1,5 · 20–25 s': '1:1.5 · 20–25 s', '1:2,5 · 28–35 s': '1:2.5 · 28–35 s'})
EXACT.update({'Alle Geschmacksangaben': 'All taste notes', ' Dazu deine Korrektur von ': ' Plus your correction of ', ' Für ': ' For ',
  ' g ausschalten. Je schneller der Shot läuft, desto mehr läuft nach.</p>': ' g. The faster the shot runs, the more drips through afterwards.</p>',
  'Nach dem Ausschalten laufen bei dir im Schnitt noch ': 'After switching off, on average another ',
  'Mit deiner Korrektur rechnet die App beim geplanten Durchfluss mit ': 'With your correction the app expects at the planned flow ',
  '</b><button class="btn small" type="button" data-dripadj="0.5" aria-label="0,5 g mehr Nachlauf">+</button></span>': '</b><button class="btn small" type="button" data-dripadj="0.5" aria-label="0.5 g more post-stop drip">+</button></span>',
  '<span class="dripadj">Kommt bei dir mehr oder weniger nach? <button class="btn small" type="button" data-dripadj="-0.5" aria-label="0,5 g weniger Nachlauf">−</button><b class="num">': '<span class="dripadj">More or less drips through for you? <button class="btn small" type="button" data-dripadj="-0.5" aria-label="0.5 g less post-stop drip">−</button><b class="num">'})
PHRASES += [(' g Nachlauf. ', ' g post-stop drip. ')]
PHRASES += [(' g auf der Waage.</b> ', ' g on the scale.</b> ')]
EXACT.update({'Abweichend von der Empfehlung: ': 'Different from the recommendation: ', 'Du hast die Empfehlung umgesetzt.': 'You followed the recommendation.',
  'Die Zeit lag ': 'The time was ', 'über': 'above', 'unter': 'below', ' der Vorhersage, zum Teil wegen der anderen Werte.': ' the prediction, partly because of the other values.',
  'Der Shot lief ': 'The shot ran ', ' als vorhergesagt. Das Mühlenmodell lernt aus dieser Abweichung.': ' than predicted. The grinder model learns from this deviation.',
  'Die Zeit traf die Vorhersage.': 'The time matched the prediction.', 'Geschmack: ': 'Taste: ',
  ', näher an der Mitte als der Shot davor': ', closer to the centre than the shot before', ', weiter von der Mitte weg als der Shot davor': ', further from the centre than the shot before', ', etwa wie der Shot davor': ', about like the shot before',
  'Geschmack noch nicht angegeben. Trag ihn beim Ausgangs-Shot ein, dann sieht die App, ob die Empfehlung geholfen hat.': 'Taste not entered yet. Add it at the base shot, then the app can tell whether the recommendation helped.',
  ' (Butler-Vorschlag übernommen)': ' (Butler suggestion accepted)', 'Empfehlung nachträglich berechnet, mit dem Datenstand vor diesem Shot': 'Recommendation calculated afterwards, using the data from before this shot',
  ' · Basis: Shot vom ': ' · Based on the shot from ', 'Empfehlung, wie sie vor dem Shot angezeigt wurde': 'Recommendation as shown before the shot',
  'wie empfohlen': 'as recommended', 'wie erwartet': 'as expected', 'langsamer': 'slower', 'schneller': 'faster', 'ca. ': 'approx. '})
PHRASES += [('<h2 id="hRecVs">Letzter Shot vs. Empfehlung</h2>', '<h2 id="hRecVs">Last shot vs. recommendation</h2>'),
  ('<th></th><th>Empfohlen</th><th>Gezogen</th><th>Abweichung</th>', '<th></th><th>Recommended</th><th>Pulled</th><th>Difference</th>'),
  ('<br><span class="muted">ausschalten bei ', '<br><span class="muted">switch off at ')]
EXACT.update({' der Vorhersage. Das passt zu den abweichenden Werten.': ' the prediction. That fits the values that differed.',
  ' als vorhergesagt, obwohl die abweichenden Werte ihn eher ': ' than predicted, although the values that differed should have made it ',
  ' gemacht hätten. Das Mühlenmodell lernt aus dieser Abweichung.': '. The grinder model learns from this deviation.'})
EXACT.update({'In der letzten Analyse fehlt dieser Vergleich. Lass den Butler neu analysieren.': 'This comparison is missing from the last analysis. Let the Butler analyse again.',
  'Der Butler vergleicht das in seiner nächsten Analyse ebenfalls.': 'The Butler will compare this in his next analysis too.'})
