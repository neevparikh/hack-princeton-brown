from uszipcode import SearchEngine


def encoded_dict (zipcode, date):
        
        search = SearchEngine(simple_zipcode=False).by_zipcode (zipcode)
        
        keys_to_remove = search.keys()[:-20]

        keys_to_remove.extend (['timezone', 'area_code_list', 'polygon', 'population_by_age', 'population_by_gender', 'population_by_race', 'head_of_household_by_age'])
        
        return_dict = {}


        for index, feature in enumerate (search.keys()):
                if feature not in keys_to_remove:
                        #return_dict[str(index) + feature] = search.values()[index]
                        parent_key = str(index) + search.keys()[index]
                        print (parent_key)
                        diction = list((search.values()[index])[0].values())[1]
                        
                        for each_dict in diction:
                                combined_key = parent_key + ' - ' + each_dict['x']
                                print (combined_key, each_dict['y'])
                                return_dict[combined_key] = each_dict['y']
                        
                        



                        # for each_dict in search.values()[index]:                                
                        #         #diction = list(each_dict.values())[1][0]
                        #         diction = list(each_dict.values())[1][0]
                        #         print (diction)
                        #         values = list(diction.values())
                                
                        #         return_dict[values[0]] = values[1]

                                
                                #print(list(diction.values()))

                        #print((search.values()[index]).keys())

                        #print (search.get("Enrolled in Private School", "no animal available"))
                        
                                #print(search.values()[inde


        print (return_dict)

                                
                
        #print(return_dict[return_dict.keys()[]]
        #print (return_dict['population_by_year'])

        dates = date.split ('/')
        date_array = [0] * 12
        date_array[int(dates[0])-1] = 1
        

        date_array = [0] * 12
        date_array[int(dates[0])-1] = 1

        print(date_array)
        