import json
import logging
from pathlib import Path

import requests
import yaml


def load_config(config_path: str) -> dict:
    """
    Load pipeline configuration from a YAML file.
    """
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open() as file:
        config = yaml.safe_load(file)

    logging.info("Loaded config from %s", path)

    return config


def fetch_weather_data(api_config: dict) -> dict:
    """
    Fetch hourly weather data from the Open-Meteo API.
    """
    params = {
        "latitude": api_config["latitude"],
        "longitude": api_config["longitude"],
        "timezone": api_config["timezone"],
        "start_date": api_config["start_date"],
        "end_date": api_config["end_date"],
        "hourly": ",".join(api_config["hourly_variables"]),
    }

    response = requests.get(
        api_config["base_url"],
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    weather_data = response.json()

    logging.info("Fetched weather data from API")

    return weather_data


def save_raw_json(data: dict, output_path: str) -> None:
    """
    Save raw API response as JSON.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as file:
        json.dump(data, file, indent=2)

    logging.info("Saved raw JSON data to %s", path)
