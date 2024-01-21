import pandas as pd
from datetime import datetime
# get_base_data = pd.read_csv('src\data_small\stations.txt',skiprows=17)
# # print(get_base_data.columns)
# data_test = get_base_data.loc[get_base_data['STANAME                                 ']=='VAEXJOE                                 ']
# # print(data_test['STAID'].squeeze())


#Option A -> Setting config to get file station
def get_station(id):
    id_station = id
    station_name = 'TG_STAID000000'
    id_station = str(id_station)
    station_name = station_name[:-len(id_station)]
    station_name = station_name+id_station

    return station_name

#Option B -> Setting Config to get file station:
# def get_station(id):
#     station_id = id
#     station_name = 'TG_STAID'
#     station_id = '' + str(station_id)
#     station_id = str(station_id).zfill(6)
#     station_name = station_name+station_id

#     return station_name


#Get the CSV
def get_file(id):
    station_name = get_station(id)
    df = pd.read_csv(f'src\data_small\{station_name}.txt',skiprows=20,parse_dates=['    DATE'])
    return df

def get_file_set_index(id,index):
    station_name = get_station(id)
    df = pd.read_csv(f'src\data_small\{station_name}.txt',skiprows=20,parse_dates=['    DATE'],index_col=index)
    df_filtred = df.loc[df['   TG'] != -9999]
    return df_filtred

#Get The Row
def get_row_by_date(date,id):
    df = get_file(id)

    #Removing fake data
    df_row = df.loc[df['   TG'] != -9999]
    
    #Init data list
    data = []

    #testing if user enter full date or just a year
    if len(date) > 4:

        #Filtre que the row of the date
        df_row = df.loc[df["    DATE"] == date]
        temperature = df_row.get('   TG') / 10
        data_row = {
            "Date":df_row.get('    DATE').squeeze(),
            "Station_ID":int(df_row.get('STAID').squeeze()),
            "Temp":float(temperature)
        }
        return data_row
    
    elif len(date) == 4:

        #Adding a column year
        df_row.loc[:,'Year'] = df_row['    DATE'].dt.year

        #Filtre for the Year
        df_data_date = df_row.loc[df_row['Year'] == int(date)]

        #Loop to regroupe data in a list
        for i,row in df_data_date.iterrows():
            data_row = {
            "Date":row.get('    DATE'),
            "Station_ID":row.get('STAID'),
            "Temp":row.get('   TG') / 10
            }
            data.append(data_row)
        return data


def get_station_main_file():
    df = pd.read_csv('src\data_small\stations.txt', skiprows=17)
    return df





