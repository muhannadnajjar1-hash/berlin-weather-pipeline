import pandas as pd
import pytest

from src.validate import validate_weather_data


def make_valid_weather_df():
    return pd.DataFrame(
        {
            "timestamp": pd.to_datetime(["2026-05-18 00:00:00"]),
            "temperature_2m": [15.2],
            "precipitation": [0.0],
            "wind_speed_10m": [8.5],
        }
    )


def test_validate_weather_data_passes_for_valid_data():
    df = make_valid_weather_df()

    validate_weather_data(df)


def test_validate_weather_data_fails_for_missing_columns():
    df = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(["2026-05-18 00:00:00"]),
            "temperature_2m": [15.2],
        }
    )

    with pytest.raises(ValueError, match="missing columns"):
        validate_weather_data(df)


def test_validate_weather_data_fails_for_negative_precipitation():
    df = make_valid_weather_df()
    df.loc[0, "precipitation"] = -1

    with pytest.raises(ValueError, match="precipitation"):
        validate_weather_data(df)


def test_validate_weather_data_fails_for_negative_wind_speed():
    df = make_valid_weather_df()
    df.loc[0, "wind_speed_10m"] = -1

    with pytest.raises(ValueError, match="wind_speed_10m"):
        validate_weather_data(df)
