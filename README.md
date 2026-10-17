# Punktestand

Mobiler **Punktezähler** für Würfelspiele (nur Summen pro Runde, kein Spielablauf).

- URL (nach Deploy): `https://spielzeug-gefunden.github.io/Gamedemo/`
- Dateien: [`index.html`](./index.html), [`styles.css`](./styles.css), [`names.js`](./names.js)
- Lizenz: [MIT](./LICENSE)

## Funktionen

- **2–8 Spieler**, Session per Cookie auf dem Gerät
- Leere Namen werden mit Fantasienamen aus [`names.js`](./names.js) gefüllt
- „Neues Spiel“ behält die letzten Spielernamen
- Rundenpunkte direkt in die hervorgehobene Tabellenzelle
- Ab **6000** Punkten Gewinnanzeige mit Konfetti; **OK** führt zurück zum Spiel (weiter/korrigieren möglich)
- Aktionstasten links vom Nummernfeld: Rückgängig, **±1000** (Abzug für Führende, eigene ↓-Zeile; aktueller Spieler ausgenommen; Summe nie unter 0), Drehen, Neues Spiel
- Menü: Ansicht drehen, Vollbild, Zum Homebildschirm

## GitHub Pages

- [`.nojekyll`](./.nojekyll) deaktiviert die Jekyll-Verarbeitung.
- Workflow [`.github/workflows/pages.yml`](./.github/workflows/pages.yml) deployt bei Push auf `main`.

In **Settings → Pages** als **Source** den Eintrag **GitHub Actions** wählen.
