# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:40:02 2021
@author: Ben
"""

import re
import pandas as pd
import os

###################################################
##########  Methods for Species  ##################
###################################################
def calcMW(atoms):   
    '''
    Calculate the molecular weight of a species based on its chemical formula.
    Parameters
    ----------
    atoms : dictionary
        dictionary with atoms and number of items.
    Returns
    -------
    mW : float
        molecular weight.
    '''
    mW = 0 #Initialize molecular weight
    try:
        #Calculate molecular weight using atomic weight
        for atom in atoms:
            atomicWeight = getAtomicWeight(atom)
            numberAtoms = atoms.get(atom)
    
            mW = mW + (atomicWeight*numberAtoms)
    except:
        mW = 0

    return mW

def parseFormula(formula):
    '''
    Break up the chemical formula into atoms and number of atoms. Returns
    a dictionary that holds number of atoms in the values and uses the 
    atomic symbol as a key.
    Parameters
    ----------
    formula : str
        chemical formula.
    Returns
    -------
    atoms : dictionary
        dictionary with atoms and number of items.
    '''
    try:
        #Split chemical formula based on capital letters and numbers
        fS = re.findall('[A-Z][a-z]?|\d+|.',formula)
        
        #Create a dictionary with element as key that holds the number of atoms
        atoms = {}
        for i in range(0,len(fS),2):
            if fS[i].isalpha():
                atoms[fS[i]] = float(fS[i+1])
            else:
                atoms = {}
                break
    except:
        atoms = {}

    return atoms

def getAtomicWeight(atom):
    '''
    Get the atomic weight of an atom from Atomic_Weights.csv
    Parameters
    ----------
    atom : str
        atomic symbol.
    Returns
    -------
    atomicWeight : float
        atomic weight for atomic symbol input.
    '''
    #The file that holds all the atomic weights
    cwd = os.path.dirname(__file__)
    file = os.path.join(cwd,'../materials/Atomic_Weights.csv')        
    atomicWeights = pd.read_csv(file)

    #Retrieve the atomic weight of the atom passed as input
    atomicWeight = atomicWeights.loc[atomicWeights['Symbol']==atom, 
                                     'Atomic Weight'].values[0]

    return atomicWeight