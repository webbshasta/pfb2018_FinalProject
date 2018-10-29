#! usr/bin/env python3

#import VeepleCensus

# Eve
#Veeple1 = {
#         'ID':1,
#         'Sex':'X',
#         'mGenome':[],
#        'pGenome':[],
#         'Base Fitness':10,
#         'Fitness':10
#         }

# Adam
#Veeple2 = {
#         'ID':2,
#         'Sex':'Y',
#         'mGenome':[],
#         'pGenome':[],
#         'Base Fitness':10,
#         'Fitness':10
#         }

#Veeple3 = {
#         'ID':3,
#         'Sex':'X',
#         'mGenome':[],
#         'pGenome':[],
#         'Base Fitness':10,
#         'Fitness':4
#         }


#Veeple4 = {
#         'ID':4,
#         'Sex':'Y',
#         'mGenome':[],
#         'pGenome':[],
#         'Base Fitness':10,
#         'Fitness':1
#         }


#VeepleCensus = [Veeple1, Veeple2, Veeple3, Veeple4]

def veeplecull(VeepleCensus):
    for Veeple in VeepleCensus:
        if Veeple['Fitness'] < 2:
            print(Veeple['ID'],"to be culled")
    
            VeepleCensus.remove(Veeple)

    return VeepleCensus
#print(len(VeepleCensus))
veeplecull(VeepleCensus)
#print(len(VeepleCensus))
