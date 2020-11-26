import pandas as pd

daily_all = pd.read_csv("data/daily_report.csv")
conditions = ["confirmed", "deaths", "recovered"]


def make_time_df(condition):
    time_df = pd.read_csv(f"data/time_{condition}.csv")
    time_sum_df = time_df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"]).sum(
    ).reset_index(name=f"{condition}").rename(columns={"index": "date"})
    return time_sum_df


def make_all_conditions_time_df():
    # daily info(confirmed/death/recover)
    acc_df = None
    for condition in conditions:
        df = make_time_df(condition)
        if acc_df is None:
            acc_df = df
        else:
            acc_df = acc_df.merge(df)
    return acc_df


def make_country_df(condition, country):
    country_df = pd.read_csv(f"data/time_{condition}.csv")
    # get row info : loc[df[true]]
    country_df = country_df.loc[country_df["Country/Region"] == country]
    country_sum_df = country_df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"]).sum(
    ).reset_index(name=f"{condition}").rename(columns={"index": "date"})
    return country_sum_df


def make_all_conditions_country_df(country):
    acc_df = None
    for condition in conditions:
        df = make_country_df(condition, country)
        if acc_df is None:
            acc_df = df
        else:
            acc_df = acc_df.merge(df)
    acc_df


# by all
daily_total_df = daily_all[["Confirmed", "Deaths", "Recovered"]]
total_sum_df = daily_total_df.sum().reset_index().rename(
    columns={"index": "condition"})

# by country
daily_country_df = daily_all[["Country_Region",
                              "Confirmed", "Deaths", "Recovered"]]
country_sum_df = daily_country_df.groupby("Country_Region").sum().reset_index()
