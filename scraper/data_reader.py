import pandas as pd
import numpy as np
import uszipcode as uz 
search = uz.SearchEngine(simple_zipcode=False)

spatial_features = [
        "population_density",
        "population_by_year",
        "population_by_age",
        "population_by_gender",
        "population_by_race",
        "families_vs_singles",
        "households_with_kids",
        "median_household_income",
        "employment_status",
        "household_income",
        "educational_attainment_for_population_25_and_over",
        "school_enrollment_age_3_to_17"
]

time_features = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
        "year",
        "day1",
        "day2",
        "day3",
        "day4",
        "day5",
        "day6",
        "day7",
        "day8",
        "day9",
        "day10",
        "day11",
        "day12",
        "day13",
        "day14",
        "day15",
        "day16",
        "day17",
        "day18",
        "day19",
        "day20",
        "day21",
        "day22",
        "day23",
        "day24",
        "day25",
        "day26",
        "day27",
        "day28",
        "day29",
        "day30",
        "day31"
]

def get_spat_features(cities, states):
        df_list = []
        for c, s in zip(cities, states):
                results = search.by_city_and_state(c, s)
                row = {}
                if results == []:
                        continue
                else:
                        print(results)
                        result = results[0].to_dict()
                        for k, v in result.items():
                                if v == None:
                                        row[k] = v
                                elif k in spatial_features:
                                        if type(v) == dict:
                                                for k_sub, v_sub in v.items():
                                                        for k_sub2, v_sub2 in v_sub.items():
                                                                row[k_sub2] = v_sub2
                                        elif type(v) == int or type(v) == float:
                                                row[k] = v
                df_list = df_list.append(row)
        return pd.DataFrame(df)

def time_feat(date):
        init = {k:0 for k in time_features}
        month = ''.join([c for c in date if c.isalpha()])
        year = int(date.rsplit(',')[1].lstrip(' '))
        day = "day"+date.rsplit(',')[0].rsplit(' ')[1]
        for k, v in init:
                if month == k or day == k:
                        init[k] = 1
                elif k == "year":
                        init[k] = v
        return init


def get_time_features(dates):
        return dates.apply(time_feat, result_type="expand")

def create_train():
        incident_df = pd.read_csv("gun_data.csv", names=["date", "city", "state", "injured", "dead"])
        spat_feat = get_spat_features(incident_df["city"], incident_df["state"])
        time_feat = get_time_features(incident_df["date"])
        res_df = spat_feat.concat(time_feat, axis=1)
        res_df.to_csv("train_feat_df.csv", index=False)

create_train()