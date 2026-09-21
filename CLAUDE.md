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

Ein Manual liegt immer als Ordner mit vier Sprachdateien vor:

```
<bereich>/<slug>/
├── <slug>_EN.md
├── <slug>_DE.md
├── <slug>_FR.md
└── <slug>_ES.md
```

Bereiche mit nur einem Manual (z. B. `region-duel/`, `minigames/`) enthalten die vier Dateien direkt.

## Regeln

1. **Vier Sprachen, immer synchron.** Jedes Manual existiert als EN, DE, FR, ES. Wird eine Fassung geändert, werden alle vier angepasst — keine inhaltlichen Abweichungen zwischen den Sprachen.
2. **Namenskonvention:** `<slug>_<SPRACHCODE>.md`, Slug in Kleinbuchstaben mit Bindestrich (`world-boss`, `alliance-duel`).
3. **Einsortieren nach Spiel-UI.** Ein neues Manual kommt in den Bereich, über dessen Button oder Gebäude man das Thema im Spiel erreicht. Passt nichts, wird ein neuer Top-Level-Bereich mit dem Namen des UI-Elements angelegt.
   Ausnahme: Inhalte ohne UI-Entsprechung (z. B. aus anderen Spielen übertragene Strategien) gehören nach `strategy/` und müssen **als unverifiziert gekennzeichnet** sein.
4. **README aktuell halten.** Neues Manual → neue Zeile in der Tabelle des passenden Bereichs mit Kurz-Info und vier Sprachlinks im Format
   `https://github.com/MatzUp2022/GTs/blob/main/<bereich>/<slug>/<slug>_<CODE>.md`
5. **Stil:** knapp, tabellarisch, keine Fülltexte. Konkrete Zahlen und Punktwerte statt allgemeiner Tipps. Zielumfang pro Manual: eine Bildschirmseite.
6. **Aufbau eines Manuals:** Grundregeln → Ressourcen-/Versuchsökonomie → empfohlener Ablauf (Tabelle) → Kopplung an übergeordnete Events (SvS etc.) → Checkliste zum Abhaken.
7. **Spielmechaniken nicht erfinden.** Werte, Boni und Punktzahlen nur übernehmen, wenn sie vom Nutzer genannt oder belegt sind. Unklares markieren statt schätzen.

## Typische Aufgaben

- Neues Manual anlegen (alle vier Sprachen + README-Zeile im passenden Bereich)
- Bestehendes Manual nach Balance-Änderung aktualisieren (alle vier Sprachen)
- Sprachfassungen auf Abweichungen prüfen
- Helden-Datenbank (`hero/hero-db/`) um weitere Helden ergänzen
