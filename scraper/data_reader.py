import pandas
import os
import csv


def rename_files ():
    for csv_file_name in os.listdir("."):
        os.rename(csv_file_name, csv_file_name.replace(".","_"))
        print ('stripped!')


def merge_data ():

        df_list = []
        for csv_file_name in os.listdir("."):
                df_list.append(pandas.read_csv(csv_file_name,  error_bad_lines=False))
        total_file = pandas.concat (df_list)

        #reorder columns
        total_file = total_file[['date', 'city_or_county', 'state', 'n_injured', 'n_killed']]
        
        total_file.to_csv('gun_data.csv', index = False)
        
def add_income_features():
        income_df = pandas.read_csv ('zip_income.csv', error_bad_lines=False, encoding = "ISO-8859-1")
        incident_df = pandas.read_csv ('gun_data.csv')
        zip_code_look_up = pandas.read_csv('free-zipcode-database.csv', error_bad_lines = False)
        zip_code_look_up = zip_code_look_up[['Zipcode', 'LocationText', 'Lat', 'Long']].dropna()
        zip_code_look_up['City'], zip_code_look_up['State Code'] = zip_code_look_up['LocationText'].str.split(',', 1).str
        print(income_df)

        

        #print (incident_df)




add_income_features()

