from datetime import datetime
from datetime import timedelta
import pandas as pd

df = pd.read_excel('Assignment_Timecard.xlsx',parse_dates=True)

def get_consecutive_days():
    pos_id_list = df['Position ID'].unique()
    employee_dict = {}

    for pos_id in pos_id_list:
        days_date_list = df[df['Position ID'] == pos_id]['Time'].dt.date.unique()
        counter = 0
        for i in range(1,len(days_date_list)):
            days = days_date_list[i] - days_date_list[i-1]
            if days.days != timedelta(days=1).days:
                break    
            else:
                counter = counter + 1
                if counter >= 7:
                    employee_dict[pos_id] = df[df["Position ID"] == pos_id]["Employee Name"].unique()[0]
    
    
    return employee_dict
