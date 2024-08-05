import pandas as pd
from sqlalchemy import create_engine


# Connect to the MySQL database
#replace username, password, portno  and dbname according to your MySQL user creds, port configuration and schema name
CONN_STRING = 'mysql+pymysql://etl_user:Etl#1234@localhost:3306/phonepe_data'
ENGINE = create_engine(CONN_STRING)

# Function to retrieve year names data from MySQL

def fetch_years():
    QUERY = "SELECT DISTINCT(Year) FROM phonepe_data.aggregate_transactions"
    df = pd.read_sql(QUERY, ENGINE)
    return df


#Function to fetch data for aggregate transactions
def fetch_aggregate_transactions(year,quarter):
    qry="SELECT * FROM phonepe_data.aggregate_transactions agt where agt.Year=:year and agt.Quarter=:quarter"
    parameters={}
    parameters['year'] = year
    parameters['quarter'] = quarter
    df = pd.read_sql(qry, ENGINE, params=parameters)
    return df

#Function to fetch data for aggregate users
def fetch_aggregate_users(year,quarter):
    QUERY="SELECT * FROM phonepe_data.aggregate_users agt where agt.Year=:year and agt.Quarter=:quarter"
    parameters={}
    parameters['year'] = year
    parameters['quarter'] = quarter
    df = pd.read_sql(QUERY, ENGINE, params=parameters)
    return df