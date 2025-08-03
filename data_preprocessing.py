import pandas as pd

def load_and_prepare_data(path="data/hotel_booking_demand.csv"):
    df = pd.read_csv(path)

    df["arrival_date"] = pd.to_datetime(
        df["arrival_date_year"].astype(str) + "-" +
        df["arrival_date_month"] + "-" +
        df["arrival_date_day_of_month"].astype(str),
        format="%Y-%B-%d"
    )

    df["revenue"] = df["adr"] * (df["stays_in_weekend_nights"] + df["stays_in_week_nights"])
    df = df[df["adr"] > 0]

    return df
