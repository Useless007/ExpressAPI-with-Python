import pandas as pd
from sqlalchemy import create_engine

# Read the CSV file with specified column names
df = pd.read_csv('../ExpressAPIWithPython/python/data_with_timestamp.csv', names=['username', 'datetime'])

# Create a connection to PostgreSQL
engine = create_engine('postgresql://username:password@localhost:postgresport/dbname')

# Insert the data into the "logs" table
df.to_sql('logs', con=engine, if_exists='append', index=False)

print("Finish")
