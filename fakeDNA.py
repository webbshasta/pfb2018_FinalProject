#!/usr/bin/env python3

#Building fake DNA

import random

def starterDNA(l):
    DNA = ['a', 't', 'c', 'g']
    DNAseq = ''

    while len(DNAseq) < l:
        randomIndex1 = random.randint(0, 3)
        DNAseq += DNA[randomIndex1]
    return(DNAseq)

#print(starterDNA(100))
#print(starterDNA(5))



#Building Fake veeple DNA
# Alleles list
allelesGeneA = ['A1', 'A2', 'A3', 'A4']
allelesGeneB = ['B1', 'B2', 'B3', 'B4']
allelesGeneC = ['C1', 'C2', 'C3', 'C4']
allelesGeneD = ['D1', 'D2', 'D3', 'D4']
allelesGeneE = ['E1', 'E2', 'E3', 'E4']

def vDNA(vDNA_A_Dict, vDNA_B_Dict, vDNA_C_Dict, vDNA_D_Dict, vDNA_E_Dict):
    A_seq = {}
    for allele in vDNA_A_Dict:
        A_seq[allele] = starterDNA(10)

    B_seq = {}
    for allele in vDNA_B_Dict:
        B_seq[allele] = starterDNA(10)

    C_seq = {}
    for allele in vDNA_C_Dict:
        C_seq[allele] = starterDNA(10)

    D_seq = {}
    for allele in vDNA_D_Dict:
        D_seq[allele] = starterDNA(10)

    E_seq = {}
    for allele in vDNA_E_Dict:
        E_seq[allele] = starterDNA(10)


    return(A_seq, B_seq, C_seq, D_seq, E_seq)



print(vDNA(allelesGeneA, allelesGeneB, allelesGeneC, allelesGeneD, allelesGeneE)
