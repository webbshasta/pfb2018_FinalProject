#!/usr/bin/env python3
import random
# Making a toy world

# Making toy veeples
Veeple1 = {'ID':1, 'Sex':'X', 'Genome': ['ACT','TAG']}  # 'Eve' # Need Cris's random gene generator
Veeple2 = {'ID':2, 'Sex':'Y', 'Genome': ['ACG','GCA']} # 'Adam'
# Make more starter Veeples
VeepleCensus = [Veeple1, Veeple2] # Census of veeples

def VeepleMaker(ID, Sex, Genome1, Genome2): # Makes a veeple when called
    Veeple = {'ID':ID,'Sex':Sex,'Genome':[Genome1,Genome2]}
    return Veeple

def VeepleSects(X,Y):
    NextVeepleID = len(VeepleCensus)+1
    if random.randint(1,2) == 1:
        Sex = 'Y'
    else:
        Sex = 'X'
    if random.randint(1,2) == 1:
        newVeeple = VeepleMaker(NextVeepleID,Sex,X['Genome'][0],Y['Genome'][1])
    else:
        newVeeple = VeepleMaker(NextVeepleID,Sex,X['Genome'][1],Y['Genome'][0])
    VeepleCensus.append(newVeeple)
    return newVeeple


while len(VeepleCensus) < 1000:
    index1 = random.randint(0,len(VeepleCensus)-1)
    while True:
        index2 = random.randint(0,len(VeepleCensus)-1)
        if index2 != index1:
            break
        VeepleSects(VeepleCensus[index1],VeepleCensus[index2])


ACTcount = 0
ACGcount = 0
GCAcount = 0
TAGcount = 0
for person in VeepleCensus:
    for gene in person['Genome']:
        if gene == 'ACT':
            ACTcount += 1
        if gene == 'ACG':
            ACGcount += 1
        if gene == 'GCA':
            GCAcount += 1
        if gene == 'TAG':
            TAGcount += 1

AllGenes = ACGcount+ACTcount+GCAcount+TAGcount
ACTalleleFreq = (ACTcount/AllGenes)*100
ACGalleleFreq = (ACGcount/AllGenes)*100
GCAalleleFreq = (GCAcount/AllGenes)*100
TAGalleleFreq = (TAGcount/AllGenes)*100

print("ACT Allele Freq is",ACTalleleFreq,'\n',\
"ACG Allele Freq is",ACGalleleFreq,'\n',\
"GCA Allele Freq is", GCAalleleFreq,'\n',\
"TAG Allele Freq is",TAGalleleFreq,'\n')
