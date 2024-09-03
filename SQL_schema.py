from sqlalchemy import create_engine, text

# Connection information
database = 'master'
server = 'localhost\SQLEXPRESS'

connection_string = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(connection_string)

# Test the connection
with engine.connect() as connection:
    SQL_script = """
    CREATE TABLE Reddit_Playground(
    POST_TITLE NVARCHAR(255),
    SUBREDDIT NVARCHAR(255),
    TIMESTAMP DATETIME,
    UPVOTE_COUNT INT,
    UPVOTE_RATIO FLOAT
    );
    """
    result = connection.execute(text(SQL_script))
    ##print(result.fetchone())
