# Gamedemo

Ein kleines Würfelspiel (Variante von „Pig") als reine statische Webseite.

## Spielen

Öffne die [`index.html`](./index.html) direkt im Browser – es sind keine
Abhängigkeiten oder Build-Schritte nötig.

### Spielregeln

- Du spielst gegen den Computer. Wer zuerst **50 Punkte** erreicht, gewinnt.
- Beim **Würfeln** werden die Augen zu deinen Rundenpunkten addiert.
- Mit **Halten** sicherst du die Rundenpunkte deinem Gesamtkonto und übergibst.
- Würfelst du eine **1**, verfallen die Rundenpunkte und der Gegner ist dran.

## GitHub Pages

Das Projekt ist für GitHub Pages vorbereitet:

- [`index.html`](./index.html) liegt im Repository-Root.
- [`.nojekyll`](./.nojekyll) deaktiviert die Jekyll-Verarbeitung.
- Der Workflow [`.github/workflows/pages.yml`](./.github/workflows/pages.yml)
  deployt die Seite automatisch bei jedem Push auf `main`.

### Einmalige Aktivierung

In den Repository-Einstellungen unter **Settings → Pages** als
**Source** den Eintrag **GitHub Actions** auswählen. Danach wird die Seite
bei jedem Push auf `main` automatisch veröffentlicht.
