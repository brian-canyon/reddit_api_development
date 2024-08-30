import pandas as pd
from sqlalchemy import create_engine, text

# Replace 'your_database' with your actual database name
database = 'master'
server = 'localhost\SQLEXPRESS'

connection_string = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(connection_string)

# Test the connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM [msdb].[dbo].[sysjobs]"))
    print(result.fetchone())
