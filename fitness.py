#!/usr/bin/env python3

def Veepfit(Veeple1, envScore, natDisScore, diseaseScore): #set up function

    Veepfit = int(Veeple1['Fitness']) - int(envScore) - int(natDisScore) - int(diseaseScore) #sum up all the contributions
    Veeple1['Fitness'] = Veepfit  #add back to dictionary
    return Veeple1 #calculated answer

