import os
import sys
import json

import numpy as np
import pandas as pd


arr = ['population_density', 'median_household_income', 'Male', 'Female', 'White', 'Black Or African American', 'American Indian Or Alaskan Native', 'Asian', 'Native Hawaiian & Other Pacific Islander', 'Other Race', '< $25,000', '$25,000-$44,999', '$45,000-$59,999', '$60,000-$99,999', '$100,000-$149,999', '$150,000-$199,999', '$200,000+', 'Less Than High School Diploma', 'High School Graduate', "Associate's Degree", "Master's Degree", 'Professional School Degree', 'Doctorate Degree', 'Enrolled In Public School', 'Enrolled In Private School', 'Not Enrolled In School', 'April', 'August', 'December', 'February', 'January', 'July', 'June', 'March', 'May', 'November', 'October', 'September', 'day1', 'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19', 'day2', 'day20', 'day21', 'day22', 'day23', 'day24', 'day25', 'day26', 'day27', 'day28', 'day29', 'day3', 'day30', 'day31', 'day4', 'day5', 'day6', 'day7', 'day8', 'day9', 'year']

# dat = pd.DataFrame(columns=arr)

flagged = []

for i in range(len(arr)):
    col = arr[i]
    print(col)

    flag = input()

    flagged.append({
        'key': arr[i],
        'flag': flag
    })

print(flagged)

with open('flagged_cols.json', 'w+') as fp:
    json.dump(flagged, fp)
