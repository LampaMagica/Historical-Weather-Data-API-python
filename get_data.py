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

#Get The Row
def get_row_by_date(date,id):
    df = get_file(id)
    df_row = df.loc[df["    DATE"] == date]
    return df_row.iloc[0].to_dict()







