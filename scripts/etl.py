"""This modules implements the etl operations in the dataset"""
from pathlib import Path
import click
import pandas as pd

from utils import parse_config, set_logger


@click.command()
@click.argument("config_file", type=str, default="./config.yml")
def etl(config_file):
    """
    ETL function that load raw data, apply transformations and export data
    Args:
        config_file [str]: path to config file
    Returns:
        None
    """
    ##################
    # configure logger
    ##################
    logger = set_logger("./log/etl.log")

    ##################
    # Load config from config file
    ##################
    logger.info("Load config from %s", config_file)
    config = parse_config(config_file)

    raw_data_file = config["etl"]["raw_data_file"]
    processed_path = Path(config["etl"]["processed_path"])
    logger.info("config: %s", config['etl'])

    ##################
    # Data transformation
    ##################
    logger.info(
        "-------------------Start data transformation-------------------")
    autos = pd.read_csv(raw_data_file, encoding = 'Latin-1')

    logger.info("The %s was loaded.", raw_data_file)

    autos.rename(columns={"yearOfRegistration": "registration_year",
                          "monthOfRegistration": "registration_month",
                          "notRepairedDamage": "unrepaired_damage",
                          "dateCreated": "ad_created",
                          "dateCrawled": "date_crawled",
                          "offerType": "offer_type",
                          "vehicleType": "vehicle_type",
                          "powerPS": "power_ps",
                          "fuelType": "fuel_type",
                          "nrOfPictures": "nr_of_pictures",
                          "postalCode": "postal_code",
                          "lastSeen": "last_seen"
                          }, inplace=True)

    logger.info("The columns of 'autos' DataFrame was renamed.")

    autos.drop(["nr_of_pictures", "seller", "offer_type"], axis=1, inplace=True)

    logger.info(
        "The columns 'nr_of_pictures', 'seller', 'odometer' were dropped.")

    autos["price"] = autos["price"].str.replace(
        "$", "").str.replace(",", "").astype(int)

    logger.info("The column 'price' was converted to dtype 'int'.")

    autos["odometer"] = autos["odometer"].str.replace(
        "km", "").str.replace(",", "").astype(int)

    logger.info("The column 'odometer' was converted to dtype 'int'.")

    autos.rename(columns={"odometer": "odometer_km"}, inplace="True")

    logger.info("The column 'odometer' was renamed to 'odometer_km'.")

    autos = autos[autos["price"].between(500, 1300000)]

    logger.info(
        "'autos' was filtered by 'price' column values between 500 and 1300000.")

    autos = autos[autos["registration_year"].between(1950, 2016)]

    logger.info(
        "'autos' was filtered by 'registration_year' column values between 1950 and 2016.")

    brands = autos['brand'].value_counts(normalize=True).index[:6]

    logger.info(
        "The top 6 car brands was selected and stored in 'brands' variable")

    mean_price = {brand: autos.loc[autos["brand"]
                                   == brand, "price"].mean() for brand in brands}

    logger.info(
        "The mean price of top 6 car brands was stored in 'mean_price' dict.")

    mean_mileage = {brand: autos.loc[autos["brand"] ==
                                     brand, "odometer_km"].mean() for brand in brands}

    logger.info(
        "The mean mileage of top 6 car brands was stored in 'mean_mileage' variable.")

    logger.info(
        "-------------------End of data transformation-------------------")

    ##################
    # Export aggregate data
    ##################

    mean_price_series = pd.Series(mean_price)

    logger.info("The 'mean_price' dict was converted to pd.Series.")

    mean_mileage_series = pd.Series(mean_mileage)

    logger.info("The 'mean_mileage' dict was converted to pd.Series.")

    df_mean_price_mileage = pd.DataFrame(
        mean_price_series, columns=['mean_price'])

    logger.info("The DataFrame 'df_mean_price_mileage' was created.")

    df_mean_price_mileage["mean_mileage"] = mean_mileage_series

    logger.info(
        "The column 'mean_mileage' was added to 'df_mean_price_mileage'.")

    # exporting the data
    logger.info("Write data to %s", processed_path)

    autos.to_csv(processed_path / "autos_processed.csv", index=False)

    df_mean_price_mileage.to_csv(
        processed_path /
        "mean_price_mileage_by_brand.csv")

    logger.info("The DataFrames were saved in CSV files.")


if __name__ == '__main__':
    etl()
