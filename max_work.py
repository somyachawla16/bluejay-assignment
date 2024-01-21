import time
from numpy import timedelta64
import pandas as pd
from datetime import datetime, timedelta

df = pd.read_excel('./Assignment_Timecard.xlsx',parse_dates=True)

def max_work():
    d = '0001-01-01'
    d = datetime.strptime(d,'%Y-%m-%d')
    
    df['Timecard Hours (as Time)'] = df['Timecard Hours (as Time)'].apply(lambda x: datetime.strptime(x,'%H:%M').hour if type(x) is not float else datetime.strptime('00:00', "%H:%M").hour)
    
    return df[df['Timecard Hours (as Time)'] >= 14][['Position ID', 'Employee Name']].to_dict('records')
    