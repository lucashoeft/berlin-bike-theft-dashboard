import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy

def get_engine():
    """Connect to the Postgres database"""
    engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres:5432/berlin_bike_theft_db', echo=False)
    return engine

def load_bike_theft_data():
    """Access the bike theft data"""
    bike_thefts_df = pd.read_csv(
        'https://www.polizei-berlin.eu/Fahrraddiebstahl/Fahrraddiebstahl.csv', 
        sep=',', 
        low_memory=False, 
        encoding='ISO-8859-1',
        parse_dates=['ANGELEGT_AM', 'TATZEIT_ANFANG_DATUM', 'TATZEIT_ENDE_DATUM'],
        date_format="%d.%m.%Y")
    
    bike_thefts_df.columns = map(str.lower, bike_thefts_df.columns)
    
    return bike_thefts_df

def read_lor_data():
    """Read file about LOR"""
    lor_df = pd.read_excel("lor_planungsraeume.xlsx", sheet_name='LOR_2023_Übersicht')

    lor_df.columns = map(str.lower, lor_df.columns)

    return lor_df

def save_data_in_db(df, engine, table_name):
    """Store the LOR dataframe into the database table"""
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def main():
    """Download the data and store it in the database"""
    engine = get_engine()
    bike_theft_df = load_bike_theft_data()
    save_data_in_db(bike_theft_df, engine, 'bike_thefts')

    berlin_lor_df = read_lor_data()
    save_data_in_db(berlin_lor_df, engine, 'berlin_lor')

if __name__ == "__main__":
    main()