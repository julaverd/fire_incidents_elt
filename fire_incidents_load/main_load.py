import pandas as pd
import psycopg2 as pg

def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)
    except:
        return ''

def load_data_local():
    origin_path = '../data'
    origin_file = 'Fire_Incidents.csv'
    df_csv_data = pd.read_csv(origin_path +'/'+ origin_file, \
                              converters={
                                  'Batallion': convert_dtype,
                                  'Box': convert_dtype,
                                  'Suppression Units': convert_dtype,
                                  'First Unit On Scene': convert_dtype,
                                  'Primary Situation': convert_dtype,
                                  'Action Taken Primary': convert_dtype,
                                  'Property Use': convert_dtype
                              })
    return df_csv_data

def ps_connect():
    try:
        conn = pg.connect("host=localhost dbname=postgres user=fep_dev password=1234")
    except pg.OperationalError:
        print("Can not connect to PG-DataBase")
    return conn


if __name__ == "__main__":
    print("Reading Downloaded Fire Incidents from local ..")
    df_load = load_data_local()
    conn = ps_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM notes')

