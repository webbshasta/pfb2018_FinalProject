#!/usr/bin/env python3

#Making an ID for a new veeple
id_list = []
def VeepleID(veepleCensus, Veeple):
    for veep in veepleCensus:
        id_list.append(veep['ID'])
    newID = (max(id_list)+1)
    Veeple['ID'] = newID
    return Veeple
