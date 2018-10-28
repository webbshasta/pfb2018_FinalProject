#!/usr/bin/env python3

#=============
# Defining function for starter genome
#==============

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

# Alleles list
allelesGeneA = ['A1', 'A2', 'A3', 'A4']
allelesGeneB = ['B1', 'B2', 'B3', 'B4']
allelesGeneC = ['C1', 'C2', 'C3', 'C4']
allelesGeneD = ['D1', 'D2', 'D3', 'D4']
allelesGeneE = ['E1', 'E2', 'E3', 'E4']
# Alleles score
# Defining base fitness based on alleles score

Allele_fit_dict = {
                    'A1':5,
                    'A2':2,
                    'A3':1,
                    'A4':3,
                    'B1':0,
                    'B2':1,
                    'B3':-2,
                    'B4':4,
                    'C1':2,
                    'C2':2,
                    'C3':4,
                    'C4':0,
                    'D1':-5,
                    'D2':-3,
                    'D3':-4,
                    'D4':0,
                    'E1':5,
                    'E2':3,
                    'E3':5,
                    'E4':2
                    }
def base_fitness(Veeple):
    mGenome = Veeple['mGenome']
    pGenome = Veeple['pGenome']
    base_fitness = 0
    for allele in mGenome:
        if allele in Allele_fit_dict:
            base_fitness += Allele_fit_dict[allele]
    for allele in pGenome:
        if allele in Allele_fit_dict:
            base_fitness += Allele_fit_dict[allele]

    return base_fitness
BF = base_fitness(Veeple1)
print(BF)

def starterGenome(alleles1, alleles2, alleles3, alleles4, alleles5,Veeple):
    randomIndex1 = random.randint(0, len(alleles1) -1)
    randomIndex2 = random.randint(0, len(alleles2) - 1)
    randomIndex3 = random.randint(0, len(alleles1) -1)
    randomIndex4 = random.randint(0, len(alleles2) - 1)
    randomIndex5 = random.randint(0, len(alleles3) -1)
    randomIndex6 = random.randint(0, len(alleles3) -1)
    randomIndex7 = random.randint(0, len(alleles4) -1)
    randomIndex8 = random.randint(0, len(alleles4) -1)
    randomIndex9 = random.randint(0, len(alleles5) -1)
    randomIndex10 = random.randint(0, len(alleles5) -1)
    Veeple['mGenome'].append(alleles1[randomIndex1])
    Veeple['pGenome'].append(alleles1[randomIndex2])
    Veeple['mGenome'].append(alleles2[randomIndex3])
    Veeple['pGenome'].append(alleles2[randomIndex4])
    Veeple['mGenome'].append(alleles3[randomIndex5])
    Veeple['pGenome'].append(alleles3[randomIndex6])
    Veeple['mGenome'].append(alleles4[randomIndex7])
    Veeple['pGenome'].append(alleles4[randomIndex8])
    Veeple['mGenome'].append(alleles5[randomIndex9])
    Veeple['pGenome'].append(alleles5[randomIndex10])
    Base_Fitness = 0
    Base_Fitness = base_fitness(Veeple)
    Veeple['Base Fitness'] = Base_Fitness
    Fitness = 0
    Veeple['Fitness'] = Fitness

    return(Veeple)

#print(starterGenome(allelesGeneA, allelesGeneB, allelesGeneC, allelesGeneD, allelesGeneE, Veeple1))

