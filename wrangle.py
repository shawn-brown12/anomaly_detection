import pandas as pd
import numpy as npo
import os
from env import host, username, password



def get_connection(db, user=username, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'