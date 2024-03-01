# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import numpy as np
import pandas as pd
import utils 
pd.set_option('display.max_rows', 8800)

# saving all the databases from the csv flies in varaiables as DataFrames
Harlington=pd.read_csv('data\\Pollution-London Harlington.csv')
Marylebone=pd.read_csv('data\\Pollution-London Marylebone Road.csv')
Kensington=pd.read_csv('data\\Pollution-London N Kensington.csv')

def daily_average(data, monitoring_station, pollutant):
    """
    this function returns an array with the daily averages for a particular pollutant and monitoring station

    data -> it has been set to an empty set and it will be taken as per the monitoring station chosen by the user
    monitoring_station -> it helps choose the database from the 3 options
    pollutant -> it helps choose the pollutant in from the database
    """ 
    # choosing database as per users choice of monitoring station
    if monitoring_station.lower()=='h':
        data = Harlington
    elif monitoring_station.lower()=='m':
        data = Marylebone
    elif monitoring_station.lower()=='k':
        data = Kensington 
    else: print('try again')
    data=data.replace('No data', '0')   #replaces No data with 0
    data=data[pollutant]    #overwrites data as series of all values of pollutant
    data=list(data) #coverts the series into a list
    mean=[]
    for i in range(0,len(data),24):
        day=[]  
        total=0
        for items in range(i,i+24):
            day.append(float(data[items]))
        x=utils.meannvalue(day) 
        mean.append(x)
    mean=np.array(mean)     #converts the variable into an array
    return mean
  

    

def daily_median(data, monitoring_station, pollutant):
    """
    this function returns an array with the daily median for a pollutant and monitoring station

    data -> it has been set to an empty set and it will be taken as per the monitoring station chosen by the user
    monitoring_station -> it will help choose the database from the 3 options
    pollutant -> it will help choose the pollutant in from the database
    """
    # choosing database as per users choice of monitoring station
    if monitoring_station.lower()=='h':
        data = Harlington
    elif monitoring_station.lower()=='m':
        data = Marylebone
    elif monitoring_station.lower()=='k':
        data = Kensington 
    else: print('try again')
    data=data.replace('No data', '0')   #replaces No data with 0
    data[pollutant]=pd.to_numeric(data[pollutant])  #overwrites data as series of all values of pollutant, converts it to numeric 
    data=data.groupby(['date']).median()    # grouping data as per date and then taking its median
    data=data.iloc[:,0]     #slicing data
    data=data.to_numpy()    #converts the variable into an array
    return data




def hourly_average(data, monitoring_station, pollutant):
    """
    returns an array with the hourly averages for a pollutant and monitoring station

    data -> it has been set to an empty set and it will be taken as per the monitoring station chosen by the user
    monitoring_station -> it will help choose the database from the 3 options
    pollutant -> it will help choose the pollutant in from the database
    """
    
    # choosing database as per users choice of monitoring station
    if monitoring_station.lower()=='h':
        data = Harlington
    elif monitoring_station.lower()=='m':
        data = Marylebone
    elif monitoring_station.lower()=='k':
        data = Kensington 
    else: print('try again')
    data=data.replace('No data', '0')   #replaces No data with 0
    data=data[pollutant]    #overwrites data as series of all values of pollutant
    data=list(data)     #coverts the series into a list
    mean=[] 
    for i in range(0,24):
        hour=[]
        for items in range(i,8760,24):
            hour.append(float(data[items]))     #adding data of particular index to the end of list hour
        x=utils.meannvalue(hour) 
        mean.append(x)
    mean=np.array(mean)     #converts the variable into an array
    return mean





def monthly_average(data, monitoring_station, pollutant):
    """
    returns an array with the monthly averages for a pollutant and monitoring station.

    data -> it has been set as an empty set and it will be taken as per the monitoring station chosen by the user
    monitoring_station -> it will help choose the database from the 3 options
    pollutant -> it will help choose the pollutant from the database
    """
    
    # choosing database as per users choice of monitoring station
    if monitoring_station.lower()=='h':
        data = Harlington
    elif monitoring_station.lower()=='m':
        data = Marylebone
    elif monitoring_station.lower()=='k':
        data = Kensington 
    else: print('try again')
    data=data.replace('No data', '0')   #replaces No data with 0
    data[pollutant]=pd.to_numeric(data[pollutant])  #overwrites data as series of all values of pollutant, converts it to numeric
    data=data.groupby(pd.PeriodIndex(data['date'],freq="M")).mean()
    data=data.iloc[:,0]     #slicing data
    data=data.to_numpy()    #converts the variable into an array
    return data




def peak_hour_date(data, date, monitoring_station,pollutant):
    """
    For a given date in the format YYYY-MM-DD this function returns the hour of the day with the highest pollution level and its corresponding value in form of a tuple (e.g., (12:00, 14.8))

    data -> it has been seet to an empty set and it will be taken as per the monitoring station chosen by the user
    date -> it will store the date the user wants the highest pollutant level for
    monitoring_station -> it will help choose the dadabase from the 3 options
    pollutant -> it will help choose the pollutant in form the database
    """
    # choosing database as per users choice of monitoring station
    if monitoring_station.lower()=='h':
        data = Harlington
    elif monitoring_station.lower()=='m':
        data = Marylebone
    elif monitoring_station.lower()=='k':
        data = Kensington 
    else: 
        print('try again')
    data=data.replace('No data', '0')   #replaces No data with 0
    data=data.set_index('date') 
    data=data.loc[date]
    data=data.set_index('time') 
    data2=data[pollutant]   #overwrites data as series of all values of pollutant
    data2=pd.to_numeric(data2)      #converts data2 to numeric
    highest_value=data2[utils.maxvalue(data2)] 
    peak_time=data2[data2==highest_value].index[0]
    peak_time=peak_time[:-3] 
    return peak_time, highest_value

    



def count_missing_data(data,  monitoring_station,pollutant):
    """
    For a given monitoring station and pollutant, returns the number of 'No data' entries are there in the data.

    data -> it has been set to an empty set and it will be taken as per the monitoring station chosen by the user
    monitoring_station -> it will help choose the dadabase from the 3 options
    pollutant -> it will help choose the pollutant from the database
    """
    # choosing database as per users choice of monitoring station
    if monitoring_station.lower()=='h':
        data = Harlington
    elif monitoring_station.lower()=='m':
        data = Marylebone
    elif monitoring_station.lower()=='k':
        data = Kensington 
    else: print('try again')  
    
      
    data=data[pollutant]    #overwrites data as series of all values of pollutant
    data=list(data)     #coverts the series into a list
    return utils.countvalue(data,"No data")
    
    



def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """
    For a given monitoring station and pollutant, returns a copy of the data with the missing values 'No data' replaced by the value in the parameter new value.

    data -> it has been set to an empty set and it will be taken as per the monitoring station chosen by the user
    new_value -> it stores the value the user gives to replavce with 'No data' in the database chosen
    monitoring_station -> it will help choose the dadabase from the 3 options
    pollutant -> it will help choose the pollutant from the database
    """
    # choosing database as per users choice of monitoring station
    if monitoring_station.lower()=='h':
        data = Harlington
    elif monitoring_station.lower()=='m':
        data = Marylebone
    elif monitoring_station.lower()=='k':
        data = Kensington 
    else: print('try again')

    data[pollutant]=data[pollutant].replace('No data', new_value) #overwrites data as series of all values of pollutant,and replaces No data with a new value choosen by the user
    data[pollutant]=pd.to_numeric(data[pollutant]) 
    return data
