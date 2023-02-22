import pandas as pd
import numpy as npo
import os
from env import host, username, password

#--------------------------------------------------------------------

def get_connection(db, user=username, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
#--------------------------------------------------------------------

def get_groceries():

    if os.path.isfile('grocery_db.csv'):
        
        df = pd.read_csv('grocery_db.csv')
        df = df.drop(columns='Unnamed: 0')

        return df
    
    else:
        
        url = wr.get_connection('grocery_db')
        query = '''
                SELECT *
                FROM grocery_customers;
                '''
        df = pd.read_sql(query, url)                
        df.to_csv('grocery_db.csv')

        return df

#--------------------------------------------------------------------



#--------------------------------------------------------------------



#--------------------------------------------------------------------



#--------------------------------------------------------------------



#--------------------------------------------------------------------
