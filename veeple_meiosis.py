#!/usr/bin/env python3

import random
import genome_maker as gm
#method which takes two veeples and assigns them as maternal or paternal genomes
#from each veeple, a single sex chromosome is generated via randomly chosen alleles from a veeples
#maternal and paternal genome (meiosis). The base fitness of the baby is calculated via genome_maker
def veeple_meiosis(veeple1,veeple2,veeplebaby):
    babymGenome=[]
    babypGenome=[]
    genomelength = len(veeple1['mGenome'])
    #Going through the Veeple1 (maternal) to generate meiosis mGenome 
    for i in range(genomelength):
        fate = random.randint(0,1)
        if fate == 1:
           babymGenome.append(veeple1['mGenome'][i])
        else:
            babymGenome.append(veeple1['pGenome'][i])
    #Going through the Veeple2 (paternal) to generate meiosis pGenome        
    for i in range(genomelength):
        fate = random.randint(0,1)
        if fate == 1:
            babypGenome.append(veeple2['mGenome'][i])
        else:
            babypGenome.append(veeple2['pGenome'][i])
    
    veeplebaby['mGenome'] = babymGenome
    veeplebaby['pGenome'] = babypGenome

    #calling up Genome_Maker base fitness
    Allele_fit_dict = gm.Allele_fit_dict
    veeplebaby['Base Fitness'] = gm.base_fitness(veeplebaby)
    return(veeplebaby)

