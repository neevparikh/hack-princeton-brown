import plotly
import plotly.plotly as plt
import plotly.graph_objs as go
import cufflinks as cf
import pandas as pd
import os

plotly.tools.set_credentials_file(username = "sonny3690", api_key = "IDjmPDbFVJV1HC5M8pnh")

def read_csv (city, state):
    file_path = os.getcwd()[:-6] + '/scraper/gun_data.csv'
    csv_df = pd.read_csv(file_path, error_bad_lines=False)
    csv_df = csv_df.loc[:, :]

    csv_df.index = pd.to_datetime (csv_df['date'])  
    del csv_df['date']

    curr_df = csv_df[csv_df['city_or_county'] == city]

    trace1 = go.Bar(
        
    )



    
    #csv_df[csv_df['city_or_county'] == city]['n_injured'].iplot (title = 'Time Series Gun Injury Plot for ' + city)
    
read_csv('New Orleans', 'Louisiana')