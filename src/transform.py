import logging

import pandas as pd


def transform_weather_data(raw_data: dict) -> pd.DataFrame:
    """
    Transform raw Open-Meteo JSON response into a clean hourly weather DataFrame.
    """
    hourly_data = raw_data.get("hourly")

    if hourly_data is None:
        raise ValueError("Missing 'hourly' section in API response")

    df = pd.DataFrame(hourly_data)

    if "time" not in df.columns:
        raise ValueError("Missing 'time' column in hourly weather data")

    df = df.rename(columns={"time": "timestamp"})

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    logging.info("Transformed weather data with shape %s", df.shape)

    return df
