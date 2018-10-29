#!/usr/bin/env python3
import random
#Veeple1 = {
#          'ID' : 1,
#          'Sex' : 'X',
#          'mGenome' : ['A1','B1'],
#          'pGenome' : ['A1','B1'],
#          'Base Fitness' : 10,
#          'Fitness' : 10
#          }
Veeple2 = {
          'ID' : 2,
          'Sex' : 'Y',
          'mGenome' : ['A2','B2'],
          'pGenome' : ['A2','B2'],
          'Base Fitness': 10,
          'Fitness' : 10,
          'Behavior': ''
          }
#veeplecensus = [Veeple1, Veeple2]

#method which takes a single veeple and assigns a dictionary randomly. current default fuck.
def behavior_initializer(veeple):
    behavior_options = ['fight','fuck','forage']
    option_index = random.randint(0,len(behavior_options)-1)
    behavior = behavior_options[option_index]
    veeple['Behavior'] =behavior
    return(veeple)

        
#behavior_initializer(veeplecensus)
