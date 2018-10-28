#!"""/usr/bin/env python3
# Starting to make the better game of life
import random
from genome_maker import starterGenome
from genome_maker import base_fitness
from behavior_initializer import behavior_initializer
import sys
from VeepleChooser import VeepleChooser
from behavior_analyzer import behavior_analyzer

#Make some starter veeples

Veeple1 = {
          'ID' : 1,
          'Sex' : 'X',
          'mGenome' : [],
          'pGenome' : [],
          'Base Fitness' :0 ,
          'Fitness' : 0,
          'Behavior': ''
          }

# Adam

Veeple2 = {
          'ID' : 2,
          'Sex' : 'Y',
          'mGenome' : [],
          'pGenome' : [],
          'Base Fitness': 0,
          'Fitness' : 0,
          'Behavior' : ''
          }

# Empty baby veeple
VeepleBaby = {
          'ID' : 0,
          'Sex' : '',
          'mGenome' : [],
          'pGenome' : [],
          'Base Fitness': 0,
          'Fitness' : 0,
          'Behavior' : ''
          }

# Give Eve a starter genome, fitnesses, and behavior
Veeple1 = starterGenome(Veeple1)
Veeple1 = base_fitness(Veeple1)
Veeple1 = behavior_initializer(Veeple1)

# Give Adam a starter genome, fitnesses, and behavior
Veeple2 = starterGenome(Veeple2)
Veeple2 = base_fitness(Veeple2)
Veeple2 = behavior_initializer(Veeple2)

# Initialize a veeple census
VeepleCensus = [Veeple1, Veeple2] #List of Veeple dictionaries 

#***************
#Get initial census stats
#**************

generation = 0
TotalGenerations = 3

while generation < TotalGenerations:
    VeepleTab = copy.VeepleCensus()
    for veeple in VeepleTab:
        randomVeepInd = VeepleChooser(VeepleTab)
        print(randomVeepInd)
        veepForBehAna1 = randomVeepInd[0]
        veepForBehAna2 = randomVeepInd[1]
        newVeeps = behavior_analyzer(veepForBehAna1, veepForBehAna2)

"""    
  

# Create a function that chooses to Veeples two
VeepleTab = copy.VeepleCensus()

VeeplesChosen = VeepleChooser(VeepleTab) #Gets list of random indices from VeepleChooser
Veeple1 = VeeplesChosen[0]
Veeple2 = VeepleChosen[1]












newVeeples = BehaviorAnalyzer(Veeple1, Veeple2) #Sends those randomly selected veeples to Behavior analyzer
#BehaviorAnalyzer returns a list of veeples either with updated stats, or a new veeple
#Update Census
for veeple in VeepleCensus:
    if newVeeple['ID'] == veeple['ID']
        VeepleCensus.remove(veeple)
        VeepleCensus.append(newVeeple)
    else
        VeepleCensus.append(newVeeple)

def VeepleBooper(VeepleCensus,index1,index2)
    


        VeepleTab.remove(VeepleTab[index1])
        VeepleTab.remove(VeepleTab[index2])


while generation < Total Genereations:
"""    
