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

        
        

merge_data()


