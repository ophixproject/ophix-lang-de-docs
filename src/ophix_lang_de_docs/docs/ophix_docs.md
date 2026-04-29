---
title: Dokumentationssystem
slug: ophix-docs
order: 500
section: Erweiterungen
---

`ophix-docs` ist ein optionales Plugin, das der Django-Administration Inline-Dokumentation hinzufügt. Jede installierte App kann eigene Markdown-Dokumentation liefern; ein Verwaltungsbefehl importiert alles in die Datenbank, wo sie in der Administrationsoberfläche mit Syntaxhervorhebung angezeigt wird.

---

## Installation

```bash
pip install ophix-docs
ophix-manage migrate
```

Nach der Installation und Migration erscheint ein Abschnitt **Dokumentation** in der Administration.

---

## Dokumentation importieren

Der Befehl `ophix_docs_update` importiert Markdown-Dateien in die Datenbank:

```bash
ophix-manage ophix_docs_update
```

Standardmäßig liest er aus dem in `OPHIX_DOCS_PATH` gesetzten Pfad (Standard: ein `docs/`-Ordner neben dem Projektstamm). Um auch Docs aus installierten Apps zu importieren:

```bash
# Auf einem Anmeldeinformationsserver:
ophix-manage ophix_docs_update \
  --include-app-docs ophix.core,ophix_creds,ophix_docs,ophix_theme_tools
```

`ophix_docs_update` ist **nur additiv** — er erstellt und aktualisiert Seiten, löscht sie aber nie. Zum Entfernen von Seiten verwenden Sie `ophix_docs_purge`.

---

## Dokumentation entfernen

### Bestimmte Seiten nach Slug löschen

```bash
ophix-manage ophix_docs_purge mein-slug
```

### Alle Seiten löschen

```bash
ophix-manage ophix_docs_purge --all
```

### Seiten löschen, deren Quelldateien entfernt wurden

```bash
ophix-manage ophix_docs_purge --deleted
```

Alle Modi unterstützen `--dry-run`:

```bash
ophix-manage ophix_docs_purge --deleted --dry-run
```

---

## Markdown-Dateiformat

Jede Dokumentationsseite ist eine `.md`-Datei mit einem YAML-Front-Matter-Block:

```text
---
title: Mein Seitentitel
slug: mein-slug
order: 10
section: Mein Abschnitt
---

## Mein erster Abschnitt

Inhalt kommt hierher...
```

### Front-Matter-Felder

| Feld | Erforderlich | Beschreibung |
| --- | --- | --- |
| `title` | Ja | Anzeigename in der Administrations-Navigation |
| `slug` | Ja | Eindeutige Kennung — muss über alle importierten Docs eindeutig sein |
| `order` | Ja | Sortierposition innerhalb des Abschnitts |
| `section` | Ja | Abschnittsname, zu dem diese Seite gehört |

---

## Abschnitte

Abschnitte gruppieren zusammengehörige Seiten in der Navigation. Jede App, die Docs liefert, sollte auch eine `sections.yaml`-Datei einschließen:

```yaml
sections:
  - name: Mein Abschnitt
    collapsed: false
```

---

## Operator-eigene Dokumentation

Operatoren können eigene Dokumentationsseiten hinzufügen. Den Pfad in `.env` konfigurieren:

```ini
OPHIX_DOCS_PATH=/home/websites/credserver/docs
```

---

## Dokumentation exportieren

```bash
ophix-manage ophix_docs_export mein-slug --output ./docs/
```

---

## Quellen auflisten

```bash
ophix-manage ophix_docs_list_sources
```

---

## Einstellungen

| Einstellung | Standard | Beschreibung |
| --- | --- | --- |
| `OPHIX_DOCS_ENABLED` | `true` | Auf `false` setzen, um den Dokumentationsabschnitt in der Administration zu verbergen |
| `OPHIX_DOCS_PATH` | `BASE_DIR/docs` | Pfad zum primären Docs-Ordner |
| `OPHIX_DOCS_APP_LABEL` | `Documentation` | Label des Admin-Abschnitts |
