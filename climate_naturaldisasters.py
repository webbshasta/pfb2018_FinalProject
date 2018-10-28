#!/usr/bin/env python3
# Functions that return penalties for environmental climate randomly.
#get_climate takes a randomly generated number and returns a penatly score for too hot or too cold climate_score
#get_naturaldisasters takes a randomly generated number and determines if a natural disaster happens (20% of the time)
#depending on the climate, which type of natural disaster happens, and assigns a penalty if a natural disaster occurs.

import random

climate = random.randint(1,10) #picks a random number to choose climate
natural_disaster = random.randint(1,10)# picks a random number to check if a natural disaster occurs

population_amount = 10 #test case. Remove when in final form.


def get_climate(climate):
    if climate >= 3 and climate <=7:
        climate_score = 0 # no penalty in temperate climate
        print('Climate: Temperate', climate)
    elif climate == (1):
        climate_score = 3
        print('Climate: Arctic tundra-level cold', climate)
    elif climate == (2):
        climate_score = 2
        print('Climate: Freezing', climate)
    elif climate == (3):
        climate_score = 1
        print('Climate: Uncomfortably cold', climate)
    elif climate == (8):
        climate_score = 1
        print('Climate: Uncomfortably hot', climate)
    elif climate == (9):
        climate_score = 2
        print('Climate: Really hot', climate)
    elif climate == (10):
        climate_score = 3
        print('Climate: You are on fire', climate)

    return(climate_score)

def get_naturaldisasters(natural_disaster,climate):
    #disaster dictionaries with associated penalty values
    disasterdict_general = {'sinkhole': 1, 'earthquake': 2, 'flood': 3, 'tornado':3, 'volcanic eruption':4, 'meteor strike':4}
    disasterdict_cold = {'avalanch': 2, 'blizzard': 2}
    disasterdict_hot = {'sandstorm': 1, 'drought':1, 'hurricane':3,}

    #key list of disasters that can be iterated over, "dict.keys" returns tuples
    disaster_cold_list = list(disasterdict_cold)
    disaster_hot_list = list(disasterdict_hot)
    disaster_general_list = list(disasterdict_general)

    #initializing natural_disaster_score, in the case that there are no disasters
    natural_disaster_score = 0

    if natural_disaster >8: #20% chance of a natural disaster at 8 (9 + 10 are valid)
        if climate <=3: #if the climate is cold use cold dictionary
            list_index = random.randint(0,len(disaster_cold_list)-1) #index to randomly choose the disaster
            natural_disaster_type = disaster_cold_list[list_index]
            natural_disaster_score = disasterdict_cold[natural_disaster_type]
            print("Natural disaster:", natural_disaster_type)

        elif climate >=7: #if the climate score is hot use hot dictionary
            list_index = random.randint(0,len(disaster_hot_list)-1)
            natural_disaster_type = disaster_hot_list[list_index]
            natural_disaster_score = disasterdict_hot[natural_disaster_type]
            print("Natural disaster:", natural_disaster_type)
        else: #otherwise climate score is temperate
            list_index = random.randint(0,len(disaster_general_list)-1)
            natural_disaster_type = disaster_general_list[list_index]
            natural_disaster_score = disasterdict_general[natural_disaster_type]
            print("Natural disaster:", natural_disaster_type)
    else:
        print("No natural disasters")
        natural_disaster_type = 'None'

    print("Natural disaster score:", natural_disaster_score)
    return(natural_disaster_score) #this value corresponds to the penalty value, or 0

def get_populationhealth(climate, population_amount):
    
    diseasedict = {'measles': 3, 'typhoid': 2, 'diptheria':3, 'cholera':1, 'chicken pox': 0, 'influenza': 2, 'smallpox': 5}
    disease_list = list(diseasedict)#because just grabbing the keys with d.keys() wont work
    
    #initializing the disease score, in the case there are no diseases
    disease_score = 0

    disease = random.randint(1,10) #sets the counter for if a disease happens

    if population_amount >= 50:
        if disease >7: #30% chance of disease due do population pollution + climate
            list_index = random.randint(0,len(disease_list)-1) #index to randomly choose the disease
            disease_type = disease_list[list_index]
            disease_score = diseasedict[disease_type]
            print("Disease:", disease_type)
        else:#What happens if you have a larger population, but the disease counter doesn't give you a disease
            disease_type = 'None'
            print("Congratulations! Even though you have a lot of Veeples, the polution hasn't affected your health too much.")

    elif disease >8: #20% chance of disease due to climate and no population effects
        list_index = random.randint(0,len(disease_list)-1) #index to randomly choose the disease
        disease_type = disease_list[list_index]
        disease_score = diseasedict[disease_type]
        print("Disease:", disease_type)

    else: #otherwise no diseases affect the population
        disease_type= 'None'
        print("congratulations, your population is relatively disease free! Good work on vaccinations.")

    print("Disease score:", disease_score)
    return(disease_score)

get_climate(climate)
get_naturaldisasters(natural_disaster, climate)
get_populationhealth(climate, population_amount)
