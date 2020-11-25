import pandas as pd

daily_all = pd.read_csv("data/daily_report.csv")
conditions = ["confirmed", "deaths", "recovered"]


def make_time_df(condition):
    time_df = pd.read_csv(f"data/time_{condition}.csv")
    time_sum = time_df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"]).sum(
    ).reset_index(name=f"{condition}").rename(columns={"index": "date"})
    return time_sum


# by all
daily_total_df = daily_all[["Confirmed", "Deaths", "Recovered"]]
total_sum = daily_total_df.sum().reset_index().rename(
    columns={"index": "condition"})

# by country
daily_country_df = daily_all[["Country_Region",
                              "Confirmed", "Deaths", "Recovered"]]
country_sum = daily_country_df.groupby("Country_Region").sum().reset_index()

# daily info(confirmed/death/recover)
acc_df = None
for condition in conditions:
    df = make_time_df(condition)
    if acc_df is None:
        acc_df = df
    else:
        acc_df = acc_df.merge(df)


# -------


def make_country_df(condition, country):
    country_df = pd.read_csv(f"data/time_{condition}.csv")
    country_df = country_df.loc[["Country/Region"] == country]
    country_sum = country_df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"]).sum(
    ).reset_index(name=f"{condition}").rename(columns={"index": "date"})
    return country_sum


acc_df = None
for condition in conditions:
    df = make_country_df(condition)
    if acc_df is None:
        acc_df = df
    else:
        acc_df = acc_df.merge(df)

acc_df
