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

VeepleBaby = {
          'ID' : 0,
          'Sex' : '',
          'mGenome' : [],
          'pGenome' : [],
          'Base Fitness': 0,
          'Fitness' : 0
          }

# ID = <int>
# Sex = <str>
# Genome = <list of str>
# Base Fitness = <int>
# Fitness = <int>
#print("The sexes are:",Veeple1['Sex'], Veeple2['Sex'])

#def VeepleBabyMaker():
def VeepleMatingTest(VeepDict1, VeepDict2, VeepDictBaby):

    if (VeepDict1['Fitness'] > 3 and VeepDict2['Fitness'] > 3):
        if VeepDict1['Sex'] == VeepDict2['Sex']:
            print('Cannot mate.')
        elif random.randint(1,2) == 1:  #assign sex of Veeplebaby
            VeepleSex = 'Y'
            VeepDictBaby['Sex'] = VeepleSex
        else:  #making Veeplebaby
            VeepleSex = 'X'
            VeepDictBaby['Sex'] = VeepleSex
    else:
        print('Fitness is too low to mate.')
    return VeepDictBaby

    #return(VeepDict1, VeepDict2)

#def VeepleSexAssign(VeepDict1, VeepDict2, VeepDictBaby):

    #if VeepDict1['Sex'] == VeepDict2['Sex']: #need one of each--no VeepleBaby
        #print("nice...recreation but no procreation, if we don't get along...consequences")
        #print('Cannot mate.')
    #elif random.randint(1,2) == 1:  #assign sex of Veeplebaby
    #VeepleSex = 'Y'
        #VeepDictBaby['Sex'] = VeepleSex#print(VeepleSex)
            #print('Congratulations!  Veeplerents of a bouncing baby Veeple')
    #else:  #making Veeplebaby
    #    VeepleSex = 'X'
    #    VeepDictBaby['Sex'] = VeepleSex
        #print(VeepleSex)
            #VeepleBaby = VeepleMaker(ID = '', Sex = SexX , mgenome = [], pgenome = [], base_fitness = 0)
            #print(VeepleBabyMaker)
            #print('Congratulations!  Veeplerents of a bouncing baby Veeple')
    #return(VeepDictBaby)

#VeepleSexAssign(Veeple1, Veeple2)                #return VeepleBabyMaker #which sex
#
#VeepleMatingTest(Veeple1, Veeple2)
