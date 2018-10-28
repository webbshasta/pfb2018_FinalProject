#!/usr/bin/env python3

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
          'Sex' : 'Y',
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
print("The sexes are:",Veeple1['Sex'], Veeple2['Sex'])

#def VeepleBabyMaker():
if Veeple1['Sex'] == Veeple2['Sex']: #need one of each--no VeepleBaby
    print("nice...recreation but no procreation, if we don't get along...consequences")

elif random.randint(1,2) == 1:  #assign sex of Veeplebaby
    VeepleBabyMaker = 'Y'
            #VeepleBaby = VeepleMaker(ID = '', Sex = SexY , mgenome = [], pgenome = [], base_fitness = 0)
    print(VeepleBabyMaker)
    print('Congratulations!  Veeplerents of a bouncing baby Veeple')
else:  #making Veeplebaby
    VeepleBabyMaker = 'X'
            #VeepleBaby = VeepleMaker(ID = '', Sex = SexX , mgenome = [], pgenome = [], base_fitness = 0)
    print(VeepleBabyMaker)
    print('Congratulations!  Veeplerents of a bouncing baby Veeple')
    #return VeepleBabyMaker #which sex
