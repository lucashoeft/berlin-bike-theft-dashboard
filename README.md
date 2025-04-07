# Berlin Bike Theft Dashboard

This project provides an interactive Grafana dashboard on bicycle thefts in Berlin. The data source is the police dataset from the Berlin Open Data Portal, which is updated daily. A sample file for the year 2024 and the dataset description can be found in the assets folder of this repository. The data has been enriched with geographic information about the locations of the thefts.

<p align="center">
<img width="890" alt="" src="/assets/images/screenshot_dashboard.png">
</p>

<p align="center">
<img width="890" alt="" src="/assets/images/screenshot_dashboard1.png">
</p>

<p align="center">
<img width="890" alt="" src="/assets/images/screenshot_dashboard2.png">
</p>

<p align="center">
<img width="890" alt="" src="/assets/images/screenshot_dashboard3.png">
</p>

### Links

* [Polizei Berlin LKA St 14 – Fahrraddiebstahl in Berlin (Berlin Open Data)](https://daten.berlin.de/datensaetze/fahrraddiebstahl-in-berlin)
* [Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen – Lebensweltlich orientierte Räume (LOR) in Berlin](https://www.berlin.de/sen/sbw/stadtdaten/stadtwissen/sozialraumorientierte-planungsgrundlagen/lebensweltlich-orientierte-raeume/)

### How to Use the Dashboard

1. Clone this repository.

2. Start docker on your computer.

3. Run the command `docker compose up` in the directory of the cloned repository.

4. Access the dashboard at `localhost:3000` in your web browser.

### Further Ideas

Data Sources:
* Add meteorological data (weather, sunset, sunrise)
* Add information about public holidays
* Add more geographical data (population density)

Dashboard:
* Add trends (WoW, MoM, YoY growth rates)
* Analyze the time duration when the crime could have occurred ("Tatzeitraum")
