# Punktestand

Mobiler **Punktezähler** für Würfelspiele (nur Summen pro Runde, kein Spielablauf).

- URL (nach Deploy): `https://spielzeug-gefunden.github.io/Gamedemo/`
- Datei: [`index.html`](./index.html)
- Lizenz: [MIT](./LICENSE)

## Funktionen

- **2–8 Spieler**, Session per Cookie auf dem Gerät
- Glass-UI mit durchscheinenden Flächen und Linienhintergrund
- Rundenpunkte direkt in die hervorgehobene Tabellenzelle
- Menü: Ansicht drehen, Vollbild, Zum Homebildschirm, Neues Spiel

## GitHub Pages

- [`.nojekyll`](./.nojekyll) deaktiviert die Jekyll-Verarbeitung.
- Workflow [`.github/workflows/pages.yml`](./.github/workflows/pages.yml) deployt bei Push auf `main`.

In **Settings → Pages** als **Source** den Eintrag **GitHub Actions** wählen.
