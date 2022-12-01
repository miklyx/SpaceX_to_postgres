import requests
import json
import pandas as pd
from sqlalchemy import create_engine
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None
url = 'https://api.spacex.land/graphql'
conn_str = 'postgresql://elon:musk@localhost:8001/spacex-db'
#conn_str = 'postgresql://elon:musk@127.0.0.1:5432/spacex-db'

def get_table(query, url):
    r = requests.post(url, json={'query': query})
    r_data = json.loads(r.text)['data']
    return r_data

def make_df(content, table_name):
    df = pd.DataFrame(content[str(table_name)])
    return df

def create_tab_query(table_name, df):
    start_text = "CREATE TABLE IF NOT EXISTS " + table_name + " ("
    end_text=")"
    for t in df:
        start_text = start_text + t + ' text,'
    result = start_text[:-1] + end_text
    return result

def insert_into_query_arr(table_name, df):
    text = "INSERT INTO " + table_name + "(" +  ", ".join(df.columns.tolist()) + ")"
    st = [text + " VALUES%s"% str(row[1:]) for row in df.itertuples() ]
    return st

def run_query(query):
    db = create_engine(conn_str)
    db.execute(query)
    db.execute('COMMIT')
