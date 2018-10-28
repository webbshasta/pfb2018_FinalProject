#!/usr/bin/env python3

#Veeple1 = {
#          'ID' : 1,
#          'Sex' : 'X',
#          'mGenome' : ['A1','B1'],
#          'pGenome' : ['A1','B1'],
#          'Base Fitness' : 10,
#          'Fitness' : 10,
#          'Behavior' : 'family'
#          }
#Veeple2 = {
#          'ID' : 2,
#          'Sex' : 'Y',
#          'mGenome' : ['A2','B2'],
#          'pGenome' : ['A2','B2'],
#          'Base Fitness': 10,
#          'Fitness' : 10,
#          'Behavior': 'family'
#          }

#method which takes two veeples from VeepleBooper and analyzes which behavior to send them to
def behavior_analyzer(veeple1, veeple2):
    #reads in behaviors and assigns them for easier coding
    behav1 = veeple1['Behavior']
    behav2 = veeple2['Behavior']
    sendTo = ''
    #if the behaviors are mating and consensual
    if behav1 == behav2 and behav1 == 'fuck':
        sendTo = 'fuck'
    #if the behaviors are fighting and mutual
    elif behav1 == behav2 and behav1 == 'fight':
        sendTo = 'fight'
    #if everyone wants to farm and leave the others alone
    elif behav1 == behav2 and behav1 == 'family':
        sendTo = 'family'
    #the two behaviors are not the same, fight > fuck > family
    else:
        if behav1 == 'fight' or behav2 == 'fight':
            sendTo = 'fight'
        elif behav1 == 'fuck' or behav2 == 'fuck':
            sendTo = 'fuck'
        else:
            sendTo = 'family' #this option may not be relevant in these circumstances.
    return(veeple1,veeple2,sendTo)

#behavior_analyzer(Veeple1, Veeple2)
