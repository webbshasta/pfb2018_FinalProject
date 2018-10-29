#! usr/bin/env python3
#import climate_naturaldisasters.py



#Veeple1 = {
 #         'ID' : 1,
 #        'Sex' : 'X',
#        'mGenome' : ['A1','B1'],
#         'pGenome' : ['A1','B1'],
#         'Base Fitness' : 10,
#         'Fitness' : 10
#         }

#Envir = -2
#Dis = -3

def Veepfit(Veeple1, Envir, Nat Dis,  Dis): #set up function

    Veepfit = int(Veeple1['Fitness']) + int(Envir) + int(NatDis) + int(Dis) #sum up all the contributions
    Veeple1['Fitness'] = Veepfit  #add back to dictionary
    #print(Veepfit, Veeple1['Fitness'])
    return Veeple1 #calculated answer 

    # print(Veepfit, Veeple1['Fitness'])
Veepfit(Veeple1)
