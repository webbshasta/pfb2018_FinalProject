#!/usr/bin/env python3


Veeple1 = {
          'ID' : 1,
          'Sex' : 'X',
          'mGenome' : ['A1','B1'],
          'pGenome' : ['A1','B1'],
          'Base Fitness' : 10,
          'Fitness' : 10
          }

Veeple2 = {
          'ID' : 2,
          'Sex' : 'Y',
          'mGenome' : ['A2','B2'],
          'pGenome' : ['A2','B2'],
          'Base Fitness': 10,
          'Fitness' : 10
          }

testVeeplelist = [Veeple1, Veeple2]

#method which counts the total veeple population from input: census list
#the length of elements in the list is the number of people added to the census
def veeple_population_count(veeplecensus):
    total_pop = len(veeplecensus)
    print('Total veeple population:',total_pop)
    return (total_pop)

#method which counts % of male and female veeples from the total census list
#input: census list
def veeple_percent_genders(veeplecensus):
    total_female = 0
    total_male = 0

    for individual in veeplecensus: #for each dictionary in the veeple census that correspons to a person
        if individual['Sex'] == 'X':
            total_female = total_female + 1
        elif individual['Sex'] == 'Y':
            total_male = total_male + 1
        else:
            print("ERROR. something wrong with the census. cant count genders.")
            break
    print(total_female, total_male)


#method which counts total alleic frequencies in the census with input census list.
def veeple_allelic_frequencies(veeplecensus):
    allelic_count_dict = {}#initializing the dictionary that has the total counts / census
    allelic_frequencies_dict = {}#initializing the frequencies based on total population
    total_veeples = len(veeplecensus)
    total_alleles = total_veeples *2 #this is because we have diploid organisms.

    for individual in veeplecensus: #for each dictionary in the veeple census that corresponds to a person
        for allele in individual['mGenome']:#cataloging the maternal genome list
            if allele in allelic_count_dict:
                allelic_count_dict[allele] += 1
            else:
                allelic_count_dict[allele] = 1

        for allele in individual['pGenome']: #cataloging the paternal genome list
            if allele in allelic_count_dict:
                allelic_count_dict[allele] +=1
            else:
                allelic_count_dict[allele] = 1

    for allele in allelic_count_dict:
        

    print(allelic_count_dict)


veeple_population_count(testVeeplelist)
veeple_percent_genders(testVeeplelist)
veeple_allelic_frequencies(testVeeplelist)
