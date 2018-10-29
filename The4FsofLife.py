#!/usr/bin/env python3
# Starting to make the better game of life
import random
import genome_maker
import sys
from VeepleChooser import VeepleChooser
from behavior_initializer import behavior_initializer
from behavior_analyzer import behavior_analyzer, fight_club
from VeepleSexAssignmentFunction import VeepleMatingTest
from IDmaker import VeepleID
import climate_naturaldisasters as clim
from fitness import Veepfit
from cull import veeplecull

#Make some starter veeples

Veeple1 = {
          'ID' : 1,
          'Sex' : 'X',
          'mGenome' : [],
          'pGenome' : [],
          'Base Fitness' :0 ,
          'Fitness' : 0,
          'Behavior': '',
          'Used' : ''
          }

# Adam

Veeple2 = {
          'ID' : 2,
          'Sex' : 'Y',
          'mGenome' : [],
          'pGenome' : [],
          'Base Fitness': 0,
          'Fitness' : 0,
          'Behavior' : '',
          'Used' : ''
          }

# Empty baby veeple
VeepleBaby = {
          'ID' : 0,
          'Sex' : '',
          'mGenome' : [],
          'pGenome' : [],
          'Base Fitness': 0,
          'Fitness' : 0,
          'Behavior' : '',
          'Used' : ''
          }

# Give Eve a starter genome, fitnesses, and behavior
Veeple1 = genome_maker.starterGenome(genome_maker.allelesGeneA, genome_maker.allelesGeneB, genome_maker.allelesGeneC, genome_maker.allelesGeneD, genome_maker.allelesGeneE, Veeple1)
Veeple1 = behavior_initializer(Veeple1)
#print(Veeple1)

# Give Adam a starter genome, fitnesses, and behavior
Veeple2 = genome_maker.starterGenome(genome_maker.allelesGeneA, genome_maker.allelesGeneB, genome_maker.allelesGeneC, genome_maker.allelesGeneD, genome_maker.allelesGeneE, Veeple2)
Veeple2 = behavior_initializer(Veeple2)
#print(Veeple2)

# Initialize a veeple census
VeepleCensus = [Veeple1, Veeple2] #List of Veeple dictionaries 

#***************
#Get initial census stats
#**************

generation = 0
TotalGenerations = 3

while generation < TotalGenerations:
    VeepleTab = VeepleCensus.copy()
    for veeple in VeepleTab:
        randomVeepInd = VeepleChooser(VeepleTab)
        #print(randomVeepInd)
        veepForAct1 = randomVeepInd[0]
        veepForAct2 = randomVeepInd[1]
        vfa1 = VeepleTab[veepForAct1]
        vfa2 = VeepleTab[veepForAct2]
        behavior = behavior_analyzer(vfa1, vfa2)
        if behavior == 'fuck':
            babyVeeple = VeepleMatingTest(vfa1, vfa2, VeepleBaby)
            babyVeeple = VeepleID(VeepleCensus, babyVeeple)
            babyVeeple = genome_maker.starterGenome(genome_maker.allelesGeneA, genome_maker.allelesGeneB, genome_maker.allelesGeneC, genome_maker.allelesGeneD, genome_maker.allelesGeneE, babyVeeple)
            babyVeeple['Used'] = 'yes'
            VeepleCensus.append(babyVeeple)
            #print(babyVeeple) 
        if behavior == 'fightclub':
            VeepleCensus.remove(vfa1)
            VeepleCensus.remove(vfa2)
            changedVeeples = fight_club(vfa1, vfa2)
            altVeeple1 = changedVeeples[0]
            altVeeple2 = changedVeeples[1]
            altVeeple1['Used'] = 'yes'
            altVeeple2['Used'] = 'yes'
            VeepleCensus.append(altVeeple1)
            VeepleCensus.append(altVeeple2)
       # print(VeepleCensus)
    climateScore = clim.get_climate(clim.climate)
    disasterScore = clim.get_naturaldisasters(clim.natural_disaster, clim.climate)
    diseaseScore = clim.get_populationhealth(clim.climate, len(VeepleCensus))
    #print(climateScore, disasterScore, diseaseScore)
    for veeple in VeepleCensus:
        updatedVeep = Veepfit(veeple, climateScore, diseaseScore, disasterScore)
       # print(updatedVeep)
    VeepleCensus = veeplecull(VeepleCensus)
    generation += 1

print(VeepleCensus)

