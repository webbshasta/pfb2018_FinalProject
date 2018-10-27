#!/usr/bin/env python3

#=============
# Defining function for starter genome
#================

# This function requires the Veeple1 and Veeple2 dictionaries. These dictionaries will have all keys filled
# except for the 'mGenome' and the 'pGenome'.

import random

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

def starterGenome(alleles1, alleles2):
    randomIndex = random.randint(0, len(alleles1) - 1)
    Veeple1['mGenome'].append(alleles1[randomIndex])
    #Veeple1['pGenome'].append(alleles1[random.randint(0, int(len(alleles1)))])
    #Veeple2['mGenome'].append(alleles1[random.randint(0, int(len(alleles1)))])
    #Veeple2['pGenome'].append(alleles1[random.randint(0, int(len(alleles1)))])
    #Veeple1['mGenome'].append(alleles2[random.randint(0, int(len(alleles2)))])
    #Veeple1['pGenome'].append(alleles2[random.randint(0, int(len(alleles2)))])
    #Veeple2['mGenome'].append(alleles2[random.randint(0, int(len(alleles2))])
    #Veeple2['pGenome'].append(alleles2[random.randint(0, int(len(alleles2))])
    return(Veeple1, Veeple2)

print(starterGenome(allelesGeneA, allelesGeneB))
