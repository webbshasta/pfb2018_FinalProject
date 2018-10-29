#!/usr/bin/env python3
import random
Veeple2 = {
          'ID' : 2,
          'Sex' : 'Y',
          'mGenome' : ['A2','B2'],
          'pGenome' : ['A2','B2'],
          'Base Fitness': 10,
          'Fitness' : 10,
          'Behavior': ''
          }
def behavior_initializer(veeple):
    behavior_options = ['fight','fuck','forage']
    option_index = random.randint(0,len(behavior_options)-1)
    behavior = behavior_options[option_index]
    veeple['Behavior'] =behavior
    return(veeple)

        
