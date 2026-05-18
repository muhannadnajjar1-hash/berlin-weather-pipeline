import logging

import pandas as pd


REQUIRED_COLUMNS = {
    "timestamp",
    "temperature_2m",
    "precipitation",
    "wind_speed_10m",
}


def validate_weather_data(df: pd.DataFrame) -> None:
    """
    Validate transformed hourly weather data.
    """
    logging.info("Starting weather data validation")

    if df.empty:
        raise ValueError("Validation failed: weather dataset is empty")

    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Validation failed: missing columns {missing_columns}")

    if df["timestamp"].isna().any():
        raise ValueError("Validation failed: timestamp contains missing values")

    if df["temperature_2m"].isna().all():
        raise ValueError("Validation failed: temperature_2m is completely empty")

    if (df["precipitation"].dropna() < 0).any():
        raise ValueError("Validation failed: precipitation contains negative values")

    if (df["wind_speed_10m"].dropna() < 0).any():
        raise ValueError("Validation failed: wind_speed_10m contains negative values")

    logging.info("Weather data validation passed")
