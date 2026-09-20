# CLAUDE.md — Arbeitsanweisungen für dieses Repo

## Zweck

Sammlung kurzer Best-Practise-Manuals für das Spiel *Last Light*, gepflegt für die Allianz **GTs**.
Zielgruppe: Mitspieler, die den Text direkt in Alliance-Chat oder Discord kopieren.

Repo: https://github.com/MatzUp2022/GTs

## Struktur

```
GTs/
├── README.md                    # Übersicht + Links auf alle Manuals
├── CLAUDE.md                    # diese Datei
└── events/
    └── <event-slug>/
        ├── <event-slug>_EN.md
        ├── <event-slug>_DE.md
        ├── <event-slug>_FR.md
        └── <event-slug>_ES.md
```

## Regeln

1. **Vier Sprachen, immer synchron.** Jedes Manual existiert als EN, DE, FR, ES. Wird eine Fassung geändert, werden alle vier angepasst — keine inhaltlichen Abweichungen zwischen den Sprachen.
2. **Namenskonvention:** `<event-slug>_<SPRACHCODE>.md`, Slug in Kleinbuchstaben mit Bindestrich (`world-boss`, `alliance-duel`).
3. **README aktuell halten.** Neues Manual → neue Zeile in der Event-Tabelle mit vier Sprachlinks im Format
   `https://github.com/MatzUp2022/GTs/blob/main/events/<slug>/<slug>_<CODE>.md`
4. **Stil:** knapp, tabellarisch, keine Fülltexte. Konkrete Zahlen und Punktwerte statt allgemeiner Tipps. Zielumfang pro Manual: eine Bildschirmseite.
5. **Aufbau eines Manuals:** Grundregeln → Ressourcen-/Versuchsökonomie → empfohlener Ablauf (Tabelle) → Kopplung an übergeordnete Events (SvS etc.) → Checkliste zum Abhaken.
6. **Spielmechaniken nicht erfinden.** Werte, Boni und Punktzahlen nur übernehmen, wenn sie vom Nutzer genannt oder belegt sind. Unklares markieren statt schätzen.

## Typische Aufgaben

- Neues Event-Manual anlegen (alle vier Sprachen + README-Zeile)
- Bestehendes Manual nach Balance-Änderung aktualisieren (alle vier Sprachen)
- Sprachfassungen auf Abweichungen prüfen
