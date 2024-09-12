This project highlights the use of the requests library in python by showcasing
a practical ETL pipeline. This pipeline includes the following elements:

    - REST API calls (extract)
    - Data transformations (transform)
    - Inserting data to SQL database (load)

Extration of data is done via REST API calls. An API (application program interface)
enables the interactio between different software applications by following REST
archtitecutre principles (representational state transfer). Authentication to this
service requires a few different parameters. In this example, I am leveraging an 
account username, password, and PAT (personal access token). Once authenticated, 
a GET request is made to extract specific information. This data is ingested via
JSON format.

The data transformations in this project leverage the pandas library. Essentially,
the JSON style data is handeled as a dictionary in python and only relevant information
is parsed and inserted into a dataframe.

For this project, I created a SQL database that is hosted on my local macheine. 
Authentication to this database is supported by the sqlalchemy libary. Once 
authentication parameters are identified, pandas has a built in function 'to_sql'
that makes inserting data to SQL a breeze.