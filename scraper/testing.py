arr_1 = ['April',
         'August', 'December', 'February', 'January', 'July', 'June', 'March',
         'May', 'November', 'October', 'September', 'day1', 'day10', 'day11',
         'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19',
         'day2', 'day20', 'day21', 'day22', 'day23', 'day24', 'day25', 'day26',
         'day27', 'day28', 'day29', 'day3', 'day30', 'day31', 'day4', 'day5',
         'day6', 'day7', 'day8', 'day9']

arr_3 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8', 'day9',
         'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19', 'day20', 'day21', 'day22', 'day23', 'day24', 'day25', 'day26', 'day27', 'day28', 'day29', 'day30', 'day31']

final = []

for word in arr_3:
    flag = False
    for check in arr_1:
        if check in word:
            flag = True
            break
    if not flag:
        final.append(word)

print(final)
print(len(arr_3), len(arr_1))


arr_2 = ['population_density', 'median_household_income', 'population_by_gender - Male', 'population_by_gender - Female',
         'population_by_race - White', 'population_by_race - Black Or African American', 'population_by_race - American Indian Or Alaskan Native',
         'population_by_race - Asian', 'population_by_race - Native Hawaiian & Other Pacific Islander', 'population_by_race - Other Race',
         'employment_status - Worked Full-time With Earnings', 'employment_status - Worked Part-time With Earnings',
         'employment_status - No Earnings', 'household_income - < $25,000', 'household_income - $25,000-$44,999', 'household_income - $45,000-$59,999',
         'household_income - $60,000-$99,999', 'household_income - $100,000-$149,999', 'household_income - $150,000-$199,999', 'household_income - $200,000+',
         'educational_attainment_for_population_25_and_over - Less Than High School Diploma', 'educational_attainment_for_population_25_and_over - High School Graduate'
         "educational_attainment_for_population_25_and_over - Associate's Degree", "educational_attainment_for_population_25_and_over - Bachelor's Degree",
         "educational_attainment_for_population_25_and_over - Master's Degree", 'educational_attainment_for_population_25_and_over - Professional School Degree',
         'educational_attainment_for_population_25_and_over - Doctorate Degree', 'school_enrollment_age_3_to_17 - Enrolled In Public School',
         'school_enrollment_age_3_to_17 - Enrolled In Private School', 'school_enrollment_age_3_to_17 - Not Enrolled In School', 'January', 'February',
         'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6',
         'day7', 'day8', 'day9', 'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19', 'day20', 'day21', 'day22', 'day23',
         'day24', 'day25', 'day26', 'day27', 'day28', 'day29', 'day30', 'day31']
# print(len(arr_2))
