from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def create_temperature_trend_chart(
    input_path: str = "data/processed/weather_2025_historical.csv",
    output_path: str = "reports/weather_temperature_trend.png",
) -> None:
    df = pd.read_csv(input_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 5))
    plt.plot(df["timestamp"], df["temperature_2m"])
    plt.title("Hourly Temperature Trend in Berlin")
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


if __name__ == "__main__":
    create_temperature_trend_chart()
