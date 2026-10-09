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
| `index.html` | Die App auf Deutsch (Vercel, `/`) |
| `en/index.html` | Die App auf Englisch (Vercel, `/en/`) |
| `src/template.html` | Quelltext der App |
| `src/sample.json`, `src/sample_en.json` | Erfundene Beispieldaten für „Mit Beispieldaten ausprobieren“ |
| `tools/i18n.py`, `tools/i18n_en.py` | Übersetzung ins Englische beim Build |
| `tools/build.py` | Baut beide Sprachversionen (und `dist/claude-artifact.html`) aus `src/` |

Nach Änderungen in `src/`:

```bash
python3 tools/build.py
```

Der Build meldet Textstellen ohne englische Übersetzung; neue Texte in `tools/i18n_en.py` ergänzen. Danach `index.html` und `en/index.html` committen. Vercel deployt jeden Push auf `main` automatisch.
