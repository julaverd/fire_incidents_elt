import os
import io
import pandas as pd
from sqlalchemy import create_engine

class Load():
    def __init__(self):
        self._PERSISTENCE_NAME = 'Fire_Incidents'
        self._origin_path = 'data'
        self._origin_suffix = 'csv'
        self._conn_str = 'postgresql+psycopg2://fep_dev:1234@localhost:5432/postgres'


    def load_data_local(self):
        self._origin_file = self._PERSISTENCE_NAME
        self._origin_file_name = os.path.join(self._origin_path, self._PERSISTENCE_NAME + "." + self._origin_suffix)
        self._df_csv_data = pd.read_csv(self._origin_file_name)
        return self._df_csv_data


    def copy_data(self, df):
        self._engine = create_engine(self._conn_str)

        df.head(0).to_sql(self._PERSISTENCE_NAME, self._engine, if_exists='replace', index=False)

        self._conn = self._engine.raw_connection()
        self._cur = self._conn.cursor()
        self._output = io.StringIO()
        df.to_csv(self._output, sep='\t', header=False, index=False)
        self._output.seek(0)
        self._contents = self._output.getvalue()
        self._cur.copy_from(self._output, self._PERSISTENCE_NAME, null="")
        self._conn.commit()








