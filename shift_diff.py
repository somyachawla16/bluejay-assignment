import pandas as pd
from datetime import datetime, timedelta

df = pd.read_excel("./Assignment_Timecard.xlsx")

def shift_diff():
    pos_id_list = df['Position ID'].unique()
    
    
    pos_dict = {}   

    for pos_id in pos_id_list:
        
        temp_df = df[df['Position ID'] == pos_id].copy(deep=True)
        
        if len(temp_df) <= 1:
            continue

        
        temp_df['Shift In Date'] = temp_df['Time'].apply(lambda x : datetime.date(x) if type(x) != float else datetime.strptime('00-00-00', '%Y-%m-%d'))
        temp_df['Shift In Time'] = temp_df['Time'].apply(lambda x : datetime.time(x) if type(x) != float else datetime.strptime('00:00','%H:%M'))
        temp_df['Shift Out Date'] = temp_df['Time Out'].apply(lambda x : datetime.date(x) if type(x) != float else datetime.strptime('00-00-00', '%Y-%m-%d'))
        temp_df['Shift Out Time'] = temp_df['Time Out'].apply(lambda x : datetime.time(x) if type(x) != float else datetime.strptime('00:00','%H:%M'))
    
        var_list = temp_df['Shift In Date'].unique()

        for var in var_list:
            
            shift_df = temp_df[temp_df['Shift In Date'] - var == timedelta(0)][['Time', 'Time Out']]
            value = 0
            
            if len(shift_df) == 3:
                diff =  shift_df['Time'].iloc[1] - shift_df['Time Out'].iloc[0]
                diff2 = shift_df['Time'].iloc[2] - shift_df['Time Out'].iloc[1]  
                value = max(diff,diff2)
                if value < timedelta(hours=10) and value > timedelta(hours=1):
                    pos_dict[pos_id] = temp_df[temp_df['Position ID'] == pos_id]['Employee Name'].unique()[0]

            elif len(shift_df) == 2:
                value =  shift_df['Time'].iloc[1] - shift_df['Time Out'].iloc[0]  
                if value < timedelta(hours=10) and value > timedelta(hours=1):
                    pos_dict[pos_id] = temp_df[temp_df['Position ID'] == pos_id]['Employee Name'].unique()[0]

    return pos_dict

