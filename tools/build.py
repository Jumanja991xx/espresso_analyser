import os, pathlib
root=pathlib.Path(__file__).resolve().parent.parent
os.chdir(root)
os.makedirs('dist',exist_ok=True)
t=open('src/template.html').read(); s=open('src/sample.json').read()
page=t.replace('__SAMPLE__',s)
open('dist/claude-artifact.html','w').write(page)
i=page.index('<div class="wrap">')
head,body=page[:i],page[i:]

open('index.html','w').write('''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Dial-in Kompass: Beanconqueror-Export laden, Shots analysieren, nächsten Espresso berechnen.">
<meta name="theme-color" content="#17675F">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Dial-in">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='14' fill='%2317675F'/%3E%3Cpath d='M16 6 L19 16 L16 26 L13 16Z' fill='white'/%3E%3C/svg%3E">
'''+head+'''<style>html{color-scheme:light}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}@media (prefers-color-scheme: dark){html{color-scheme:dark}}</style>
</head>
<body>
'''+body+'''
</body>
</html>
''')
