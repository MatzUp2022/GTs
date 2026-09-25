# CLAUDE.md — Arbeitsanweisungen für dieses Repo

## Zweck

Sammlung kurzer Best-Practise-Manuals für das Spiel *Last Light*, gepflegt für die Allianz **GTs**.
Zielgruppe: Mitspieler, die den Text direkt in Alliance-Chat oder Discord kopieren.

Repo: https://github.com/MatzUp2022/GTs

## Struktur

Die Ordner **spiegeln die Spiel-Oberfläche**: Jedes Top-Level-Verzeichnis entspricht einem Button
bzw. Bereich im Spiel, darunter liegt ein Ordner je Manual.

```
GTs/
├── README.md        # Übersicht, gegliedert wie die Spiel-Navigation
├── CLAUDE.md        # diese Datei
├── events/          # Button „Events" (rechte Leiste)
├── region-duel/     # Button „Region Duel" (SvS)
├── trial/           # Button „Trial" (untere Leiste)
├── hero/            # Button „Hero" (untere Leiste)
├── alliance/        # Button „Alliance" (untere Leiste)
├── minigames/       # Button „Leave None" (untere Leiste)
├── base/            # Basis & Gebäude (Radar, Tavern, Vehicle)
│   └── research/    # Research Lab: ein Ordner je Forschungsbaum
├── account/         # Profil · Shop · VIP · Hilfe
└── strategy/        # kein UI-Element: Wochenplan, übertragene Strategien
    ├── weekly-plan/        # tages- und uhrzeitgenauer Plan über alle Events
    └── last-war-transfer/  # aus verwandten Spielen übertragen, unverifiziert
```

Ein Manual liegt immer als Ordner mit acht Sprachdateien vor:

```
<bereich>/<slug>/
├── <slug>_EN.md   ├── <slug>_NL.md
├── <slug>_DE.md   ├── <slug>_RU.md
├── <slug>_FR.md   ├── <slug>_JP.md
└── <slug>_ES.md   └── <slug>_CN.md
```

Bereiche mit nur einem Manual (z. B. `region-duel/`, `minigames/`) enthalten die acht Dateien direkt.

## Regeln

1. **Acht Sprachen, immer synchron.** Jedes Manual existiert als EN, DE, FR, ES, NL, RU, JP, CN. Wird eine Fassung geändert, werden alle acht angepasst — keine inhaltlichen Abweichungen zwischen den Sprachen.
   Spiel-UI-Begriffe (Event-, Skill-, Helden- und Gebäudenamen) bleiben in allen Sprachen englisch, weil der Client englisch ist. Übersetzt wird der erklärende Text, nicht das, was im Spiel auf dem Button steht.
   Prüfen mit `python3 tools/check-languages.py` — vergleicht Vollständigkeit, Struktur (Überschriften, Tabellenzeilen, Checkboxen) und alle Zahlenwerte über die acht Fassungen. Zahlen werden vorher normalisiert, `25,000` / `25.000` / `25 000` gelten als derselbe Wert. Exit-Code ≠ 0 bei Abweichung.
   **Zahlen als Ziffer schreiben, nicht als Wort** — „1×/Tag", nicht „einmal täglich". Sonst meldet die Prüfung Unterschiede, die keine sind.
2. **Namenskonvention:** `<slug>_<SPRACHCODE>.md`, Slug in Kleinbuchstaben mit Bindestrich (`world-boss`, `alliance-duel`). Sprachcodes: EN, DE, FR, ES, NL, RU, JP, CN (JP/CN statt ISO ja/zh — so vom Nutzer festgelegt; CN = vereinfachtes Chinesisch).
3. **Einsortieren nach Spiel-UI.** Ein neues Manual kommt in den Bereich, über dessen Button oder Gebäude man das Thema im Spiel erreicht. Passt nichts, wird ein neuer Top-Level-Bereich mit dem Namen des UI-Elements angelegt.
   Ausnahme: Inhalte ohne UI-Entsprechung (z. B. aus anderen Spielen übertragene Strategien) gehören nach `strategy/` und müssen **als unverifiziert gekennzeichnet** sein.
4. **README aktuell halten.** Neues Manual → neue Zeile in der Tabelle des passenden Bereichs mit Kurz-Info und acht Sprachlinks im Format
   `https://github.com/MatzUp2022/GTs/blob/main/<bereich>/<slug>/<slug>_<CODE>.md`
5. **Stil:** knapp, tabellarisch, keine Fülltexte. Konkrete Zahlen und Punktwerte statt allgemeiner Tipps. Zielumfang pro Manual: eine Bildschirmseite.
6. **Aufbau eines Manuals:** Grundregeln → Ressourcen-/Versuchsökonomie → empfohlener Ablauf (Tabelle) → Kopplung an übergeordnete Events (SvS etc.) → Checkliste zum Abhaken.
7. **Spielmechaniken nicht erfinden.** Werte, Boni und Punktzahlen nur übernehmen, wenn sie vom Nutzer genannt oder belegt sind. Unklares markieren statt schätzen.
8. **Lizenz.** Der Text des Repos steht unter **CC BY 4.0** (`LICENSE`). Neue Inhalte werden unter derselben Lizenz beigesteuert.
   Die Lizenz deckt **unseren Text**, nicht das Spiel: Name, Grafiken, Oberfläche und Inhalte von *Last Light* gehören ihren Eigentümern — hier wird nur darüber berichtet. Das Repo ist ein inoffizielles Fan-Projekt. Keine Spiel-Assets (Screenshots, Artwork, Icons) ins Repo einchecken.

## Typische Aufgaben

- Neues Manual anlegen (alle acht Sprachen + README-Zeile im passenden Bereich)
- Bestehendes Manual nach Balance-Änderung aktualisieren (alle acht Sprachen)
- Sprachfassungen auf Abweichungen prüfen (`python3 tools/check-languages.py`, mit `-v` auch die einstelligen JP/CN-Notizen)
- Helden-Datenbank (`hero/hero-db/`) um weitere Helden ergänzen
