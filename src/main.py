import logging

from ingest import fetch_weather_data, load_config, save_raw_json
from load import save_csv, save_parquet, save_to_sqlite
from transform import transform_weather_data
from validate import validate_weather_data

CONFIG_PATH = "config/config.yaml"


def main() -> None:
    """
    Run the Berlin weather ETL pipeline.
    """
    config = load_config(CONFIG_PATH)

    logging.basicConfig(
        level=getattr(logging, config["logging"]["level"]),
        format="%(asctime)s %(levelname)s %(message)s",
        force=True,
    )

    logging.info("Starting Berlin weather ETL pipeline")

    raw_data = fetch_weather_data(config["api"])

    save_raw_json(
        raw_data,
        config["output"]["raw_json_path"],
    )

    weather_df = transform_weather_data(raw_data)

    validate_weather_data(weather_df)

    save_csv(
        weather_df,
        config["output"]["processed_csv_path"],
    )

    save_parquet(
        weather_df,
        config["output"]["processed_parquet_path"],
    )

    save_to_sqlite(
        weather_df,
        config["output"]["sqlite_path"],
        config["output"]["table_name"],
    )

    logging.info("Berlin weather ETL pipeline finished successfully")
    logging.info("Final rows: %s", len(weather_df))


if __name__ == "__main__":
    main()
