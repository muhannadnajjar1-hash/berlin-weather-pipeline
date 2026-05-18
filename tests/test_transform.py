import pandas as pd

from src.transform import transform_weather_data


def test_transform_weather_data_returns_dataframe():
    raw_data = {
        "hourly": {
            "time": ["2026-05-18T00:00", "2026-05-18T01:00"],
            "temperature_2m": [15.2, 14.8],
            "precipitation": [0.0, 0.1],
            "wind_speed_10m": [8.5, 7.9],
        }
    }

    df = transform_weather_data(raw_data)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert "timestamp" in df.columns
    assert "time" not in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])


def test_transform_weather_data_fails_without_hourly():
    raw_data = {}

    try:
        transform_weather_data(raw_data)
    except ValueError as error:
        assert "Missing 'hourly'" in str(error)
    else:
        raise AssertionError("Expected ValueError was not raised")
