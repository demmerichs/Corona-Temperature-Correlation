# Corona Temperature Correlation
Analyzing data for Germany 2020 to understand if and how temperature might affect the reproduction of the corona virus.

## Materials

- RKI Nowcasting methodical description in ["Epidemiologisches Bulletin" Ausgabe 17 2020 released 23. April 2020](https://www.rki.de/DE/Content/Infekt/EpidBull/Archiv/2020/Ausgaben/17_20.pdf?__blob=publicationFile)
- [RKI R-Wert Berechnung](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Projekte_RKI/R-Wert-Erlaeuterung.pdf?__blob=publicationFile)
- [Quelle für Geo-Locations von Landkreisen](https://nominatim.openstreetmap.org/ui/search.html?q=kiel)

## Datasets

- [Corona Numbers in Germany from RKI](https://www.arcgis.com/home/item.html?id=f10774f1c63e40168479a1feb6c7ca74)
    - data is available under [Open Data Datenlizenz Deutschland - Namensnennung - Version 2.0](https://www.govdata.de/dl-de/by-2-0) and has the following information appended:
    - Quellenvermerk: Robert Koch-Institut (RKI), dl-de/by-2-0   Haftungsausschluss: „Die Inhalte, die über die Internetseiten des Robert Koch-Instituts zur Verfügung gestellt werden, dienen ausschließlich der allgemeinen Information der Öffentlichkeit, vorrangig der Fachöffentlichkeit“.
- [Temperature data for Europe from European Climate Assessment & Dataset](https://www.ecad.eu/download/ensembles/download.php#chunks)
    - Citation:
    - We acknowledge the E-OBS dataset from the EU-FP6 project UERRA (http://www.uerra.eu) and the Copernicus Climate Change Service, and the data providers in the ECA&D project (https://www.ecad.eu)"
    "Cornes, R., G. van der Schrier, E.J.M. van den Besselaar, and P.D. Jones. 2018: An Ensemble Version of the E-OBS Temperature and Precipitation Datasets, J. Geophys. Res. Atmos., 123. doi:10.1029/2017JD028200"
- [Nowcasting Zahlen und R-Wert Download](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Projekte_RKI/Nowcasting.html)
