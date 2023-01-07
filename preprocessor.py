import re
import pandas as pd

def preprocess(data):
    pattern='\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\w{2}\s-\s'
    
    messages=re.split(pattern,data)[1:]
    
    dates=re.findall(pattern,data)
    for i in range(len(dates)):
        dates[i]=dates[i].replace(' - ','').replace(',','')
    df=pd.DataFrame({'user_message':messages,'date':dates})
    df['date']=pd.to_datetime(df['date'])
    
    users=[]
    message=[]
    for m in df['user_message']:
        entry=re.split('([\w\W]+?):\s',m)
        if entry[1:]:
            users.append(entry[1])
            message.append(entry[2])
        else:
            users.append('group_notification')
            message.append(entry[0])
    df['user']=users
    df['message']=message
    df.drop(columns='user_message',inplace=True)
    
    df['only_date']=df['date'].dt.date
    df['day_name']=df['date'].dt.day_name()
    df['year']=df['date'].dt.year
    df['month_num']=df['date'].dt.month
    df['month']=df['date'].dt.month_name()
    df['day']=df['date'].dt.day
    df['hour']=df['date'].dt.hour
    df['minute']=df['date'].dt.minute 
    
    return df