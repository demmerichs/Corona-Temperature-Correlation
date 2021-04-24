#!/usr/bin/env python3

import os.path as osp

import requests
import yaml
from tqdm import tqdm

from load_data import corona_data, reformat_lk_name

SRC_DIR = osp.join(osp.dirname(__file__), "..")


def load_geoloc_data():
    with open(
        osp.join(SRC_DIR, "data", "landkreis_locs.yml"), "r", encoding="utf-8"
    ) as fin:
        return yaml.safe_load(fin)


def save_geoloc_data(landkreis_database):
    with open(
        osp.join(SRC_DIR, "data", "landkreis_locs.yml"), "w", encoding="utf-8"
    ) as fout:
        fout.write(yaml.safe_dump(landkreis_database, default_flow_style=False))


def extract_geoloc_from_xml_string(data_str: str):
    index = data_str.index(r"lat=\'")
    lat_str = data_str[index + 6 :]
    lat_str = lat_str[: lat_str.index("\\")]
    index = data_str.index(r"lon=\'")
    lon_str = data_str[index + 6 :]
    lon_str = lon_str[: lon_str.index("\\")]
    return [float(lat_str), float(lon_str)]


base_request = (
    "https://nominatim.openstreetmap.org/search?country=Germany&county=%s&format=xml"
)


def get_geo_data(lk: str):
    if lk[:3] in {"SK ", "LK "}:
        lk_no_prefix = lk[3:]
    elif lk[:12] == "StadtRegion ":
        lk_no_prefix = lk[12:]
    else:
        assert lk[:7] == "Region ", lk
        lk_no_prefix = lk[7:]
    if lk_no_prefix == "Bergstraße":
        lk_no_prefix = "Kreis " + lk_no_prefix
    if lk_no_prefix == "Neumarkt i.d.OPf.":
        lk_no_prefix = "Landkreis Neumarkt in der Oberpfalz"
    if lk_no_prefix in {
        "Berlin Mitte",
        "Berlin Friedrichshain-Kreuzberg",
        "Berlin Pankow",
        "Berlin Charlottenburg-Wilmersdorf",
        "Berlin Spandau",
        "Berlin Steglitz-Zehlendorf",
        "Berlin Tempelhof-Schöneberg",
        "Berlin Neukölln",
        "Berlin Treptow-Köpenick",
        "Berlin Marzahn-Hellersdorf",
        "Berlin Lichtenberg",
        "Berlin Reinickendorf",
    }:
        lk_no_prefix = "Berlin"
        return (
            str(
                requests.get(
                    base_request.replace("county", "city")
                    % lk_no_prefix.replace(" ", "+")
                ).content
            ),
            base_request.replace("county", "city") % lk_no_prefix.replace(" ", "+"),
        )
    return (
        str(requests.get(base_request % lk_no_prefix.replace(" ", "+")).content),
        base_request % lk_no_prefix,
    )


try:
    landkreis_database = load_geoloc_data()
except FileNotFoundError:
    landkreis_database = {}

print("nbr Landkreise: %d" % len(corona_data["Landkreis"].unique()))

pbar = tqdm(corona_data["Landkreis"].unique())
for lk in pbar:
    pbar.set_description("Processing %s ..." % lk)
    if reformat_lk_name(lk) in landkreis_database:
        continue
    answer, cur_request = get_geo_data(lk)
    try:
        landkreis_database[reformat_lk_name(lk)] = extract_geoloc_from_xml_string(
            answer
        )
    except Exception:
        print(lk)
        print(answer)
        print(cur_request)
        save_geoloc_data(landkreis_database)
        raise

save_geoloc_data(landkreis_database)
