from uszipcode import SearchEngine
import pickle
from sklearn.neural_network import MLPClassifier as mlp
from sklearn import preprocessing
import numpy as np


def encoded_dict(zipcode, date):

    search = SearchEngine(simple_zipcode=False).by_zipcode(zipcode)

    #keys_to_remove.extend (['timezone', 'area_code_list', 'polygon', 'population_by_age', 'population_by_gender', 'population_by_race', 'head_of_household_by_age'])
    keys_to_include = [
        "population_density",
        "population_by_gender",
        "population_by_race",
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
        "day31"]

    return_dict = {}

    for index, feature in enumerate(search.keys()):
        if feature in keys_to_include:
            #return_dict[str(index) + feature] = search.values()[index]
            parent_key = str(search.keys()[index])

            #print (search.values()[index])
            if type(search.values()[index]) == list:
                diction = list((search.values()[index])[0].values())[1]
            else:
                return_dict[search.keys()[index]] = search.values()[index]
                continue

            for each_dict in diction:
                combined_key = parent_key + ' - ' + str(each_dict['x'])
                return_dict[combined_key] = each_dict['y']

    dates = date.split('/')

    for index, time in enumerate(time_features):
        return_dict[time_features[index]] = 0

        if (index == int(dates[0])-1):
            return_dict[time_features[index]] = 1
        elif (index == int(dates[1])+11):
            return_dict[time_features[index]] = 1

    return return_dict


order_dict = []


def onehot(pickle_to_read, zip, date):

    with open(pickle_to_read, 'rb') as picker_reader:
        model = pickle.load(picker_reader)

    result_dict = encoded_dict(zip, date)

    del result_dict["employment_status - Worked Full-time With Earnings"]
    del result_dict["employment_status - Worked Part-time With Earnings"]
    del result_dict["employment_status - No Earnings"]
    del result_dict["educational_attainment_for_population_25_and_over - Bachelor's Degree"]
    del result_dict["population_by_race - Two Or More Races"]

    # print(result_dict, len(result_dict))
    X = np.nan_to_num(np.array([list(result_dict.values())]))
    result_prob = model.predict_proba(X)
    return result_prob

if __name__ == '__main__':
    prob = onehot("model.pkl", "94577", "10/20/2019")
    print(prob)
