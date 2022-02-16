import pandas as pd
import psycopg2 as pg
import os

from sqlalchemy import create_engine
import io

import logging
from config import config

PERSISTENCE_NAME = 'Fire_Incidents'

def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)
    except:
        return ''

def load_data_local():
    origin_path = '../data'
    origin_file = PERSISTENCE_NAME
    origin_suffix = 'csv'
    origin_file_name = os.path.join(origin_path, origin_file + "." + origin_suffix)
    df_csv_data = pd.read_csv(origin_file_name, \
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
    """Method to connect to postgres database server"""
    conn=None
    try:
        params=config()
        conn = pg.connect(**params)
    except pg.OperationalError:
        logging.Logger.info("Unable to connect to Postgres Database server")
        pass
    return conn

def create_table(conn):
    dir_name = os.path.join(os.getcwd(), 'sql')
    base_filename = PERSISTENCE_NAME
    filename_suffix = 'sql'
    file_name = os.path.join(dir_name, base_filename + "." + filename_suffix)
    sql_file = open(file_name, 'r')
    cur = conn.cursor()
    cur.execute(sql_file.read())
    conn.commit()

def copy_data(df):
    engine = create_engine('postgresql+psycopg2://fep_dev:1234@localhost:5432/postgres') # Needs to hide

    df.head(0).to_sql(PERSISTENCE_NAME, engine, if_exists='replace',
                      index=False)  # drops old table and creates new empty table

    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, PERSISTENCE_NAME, null="")  # null values become ''
    conn.commit()

if __name__ == "__main__":

    print("Reading Downloaded Fire Incidents from local ..")
    df_load = load_data_local()
    conn = ps_connect()

    #create_table(conn)
    print("Reading Downloaded Fire Incidents from local ..")
    copy_data(df_load)





