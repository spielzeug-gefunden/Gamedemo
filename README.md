# Gamedemo

Kleine Web-Apps rund um Würfelspiele – rein statisch, ohne Build-Schritt.

Lizenz: [MIT](./LICENSE)

## Apps

### Punktestand

Mobiler **Punktezähler** für **2–8 Spieler** (nur Summen pro Runde, kein Spielablauf).

- URL (nach Deploy): `https://spielzeug-gefunden.github.io/Gamedemo/punkte/`
- Lokal: [`punkte/index.html`](./punkte/index.html)
- Session wird per **Cookie** auf dem Gerät gespeichert (Namen, Rundenpunkte, aktiver Spieler).
- Glass-UI mit durchscheinenden Flächen und Linienhintergrund.
- Layout: Menü oben, Punktetabelle (obere Hälfte, aktiver Name hervorgehoben), Ziffernblock 0–9 + OK (untere Hälfte).
- Tippen auf einen Tabellenwert erlaubt Korrekturen.
- Menüoption **Ansicht drehen**: gegenüber sitzende Spieler (2, 4, …) sehen die Ansicht um 180° gedreht.

### Würfelspiel (Demo)

Einfaches Würfelspiel (Variante von „Pig“) im Repository-Root.

- URL: `https://spielzeug-gefunden.github.io/Gamedemo/`
- Datei: [`index.html`](./index.html)

## GitHub Pages

- [`.nojekyll`](./.nojekyll) deaktiviert die Jekyll-Verarbeitung.
- Workflow [`.github/workflows/pages.yml`](./.github/workflows/pages.yml) deployt bei jedem Push auf `main`.

In **Settings → Pages** als **Source** den Eintrag **GitHub Actions** wählen.
