# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:01:27 2021

@author: Ben
"""

from sympy import symbols,Eq

from materials import materialClasses as mC
from streams import streams as stms
from unitOperations import unitOperations as uO

water = mC.Species('H2O1')
methane = mC.Species('C1H4')
co2 = mC.Species('C1O2')
co = mC.Species('C1O1')
hydrogen = mC.Species('H2')
nitrogen = mC.Species('N2')
salt = mC.Species('Na1Cl2')
oxygen = mC.Species('O2')

ms1 = stms.MaterialStream([water,methane,co],[0.3,0.4,0.3],8)
ms2 = stms.MaterialStream([water,methane,co],[0.1,0.7,0.2],5)
ms3 = stms.MaterialStream([oxygen,nitrogen],[0.21,0.79],'q')
ms4 = stms.MaterialStream([methane,co2,co],['x','y','z'],6)

print(ms4.getAtomicMassFlow())
print(ms4.getSpeciesMassFlow())

print(ms3.getMoleFlow())
print(ms3.getSpeciesMassFlow())

myDict1 = {'a':1,'b':4,'c':2,'e':7}
myDict2 = {'a':3,'b':2,'c':8,'d':3}

def addDict(dict1,dict2):
    returnDict = {}
    for key in dict1:
        val1 = dict1[key]
        if key in dict2:
            val2 = dict2[key]
        else:
            val2 = 0
        val = val1+val2
        returnDict[key] = val
    for key in dict2:
        if not key in returnDict:
            returnDict[key] = dict2[key]
    return returnDict
        
myDict3 = addDict(myDict1,myDict2)
print(myDict3)