import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy

engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres:5432/berlin_bike_theft_db', echo=False)

# read data (format date columns correctly)
bike_thefts_df = pd.read_csv(
    'https://www.polizei-berlin.eu/Fahrraddiebstahl/Fahrraddiebstahl.csv', 
    sep=',', 
    low_memory=False, 
    encoding='ISO-8859-1',
    parse_dates=['ANGELEGT_AM', 'TATZEIT_ANFANG_DATUM', 'TATZEIT_ENDE_DATUM'],
    date_format="%d.%m.%Y")

bike_thefts_df.to_sql('bike_thefts', con=engine, if_exists='replace', index=False)