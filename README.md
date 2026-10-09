# Dial-in Kompass

Web-App für das Espresso-Dial-in auf Basis von Beanconqueror-Daten. Läuft komplett im Browser, ohne Server und ohne Build-Schritt auf Vercel.

## Funktionen

- Import: Beanconqueror-Excel-Export, vollständiges Backup (ZIP), Flowprofile einzelner Bezüge (JSON/Excel), Visualizer-Dateien
- Cloud-Sync über visualizer.coffee (Beanconqueror lädt Bezüge automatisch dort hoch)
- Empfehlung für den nächsten Shot: Mahlgrad, Dosis, Ausbeute, Zeit, Temperatur
- Shot-Analyse: erster Tropfen, Durchfluss der Hauptphase, Waagenkurve, Channeling-Hinweise, Vergleich
- Rezept-Werkstatt: Geschmacksziele, Was-wäre-wenn-Rechner (z. B. 17 statt 18 g), Mühlen-Kalibrierung
- Rezepte pro Bohne und Mühle, gelernter Nachlauf, Pflege-Zähler

Alle Daten bleiben im Browser (localStorage). Zugangsdaten für den Cloud-Sync gehen nur direkt an visualizer.coffee.

## Aufbau

| Pfad | Zweck |
|---|---|
| `index.html` | Die ausgelieferte App (wird von Vercel direkt serviert) |
| `src/template.html` | Quelltext der App |
| `src/sample.json` | Beispieldaten, die beim ersten Öffnen geladen werden |
| `tools/build.py` | Baut `index.html` (und `dist/claude-artifact.html`) aus `src/` |

Nach Änderungen in `src/`:

```bash
python3 tools/build.py
```

Danach `index.html` committen. Vercel deployt jeden Push auf `main` automatisch.
