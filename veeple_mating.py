#!/usr/bin/env python3

#import VeepleBooper
#import genome_maker
import random

# Model Veeples for testing

# Eve

Veeple1 = {
          'ID' : 1,
          'Sex' : 'X',
          'mGenome' : ['A1','B1'],
          'pGenome' : ['A1','B1'],
          'Base Fitness' : 10,
          'Fitness' : 10
          }

# Adam

Veeple2 = {
          'ID' : 2,
          'Sex' : 'X',
          'mGenome' : ['A2','B2'],
          'pGenome' : ['A2','B2'],
          'Base Fitness': 10,
          'Fitness' : 10
          }

# ID = <int>
# Sex = <str>
# Genome = <list of str>
# Base Fitness = <int>
# Fitness = <int>


#Veeple1['Sex'] = X #Veeples need to be of different sex to procreate, but they might do something else
#Veeple2['Sex'] = Y

def VeepleMaker(ID, Sex, mgenome, pgenome, base_fitness):
        VeepleBaby= {'ID': ID, 'Sex': Sex, 'Maternal Genome': mgenome, 'Paternal Genome': pgenome, 'Base Fitness': base_fitness}

def VeepleMate(Veeple1, Veeple2):

    #VeepleBaby= {}

    if Veeple1['Sex'] == Veeple2['Sex']:  #need one of each--test
        print("nice...recreation but no procreation, if we don't get along...consequences")

    elif random.randint(1,2) == 1:  #assign sex of Veeplebaby
        SexY = 'Y'
        VeepleBaby = VeepleMaker(ID = '', Sex = SexY , mgenome = [], pgenome = [], base_fitness = 0)

    else:  #making Veeplebaby
        SexX = 'X'
        VeepleBaby = VeepleMaker(ID = '', Sex = SexX , mgenome = [], pgenome = [], base_fitness = 0)

    return VeepleBaby

print(VeepleBaby)


VeepleMate(Veeple1, Veeple2)
#print('Congratulations!  Veeplerents of a bouncing baby Veeple')
