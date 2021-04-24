#!/usr/bin/env python3

import os.path as osp
import pandas

raw_lk_names = {}


def reformat_lk_name(lk):
    result = (
        lk.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    )
    raw_lk_names[result] = lk
    return result


corona_data = pandas.read_csv(
    osp.join(osp.dirname(__file__), "..", "data", "in", "RKI_COVID19.csv")
)

for lk in corona_data["Landkreis"].unique():
    reformat_lk_name(lk)
