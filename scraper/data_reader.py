import pandas as pd
import numpy as np
import uszipcode as uz 
search = uz.SearchEngine(simple_zipcode=False)

spatial_features = [
    "population_density",
    "population_by_age",
    "population_by_gender",
    "population_by_race",
    "median_household_income",
    "employment_status",
    "household_income",
    "educational_attainment_for_population_25_and_over",
    "school_enrollment_age_3_to_17"
]

temporal_features = [
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
    i = 0
    for c, s in zip(cities, states):
        print(i)
        i += 1
        results = search.by_city_and_state(c, s)
        row = {}
        if results == []:
            continue
        else:
            result = results[0].to_dict()
            for k, v in result.items():
                if v == None:
                    continue
                elif k in spatial_features:
                    if type(v) == list:
                        d_sub = v[0]
                        for d_sub2 in d_sub["values"]:
                            k_sub2 = d_sub2["x"]
                            v_sub2 = d_sub2["y"]
                            row[k_sub2] = v_sub2
                    elif type(v) == int or type(v) == float:
                        row[k] = v
        df_list.append(row)
    return pd.DataFrame(df_list)

def time_features(date):
    init = {k:0 for k in temporal_features}
    year = int(date.rsplit(',')[1].lstrip(' '))
    day = "day"+date.rsplit(',')[0].rsplit(' ')[1]
    month = ''.join([c for c in date if c.isalpha()])
    for k, v in init.items():
        if month == k or day == k:
                init[k] = 1
        elif k == "year":
                init[k] = year  
    return init

def get_time_features(dates):
    df_list = []
    for k, v in dates.iteritems():
        if v == "date" or type(v) != str:
            continue
        df_list.append(time_features(v))
    return pd.DataFrame(df_list)

def valid_years(y):
    if y < 2016:
        return str(y)
    else:
        return "2015"

def create_train():
    incident_df = pd.read_csv("gun_data.csv", names=["date", "city", "state", "injured", "dead"]).sample(5000, random_state=5)
    spat_feat = get_spat_features(incident_df["city"], incident_df["state"])
    time_feat = get_time_features(incident_df["date"])
    df = pd.concat([spat_feat, time_feat], axis=1).dropna()

    # print(df.loc(['2014']))

    # i = 0
    # pop_y = []

    # while i < len(df.index.get_values()):
    #     r = df.iloc[i]
    #     y = int(r['year'])
    #     pop_y.append(r.loc[valid_years(y)])
    #     i += 1
    
    df["population"] = df["Male"] + df["Female"]

    # del df["2005"]
    # del df["2006"]
    # del df["2007"]
    # del df["2008"]
    # del df["2009"]
    # del df["2010"]
    # del df["2011"]
    # del df["2012"]
    # del df["2013"]
    # del df["2014"]
    # del df["2015"]

    df.to_csv("train_feat_df.csv", index=False)

create_train()