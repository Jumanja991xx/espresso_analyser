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
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Dial-in">
<link rel="manifest" href="{'/en/manifest.webmanifest' if lang == 'en' else '/manifest.webmanifest'}">
<link rel="apple-touch-icon" href="/icons/icon-180.png">
<link rel="alternate" hreflang="de" href="/">
<link rel="alternate" hreflang="en" href="/en/">
<link rel="icon" type="image/svg+xml" href="/icons/icon.svg">
<link rel="icon" type="image/png" sizes="192x192" href="/icons/icon-192.png">
{redirect}
{head}<style>html{{color-scheme:light}}:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}@media (prefers-color-scheme: dark){{html{{color-scheme:dark}}}}</style>
</head>
<body>
{body}
<script>if('serviceWorker' in navigator && location.protocol === 'https:') navigator.serviceWorker.register('/sw.js').catch(function(){{}});</script>
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

# Syntaxprüfung der eingebetteten Skripte (falls Node vorhanden)
import shutil, subprocess
if shutil.which('node'):
    chk = "const fs=require('fs');let bad=0;for(const f of ['index.html','en/index.html','dist/claude-artifact.html']){const h=fs.readFileSync(f,'utf8');for(const m of h.matchAll(/<script>([\\s\\S]*?)<\\/script>/g)){try{new Function(m[1])}catch(e){bad=1;console.log('SYNTAXFEHLER',f,e.message)}}}process.exit(bad)"
    r = subprocess.run(['node', '-e', chk])
    if r.returncode: sys.exit('Build enthält Syntaxfehler')
