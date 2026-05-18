# Berlin Weather Pipeline

![Tests](https://github.com/muhannadnajjar1-hash/berlin-weather-pipeline/actions/workflows/tests.yml/badge.svg)

Ein Data-Engineering-Portfolio-Projekt, das Wetterdaten für Berlin über eine öffentliche API abruft, verarbeitet, validiert und lokal speichert.

Die Pipeline verwendet die Open-Meteo API, lädt stündliche Wetterdaten als JSON, transformiert sie in eine tabellarische Struktur und speichert die verarbeiteten Daten als CSV, Parquet und SQLite-Datenbank.

## Projektziel

Dieses Projekt zeigt zentrale Fähigkeiten im Bereich Data Engineering:

- API-Datenaufnahme
- JSON-Verarbeitung
- Datenbereinigung und Transformation
- Konfigurationsgesteuerte Pipeline-Ausführung
- Datenvalidierung
- Speicherung als CSV, Parquet und SQLite
- Unit Testing
- Ruff Linting
- GitHub Actions / CI
- Git/GitHub-Projektorganisation

## Datensatz / API

Das Projekt verwendet die Open-Meteo API für Wetterdaten.

Für diese Version werden stündliche Wetterdaten für Berlin verarbeitet:

```text
Latitude: 52.52
Longitude: 13.41
Timezone: Europe/Berlin
