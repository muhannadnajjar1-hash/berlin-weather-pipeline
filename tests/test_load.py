import sqlite3

import pandas as pd

from src.load import save_to_sqlite


def test_save_to_sqlite_creates_table(tmp_path):
    df = pd.DataFrame(
        {
            "timestamp": ["2026-05-18 00:00:00"],
            "temperature_2m": [15.2],
            "precipitation": [0.0],
            "wind_speed_10m": [8.5],
        }
    )

    db_path = tmp_path / "test_weather.db"
    table_name = "weather_hourly_test"

    save_to_sqlite(df, str(db_path), table_name)

    with sqlite3.connect(db_path) as conn:
        result = conn.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        ).fetchone()[0]

    assert result == 1
