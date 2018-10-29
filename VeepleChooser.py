#!/usr/bin/env python3
# Veeple Chooser Function!
import random

def VeepleChooser(VeepleTab):
    index1 = random.randint(0,len(VeepleTab)-1)
    while True:
        index2 = random.randint(0,len(VeepleTab)-1)
        if index2 != index1:
            break
    return [index1, index2]
