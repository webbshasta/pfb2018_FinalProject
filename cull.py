#!/usr/bin/env python3
# identify and remove Veeples with fitness too low to continue.
def veeplecull(census):
    for Veeple in census:
        if Veeple['Fitness'] < 2: #test for low fitness--maybe change?
            census.remove(Veeple)
    return census
