import os
import sys
import json

import numpy as np
import pandas as pd
from random import randint
import math

arr = ['Male', 'Female', 'White', 'Black Or African American', 'American Indian Or Alaskan Native', 'Asian', 'Native Hawaiian & Other Pacific Islander',
       'Other Race', 'Two Or More Races', 'Husband Wife Family Households', 'Single Guardian', 'Singles', 'Singles With Roommate', 'Households Without Kids',
       'Households With Kids', 'Worked Full-time With Earnings', 'Worked Part-time With Earnings', 'No Earnings', '< $25,000', '$25,000-$44,999',
       '$45,000-$59,999', '$60,000-$99,999', '$100,000-$149,999', '$150,000-$199,999', '$200,000+', 'Less Than High School Diploma', 'High School Graduate',
       "Associate's Degree", "Bachelor's Degree", "Master's Degree", 'Professional School Degree', 'Doctorate Degree', 'Enrolled In Public School',
       'Enrolled In Private School', 'Not Enrolled In School', 'April', 'August', 'December', 'February', 'January', 'July', 'June', 'March', 'May',
       'November', 'October', 'September', 'day1', 'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19', 'day2',
       'day20', 'day21', 'day22', 'day23', 'day24', 'day25', 'day26', 'day27', 'day28', 'day29', 'day3', 'day30', 'day31', 'day4', 'day5', 'day6', 'day7',
       'day8', 'day9', 'year']

dat = pd.DataFrame(columns=arr)

flagged = []

with open('flagged_cols.json', 'r') as fp:
    flagged = json.load(fp)

train_feat = pd.read_csv("../scraper/train_feat_df.csv")

for demo in flagged:
    demo["mean"] = train_feat[demo["key"]].mean()
    demo["std"] = train_feat[demo["key"]].std()
    demo["max"] = train_feat[demo["key"]].max()
    demo["min"] = train_feat[demo["key"]].min()

for i in range(5000):
    row = []
    for feat in flagged:
        if feat["flag"] == "y":
            row.append(abs(randint(
                int(round(feat["mean"])) + int(round(feat["std"] / 2)), int(round(feat["max"])))))
        elif feat["flag"] == "n":
            row.append(abs(
                randint(int(round(feat["mean"])) - int(round(feat["std"] / 2)), int(round(feat["mean"])) + int(round(feat["std"])))))
        else:
            row.append(abs(
                randint(int(round(feat["min"])), int(round(feat["max"])))))

    dat.loc[i] = row
    if (i % 100 == 0):
        print(i)

print(dat)
dat.to_csv("fake.csv", ",")
