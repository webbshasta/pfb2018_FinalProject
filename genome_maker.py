#!/usr/bin/env python3

#=============
# Defining function for starter genome
#==============

# This function requires the Veeple1 and Veeple2 dictionaries. These dictionaries will have all keys filled
# except for the 'mGenome' and the 'pGenome'.

import random

# Alleles score

#AlleleA_fit_dict = {
                    #'A1': '5'
                    #'A2': '2'
                    #'A3': '-1'
                    #'A4': '3'
                    #}
#AlleleB_fit_dict = {
                    #'B1': '0'
                    #'B2': '1'
                    #'B3': '-2'
                    #'B4': '4'
                    #}

# Eve
Veeple1 = {
          'ID':1,
          'Sex':'X',
          'mGenome':[],
          'pGenome':[],
          'Base Fitness':10,
          'Fitness':10
          }

# Adam
Veeple2 = {
          'ID':2,
          'Sex':'Y',
          'mGenome':[],
          'pGenome':[],
          'Base Fitness':10,
          'Fitness':10
          }

allelesGeneA = ['A1', 'A2', 'A3', 'A4']
allelesGeneB = ['B1', 'B2', 'B3', 'B4']

def starterGenome(alleles1, alleles2, Veeple):
    randomIndex1 = random.randint(0, len(alleles1) -1)
    randomIndex2 = random.randint(0, len(alleles2) - 1)
    randomIndex3 = random.randint(0, len(alleles1) -1)
    randomIndex4 = random.randint(0, len(alleles2) - 1)
    Veeple['mGenome'].append(alleles1[randomIndex1])
    Veeple['pGenome'].append(alleles1[randomIndex2])
    Veeple['mGenome'].append(alleles2[randomIndex3])
    Veeple['pGenome'].append(alleles2[randomIndex4])

    return(Veeple)

print(starterGenome(allelesGeneA, allelesGeneB, Veeple1))
