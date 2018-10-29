#!/usr/bin/env python3
#method which takes two veeples from VeepleBooper and analyzes which behavior to send them to
def behavior_analyzer(veeple1, veeple2):
    #reads in behaviors and assigns them for easier coding
    behav1 = veeple1['Behavior']
    behav2 = veeple2['Behavior']
    sendTo = ''
    #if the behaviors are mating and consensual
    if behav1 == behav2 and behav1 == 'fuck':
        sendTo = 'fuck'
    else:
        sendTo = 'fightclub'
    return(sendTo)

#skeleton sends veeples to the appropriate output --essentially if not going to mating module
#input two veeple dictionaries, output updated dictionaries
def fight_club(veeple1, veeple2):
    behav1 = veeple1['Behavior']
    behav2 = veeple2['Behavior']
    fit1 = veeple1['Fitness']
    fit2 = veeple2['Fitness']

    #when fighting, see who has the better fitness and determine winners.
    if behav1 == behav2 and behav1 == 'fight':
        if fit1 > fit2:
            veeple1['Fitness'] += 8
            veeple2['Fitness'] -= 2
        elif fit1 < fit2:
            veeple1['Fitness'] -= 2
            veeple2['Fitness'] += 8
        else:
            veeple1['Fitness'] -= 4
            veeple2['Fitness'] -= 4
    #when foraging, both veeples gain the same advantage
    elif behav1 == behav2 and behav1 == 'forage':
        veeple1['Fitness'] += 7
        veeple2['Fitness'] += 7
    #if no one agrees, that means they waste time running away and suffer
    else:
        veeple1['Fitness'] -= 2
        veeple2['Fitness'] -= 2
    
    return veeple1, veeple2
