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
- Einfache Visualisierung aus verarbeiteten Daten

## Datensatz / API

Das Projekt verwendet die Open-Meteo API für Wetterdaten.

Für diese Version werden stündliche Wetterdaten für Berlin verarbeitet:

```text
Latitude: 52.52
Longitude: 13.41
Timezone: Europe/Berlin
```

Abgerufene Variablen:

```text
temperature_2m
precipitation
wind_speed_10m
```

Die Rohdaten werden als JSON gespeichert:

```text
data/raw/weather_raw.json
```

Der Ordner `data/` wird von Git ignoriert und lokal erzeugt.

## Projektstruktur

```text
berlin-weather-pipeline/
├── config/
│   └── config.yaml
├── data/
│   ├── raw/
│   └── processed/
├── reports/
│   └── weather_temperature_trend.png
├── src/
│   ├── __init__.py
│   ├── ingest.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── visualize.py
│   └── main.py
├── tests/
│   ├── test_transform.py
│   ├── test_validate.py
│   └── test_load.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Pipeline

```text
Open-Meteo API
      ↓
Ingest
      ↓
Raw JSON
      ↓
Transform
      ↓
Validate
      ↓
Load
      ↓
CSV / Parquet / SQLite
```

### Ingest

`src/ingest.py` lädt die Konfiguration, ruft die Open-Meteo API ab und speichert die rohe JSON-Antwort lokal.

### Transform

`src/transform.py` wandelt die verschachtelte JSON-Struktur in einen tabellarischen DataFrame um.

Die transformierten Daten enthalten unter anderem:

```text
timestamp
temperature_2m
precipitation
wind_speed_10m
```

### Validate

`src/validate.py` prüft die transformierten Wetterdaten vor dem Speichern.

Die Validierung prüft unter anderem:

- Der Datensatz ist nicht leer
- Alle erforderlichen Spalten sind vorhanden
- `timestamp` enthält keine fehlenden Werte
- `temperature_2m` ist nicht vollständig leer
- `precipitation` enthält keine negativen Werte
- `wind_speed_10m` enthält keine negativen Werte

### Load

`src/load.py` speichert die validierten Daten als:

```text
data/processed/weather_hourly.csv
data/processed/weather_hourly.parquet
data/processed/berlin_weather.db
```

### Visualize

`src/visualize.py` erzeugt aus den verarbeiteten Daten eine einfache Grafik für die README-Datei.

Der aktuelle Chart wird hier gespeichert:

```text
reports/weather_temperature_trend.png
```

## Konfiguration

Die Pipeline-Einstellungen werden in folgender Datei gespeichert:

```text
config/config.yaml
```

Beispiel:

```yaml
api:
  base_url: "https://api.open-meteo.com/v1/forecast"
  latitude: 52.52
  longitude: 13.41
  timezone: "Europe/Berlin"
  hourly_variables:
    - temperature_2m
    - precipitation
    - wind_speed_10m

output:
  raw_json_path: "data/raw/weather_raw.json"
  processed_csv_path: "data/processed/weather_hourly.csv"
  processed_parquet_path: "data/processed/weather_hourly.parquet"
  sqlite_path: "data/processed/berlin_weather.db"
  table_name: "weather_hourly"

logging:
  level: "INFO"
```

## Lokale Ausführung

Repository klonen:

```bash
git clone https://github.com/muhannadnajjar1-hash/berlin-weather-pipeline.git
cd berlin-weather-pipeline
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

Pipeline ausführen:

```bash
python src/main.py
```

Erwarteter Output:

```text
data/raw/weather_raw.json
data/processed/weather_hourly.csv
data/processed/weather_hourly.parquet
data/processed/berlin_weather.db
```

Visualisierung erzeugen:

```bash
python src/visualize.py
```

Erwarteter Output:

```text
reports/weather_temperature_trend.png
```

## Visualisierung

Die folgende Grafik zeigt den stündlichen Temperaturverlauf für Berlin aus den verarbeiteten API-Daten.

![Stündlicher Temperaturverlauf Berlin](reports/weather_temperature_trend.png)

## Tests und Linting

Tests ausführen:

```bash
pytest
```

Ruff Linting ausführen:

```bash
ruff check src tests
```

Die Tests prüfen unter anderem:

- JSON-Wetterdaten werden korrekt in einen DataFrame transformiert
- Fehlende API-Strukturen werden erkannt
- Gültige Wetterdaten bestehen die Validierung
- Ungültige Wetterdaten schlagen bei der Validierung fehl
- SQLite-Export erstellt eine abfragbare Tabelle

## Continuous Integration

Dieses Projekt verwendet GitHub Actions, um Ruff Linting und Unit Tests automatisch bei jedem Push und Pull Request auf den `main`-Branch auszuführen.

Der Workflow ist definiert in:

```text
.github/workflows/tests.yml
```

Der Workflow führt aus:

```bash
ruff check src tests
pytest
```

## Aktuelle Ergebnisse

Ein erfolgreicher Pipeline-Lauf erzeugt aktuell stündliche Wetterdaten für Berlin.

Der letzte lokale Testlauf erzeugte:

```text
168 stündliche Datensätze
```

Die verarbeiteten Daten enthalten folgende Spalten:

```text
timestamp, temperature_2m, precipitation, wind_speed_10m
```

## Designentscheidungen

- Die Pipeline verwendet eine öffentliche API statt einer lokalen Excel-Datei, um dynamische Datenquellen zu demonstrieren.
- Die rohe JSON-Antwort wird gespeichert, damit der ursprüngliche API-Response nachvollziehbar bleibt.
- Die Transformationslogik ist getrennt von Ingestion, Validierung und Speicherung.
- Die Daten werden als CSV, Parquet und SQLite gespeichert, um verschiedene Analyse- und Speicherformate zu zeigen.
- Die Visualisierung wird aus den verarbeiteten Daten erzeugt und nicht manuell erstellt.
- Die aktuelle Version bleibt lokal und kostenfrei.
- GitHub Actions stellt sicher, dass Tests und Linting automatisch ausgeführt werden.

## Nächste Schritte

Geplante Erweiterungen:

- Geplante tägliche Ausführung mit GitHub Actions
- Inkrementelles Laden historischer Wetterdaten
- Visualisierung von Niederschlag und Windgeschwindigkeit
- Spätere Verbindung mit dem Berlin Mobility Pipeline Projekt
