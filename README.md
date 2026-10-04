# Gamedemo

Kleine Web-Apps rund um Würfelspiele – rein statisch, ohne Build-Schritt.

Lizenz: [MIT](./LICENSE)

## Apps

### Punktestand

Mobiler **Punktezähler** für zwei Spieler (nur Summen pro Runde, kein Spielablauf).

- URL (nach Deploy): `https://spielzeug-gefunden.github.io/Gamedemo/punkte/`
- Lokal: [`punkte/index.html`](./punkte/index.html)
- Session wird per **Cookie** auf dem Gerät gespeichert (Namen, Rundenpunkte, aktiver Spieler).
- Layout: Menü oben, Punktetabelle (obere Hälfte, aktiver Name hervorgehoben), Ziffernblock 0–9 + OK (untere Hälfte).
- Tippen auf einen Tabellenwert erlaubt Korrekturen.
- Menüoption **Ansicht drehen**: bei Spieler 2 wird die Ansicht um 180° gedreht (gegenüber sitzen).

### Würfelspiel (Demo)

Einfaches Würfelspiel (Variante von „Pig“) im Repository-Root.

- URL: `https://spielzeug-gefunden.github.io/Gamedemo/`
- Datei: [`index.html`](./index.html)

## GitHub Pages

- [`.nojekyll`](./.nojekyll) deaktiviert die Jekyll-Verarbeitung.
- Workflow [`.github/workflows/pages.yml`](./.github/workflows/pages.yml) deployt bei jedem Push auf `main`.

In **Settings → Pages** als **Source** den Eintrag **GitHub Actions** wählen.
