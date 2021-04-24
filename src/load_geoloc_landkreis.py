#!/usr/bin/env python3

import os.path as osp
import yaml

SRC_DIR = osp.join(osp.dirname(__file__), "..")


def reformat_lk_name(lk):
    result = (
        lk.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    )
    return result


def load_geoloc_data():
    with open(
        osp.join(SRC_DIR, "data", "landkreis_locs.yml"), "r", encoding="utf-8"
    ) as fin:
        return yaml.safe_load(fin)


landkreis_database = load_geoloc_data()


def get_geoloc(lk):
    return landkreis_database[reformat_lk_name(lk)]


if __name__ == "__main__":
    print(get_geoloc("SK Zweibrücken"))
