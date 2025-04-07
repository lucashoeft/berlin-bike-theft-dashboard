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
    
    bike_thefts_df['tatzeit_anfang'] = pd.to_datetime(bike_thefts_df['tatzeit_anfang_datum'].astype(str) 
                                                      + ' ' 
                                                      + bike_thefts_df['tatzeit_anfang_stunde'].astype(str) 
                                                      + ':00:00')
    
    bike_thefts_df['tatzeit_ende'] = pd.to_datetime(bike_thefts_df['tatzeit_ende_datum'].astype(str) 
                                                      + ' ' 
                                                      + bike_thefts_df['tatzeit_ende_stunde'].astype(str) 
                                                      + ':00:00')
    
    return bike_thefts_df

def read_lor_data():
    """Read file about LOR"""
    lor_df = pd.read_excel("lor_planungsraeume.xlsx", sheet_name='LOR_2023_Übersicht')

    lor_df.columns = map(str.lower, lor_df.columns)

    return lor_df

def read_geo_data(file_name):
    """Read csv file """
    geo_df = pd.read_csv(file_name)

    geo_df.columns = map(str.lower, geo_df.columns)

    return geo_df

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

    geo_data_df = read_geo_data('bezirke.csv')
    save_data_in_db(geo_data_df, engine, 'geo_lor')

    bezirksregionen_df = read_geo_data('bezirksregionen.csv')
    save_data_in_db(bezirksregionen_df, engine, 'bezirksregionen_lor')

    planungsraeume_df = read_geo_data('planungsraeume.csv')
    save_data_in_db(planungsraeume_df, engine, 'planungsraeume_lor')

    prognoseraeume_df = read_geo_data('prognoseraeume.csv')
    save_data_in_db(prognoseraeume_df, engine, 'prognoseraeume_lor')

if __name__ == "__main__":
    main()