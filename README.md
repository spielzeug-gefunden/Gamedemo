# Punktestand

Mobiler **Punktezähler** für Würfelspiele (u. a. Tutto): Rundenpunkte, Vormerken, Niete und Plus/Minus (±1000).

- URL (nach Deploy): `https://spielzeug-gefunden.github.io/Gamedemo/`
- Dateien: [`index.html`](./index.html), [`styles.css`](./styles.css), [`names.js`](./names.js)
- Lizenz: [MIT](./LICENSE)

## Lokal testen

Voraussetzung: **Python 3** (kein npm/pip).

```bash
python start-server.py
```

Unter Windows Doppelklick auf [`start-server.bat`](./start-server.bat), unter Linux/Mac [`start-server.sh`](./start-server.sh). Der Browser öffnet `http://localhost:4173`. Beenden mit `Ctrl+C`.

## Funktionen

- **2–8 Spieler**, Session per Cookie auf dem Gerät
- Leere Namen werden mit Fantasienamen aus [`names.js`](./names.js) gefüllt
- „Neues Spiel“ behält die Namen und rotiert die Reihenfolge (bisheriger 2. wird 1. usw.); Reihenfolge im Setup per Ziehen am ⠿-Griff änderbar
- Vollbild nur manuell über das Menü (kein Auto-Vollbild beim Start)
- Rundenpunkte direkt in die hervorgehobene Tabellenzelle
- Keypad links: **Neues Spiel**, **±** (Tutto: +1000 für den aktuellen Spieler, −1000 für andere Führende, Zugwechsel; Summe nie unter 0), **Niete** (0), **+** (Vormerken/aufaddieren)
- Ab **6000** Punkten Gewinnanzeige mit Konfetti; **OK** führt zurück zum Spiel (weiter/korrigieren möglich)
- Menü: Ansicht drehen, Vollbild, Zum Homebildschirm, Letzten Eintrag löschen, Neues Spiel

## GitHub Pages

- [`.nojekyll`](./.nojekyll) deaktiviert die Jekyll-Verarbeitung.
- Workflow [`.github/workflows/pages.yml`](./.github/workflows/pages.yml) deployt bei Push auf `main`.

In **Settings → Pages** als **Source** den Eintrag **GitHub Actions** wählen.
