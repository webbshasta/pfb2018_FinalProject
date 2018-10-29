#!/usr/bin/env python3
import random
import genome_maker as gm
from behavior_initializer import behavior_initializer as bi
import sys
# Making a starting group of Veeples

StartingVeepArc = []

numVeepsDes = 10 #sys.argv[1]

BlankVeeple = {
          'ID' : 0,
          'Sex' : '',
          'mGenome' : [], 
          'pGenome' : [], 
          'Base Fitness' :0 ,
          'Fitness' : 0,
          'Behavior': '', 
          'Used' : 'no'
          }

while len(StartingVeepArc) < numVeepsDes:
    newVeeple = BlankVeeple
    newVeeple['ID'] = len(StartingVeepArc)+1
    newVeeple = gm.starterGenome(gm.allelesGeneA, gm.allelesGeneB, gm.allelesGeneC, gm.allelesGeneD, gm.allelesGeneE, newVeeple)
    newVeeple = bi(newVeeple)
    StartingVeepArc.append(newVeeple)
    #print('New Veeple \n', 'ID\t', newVeeple['ID'], 'Fitness\t', newVeeple['Fitness'], 'Behavior\t', newVeeple['Behavior'])
