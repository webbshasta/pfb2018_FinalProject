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
import population_statistics as ps
from veeple_meiosis import veeple_meiosis
from population_statistics import veeple_population_count as vpc, veeple_percent_sex as vps, veeple_allelic_frequencies as vaf

#Make some starter veeples

Veeple1 = {
          'ID' : 1,
          'Sex' : 'X',
          'mGenome' : [],
          'pGenome' : [],
          'Base Fitness' :0 ,
          'Fitness' : 0,
          'Behavior': '',
          'Used' : 'no'
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
          'Used' : 'no'
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
VeepleArchive = VeepleCensus.copy()

#Get initial population statistics
init_tot_pop = vpc(VeepleCensus)
init_allelic_freq = vaf(VeepleCensus)
sex_percents = vps(VeepleCensus)
per_X = sex_percents[0]*100
per_Y = sex_percents[1]*100
#print('Initial population is {} large \nIt has {}%X and {}%Y \nThe allelic frequencies are {}'.format(init_tot_pop, per_X, per_Y, init_allelic_freq))

# Generation Counter
generation = 0
TotalGenerations = 10

# Life happens here up to set number of generations
while generation < TotalGenerations:
    VeepleTab = VeepleCensus.copy()

    #Death clause
    if len(VeepleCensus) < 2:
        print('The population has crashed -- Ask not for whom the bell tolls')
        break
    else: # Looping over the populat
        for veeple in VeepleTab:
            if veeple['Used'] == 'no':   # Only un-chosen veelpes will used
                randomVeepInd = VeepleChooser(VeepleTab)    # Randomly choose 2 veeples
                veepForAct1 = randomVeepInd[0]
                veepForAct2 = randomVeepInd[1]
                vfa1 = VeepleTab[veepForAct1] 
                vfa2 = VeepleTab[veepForAct2]
                behavior = behavior_analyzer(vfa1, vfa2)    # Determine their behavior

                if behavior == 'fuck':      # If they both wanna make a baby
                    babyVeeple = VeepleMatingTest(vfa1, vfa2, VeepleBaby)
                    babyVeeple = VeepleID(VeepleArchive, babyVeeple)
                    babyVeeple = veeple_meiosis(vfa1, vfa2, babyVeeple)
                    babyVeeple['Used'] = 'yes'  # Our initiated vBaby
                    #print('babyVeeple\n',babyVeeple)
                    vfa1['Used'] = 'yes'
                    vfa2['Used'] = 'yes'
                    VeepleCensus.append(babyVeeple)  # Add vBaby to the census
                    VeepleArchive.append(babyVeeple) # and the archive

                elif behavior == 'fightclub':  # Any other behaviors
                    VeepleCensus.remove(vfa1)  # Take out our actors from census
                    VeepleCensus.remove(vfa2)   
                    changedVeeples = fight_club(vfa1, vfa2) # Get them back with new fit
                    #print('Changed veeps\n', changedVeeples)
                    altVeeple1 = changedVeeples[0]
                    #print('Alt1\n',altVeeple1)
                    altVeeple2 = changedVeeples[1]
                    #print('Alt2\n', altVeeple2)
                    altVeeple1['Used'] = 'yes'
                    altVeeple2['Used'] = 'yes'
                    VeepleCensus.append(altVeeple1)
                    VeepleCensus.append(altVeeple2)

    climateScore = clim.get_climate(clim.climate)
    disasterScore = clim.get_naturaldisasters(clim.natural_disaster, clim.climate)
    diseaseScore = clim.get_populationhealth(clim.climate, len(VeepleCensus))
    for veeple in VeepleCensus:
        updatedVeep = Veepfit(veeple, climateScore, diseaseScore, disasterScore)
       # print(updatedVeep)
    for veeple in VeepleCensus:
        veeple = behavior_initializer(veeple)
    VeepleCensus = veeplecull(VeepleCensus)
    for veeple in VeepleCensus:
        veeple['Used'] = 'no'
    for veeple in VeepleCensus:
         print('id', veeple['ID'], '\t','sex', veeple['Sex'], '\tbehav', veeple['Behavior'], '\tfit',veeple['Fitness'] )
    print('gen',generation)
    generation += 1

#Get final population statistics
fin_tot_pop = len(VeepleCensus)
fin_allelic_freq = vaf(VeepleCensus)
fin_sex_percents = vps(VeepleCensus)
fin_per_X = sex_percents[0]*100
fin_per_Y = sex_percents[1]*100
#print('Final population is {} large \nIt has {}%X and {}%Y \nThe allelic frequencies are {}'.format(fin_tot_pop, fin_per_X, fin_per_Y, fin_allelic_freq))


