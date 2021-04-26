# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:16:20 2021
@author: Ben
"""

import pandas as pd
import os

def unitConversions(x,unit1,quantity,unit2="default"):     
    '''
    Parameters
    ----------
    x : float
        unit 1 value. (ex. 5.2)
    unit1 : str
        unit 1. (ex. 'kg')
    quantity : str
        quantity of measurement. (ex. 'Mass')
    unit2 : str, optional
        unit 2. The default is "default" (Metric) (ex. 'lbm')
    Returns
    -------
    y : float
        value in unit 2.
    '''

    cwd = os.path.dirname(__file__)
    file = os.path.join(cwd,'../units/Unit_Conversions.csv')

    unitConvs = pd.read_csv(file)

    quantVals = unitConvs.loc[unitConvs['Quantity']==quantity]

    u1M = quantVals.loc[quantVals['Unit']==unit1,'Value'].values[0]

    if unit2 == 'default':
        u2M = quantVals.loc[quantVals['Base']==True, 'Value'].values[0]
    else:
        u2M = quantVals.loc[quantVals['Unit']==unit2,'Value'].values[0]        

    y = x*u2M/u1M

    return y

def unitParse(unit):
    
    #This function should break up the units into the base units
    #Ex. kg/s --> kg and s
    numeratorUnits = [] #units that are in the numerator
    denominatorUnits = [] #units that are in the denominator

    parsedUnits = unit.split('/') #units divided into top and bottom
    
    #Iterate through numerator units
    for nu in parsedUnits[0].split('*'):
        numeratorUnits.append(nu)
    #Iterate through denominator units
    for nu in parsedUnits[1].split('*'):
        denominatorUnits.append(nu)

    return numeratorUnits,denominatorUnits

def complexUnitConversions(unit1,unit2='default'):
    #This function should loop through each base unit of a larger value
    #using unitConversions and return a single unit value in the target unit
    #base
    nUnits1,dUnits1 = unitParse(unit1)
    nUnits2,dUnits2 = unitParse(unit2)
    
    nU1len = len(nUnits1)
    dU1len = len(dUnits1)
        
    numerator = 1
    denominator = 1
    
    for k in range(0,nU1len):
        u1 = nUnits1[k]
        u2 = nUnits2[k]
        cF = unitConvFactor(u1,u2)
        numerator = numerator*cF
    for k in range(0,dU1len):
        u1 = dUnits1[k]
        u2 = dUnits2[k]
        cF = unitConvFactor(u1,u2)
        denominator = denominator*cF
        
    convFact = numerator/denominator
    
    return convFact

def unitConvFactor(unit1,unit2):
    file = "Unit_Conversions.csv"
    unitConvs = pd.read_csv(file)
    
    u1M = unitConvs.loc[unitConvs['Unit']==unit1,'Value'].values[0]
    u2M = unitConvs.loc[unitConvs['Unit']==unit2,'Value'].values[0]
    
    convFactor = u2M/u1M
    return convFactor