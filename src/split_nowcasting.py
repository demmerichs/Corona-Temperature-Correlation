#!/usr/bin/env python3

import inspect
from pathlib import Path
import pandas as pd


def read_floats_setting_dots_to_NaN(val):
    if val == ".":
        return float("nan")
    if val == "":
        return None
    return float(val.replace(",", "."))


def main():

    this_file = Path(inspect.stack()[1].filename)
    nowcasting_fname = this_file.parent.parent / Path(
        "data/in/Nowcasting_Zahlen_csv.csv"
    )
    nowcasting_ger = pd.read_csv(
        nowcasting_fname,
        sep=";",
        decimal=",",
        error_bad_lines=False,
        converters={"Schätzer_7_Tage_R_Wert": read_floats_setting_dots_to_NaN},
    )
    n = nowcasting_ger.index[nowcasting_ger["Datum"] == "Erläuterung"]
    nowcasting_ger.drop(
        nowcasting_ger.tail(nowcasting_ger.shape[0] - n[0]).index, inplace=True
    )

    cleaned_temps_file = this_file.parent.parent / Path(
        "data/in/Temp_Germany2020_cleaned.csv"
    )
    if cleaned_temps_file.exists():
        temp_ger = pd.read_csv(cleaned_temps_file, sep=",", index_col=0)
    else:
        temp_ger_fname = this_file.parent.parent / Path("data/in/Temp_Germany2020.csv")
        temp_ger = pd.read_csv(temp_ger_fname, sep=",")
        temp_ger.dropna(inplace=True)
        temp_ger.to_csv(cleaned_temps_file)
    nowcasting_ger["Datum"] = pd.to_datetime(nowcasting_ger["Datum"])
    temp_ger["time"] = pd.to_datetime(temp_ger["time"])

    print(nowcasting_ger)
    print(temp_ger.head())
    temp_mean = temp_ger.groupby("time").mean()
    temp_mean.reset_index(inplace=True)

    # temp_now = nowcasting_ger.merge(temp_ger, on="", how="left")

    tmp_nowcasted_mergeed = pd.merge(
        temp_mean, nowcasting_ger, how="inner", left_on=["time"], right_on=["Datum"]
    )
    # tmp_nowcasted_mergeed.dropna(inplace=True)

    print("Foo!")
    print(tmp_nowcasted_mergeed.corr())
    correlation = tmp_nowcasted_mergeed.corr()
    print(correlation["Schätzer_7_Tage_R_Wert"])

    print("Done!")

    # temp_ger.to_csv("/tmp/Temp_Germany2020_cleaned.csv")


if __name__ == "__main__":
    main()
