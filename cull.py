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

def veeplecull(census):
    for Veeple in census:
        if Veeple['Fitness'] < 2:
           # print(Veeple['ID'],"to be culled")
            census.remove(Veeple)
<<<<<<< HEAD
            
=======
>>>>>>> eab006bfc48ba18158c19a780ff8768d1afc929a
    return census
#print(len(VeepleCensus))
#veeplecull(VeepleCensus)
#print(len(VeepleCensus))
