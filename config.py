#%%
import configparser
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read('config.cfg')

engine = create_engine(config.get('database', 'con'))

with open('db/table_create_statement.sql','r') as fp:
    table_create_statement = fp.read()

with engine.connect() as conn:
    cursor = conn.execute(table_create_statement)
