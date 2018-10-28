#!/usr/bin/env python3
#Veeple1 = {
#          'ID' : 1,
#          'Sex' : 'X',
#          'mGenome' : ['A1','B1'],
#          'pGenome' : ['A1','B1'],
#          'Base Fitness' : 10,
#          'Fitness' : 10
#          }
#Veeple2 = {
#          'ID' : 2,
#          'Sex' : 'Y',
#          'mGenome' : ['A2','B2'],
#          'pGenome' : ['A2','B2'],
#          'Base Fitness': 10,
#          'Fitness' : 10
#          }
#veeplecensus = [Veeple1, Veeple2]

#method which takes the veeple census, and one by one, assigns a behavior to each veeple.
def behavior_initializer(veeplecensus):
    behavior_options = ['fight','fuck','family']
    option_index = randint(0,len(behavior_options)-1)

    for individual in veeplecensus:#for each veeple, assign a behavior
        individual['Behavior'] = behavior_options[1]#change 1 to option_index once we want more options
    return(veeplecensus)

#behavior_initializer(veeplecensus)
