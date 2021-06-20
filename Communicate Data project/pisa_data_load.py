"""
Python methods for loading and processing PISA data in sqlite database. This python file is referenced by
the jupyter notebook called PISA Data Part 1.

"""

import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def load_pisa_database(file):
    """
    Load pisa.csv raw data file into sqllite database so that the pisa data can be queried on
    with Sql.  The raw pisa csv file name passed into this function is a very large file.  It is loaded into a
    pandas dataframe using chunking option.

    For each chunk of pisa data rows loaded into the pandas dataframe, the dataframe records are loaded into a
    sqllite database table called pisa.

    args:
        file: raw pisa data file name
    """

    pisa2012_database = create_engine('sqlite:///pisa2012_database.db')
    table_name = 'pisa'

    chunk_size = 50000
    i = 0
    j = 0

    for df in pd.read_csv(file, chunksize=chunk_size, iterator=True, encoding='ISO-8859-1'):
        df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
        df.index += j
        df.to_sql(table_name, pisa2012_database, if_exists='append')
        j = df.index[-1] + 1
        print('| index: {}'.format(j))


