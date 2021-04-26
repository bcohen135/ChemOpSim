# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:57:58 2021

@author: Ben
"""

from sympy import symbols,Basic

###################################################
##########  Methods for Stream  ###################
###################################################
def flowSign(flow,isInfluent):
    '''
    flowSign corrects the sign of the flow (+ for influent) (- for effluent)

    Parameters
    ----------
    flow : float or str
        the flow
    isInfluent : bool
        True if influent, False if effluent

    Returns
    -------
    flow : float or symbol
        the signed flow

    '''
    if isinstance(flow,str):
        if isInfluent:
            flow = symbols(flow)
        else:
            flow = -symbols(flow)
    else:
        if not isInfluent:
            flow = -flow            
    return flow

def copy(stream):
    flow = stream.getFlow()
    isInfluent = stream.getIsInfluent()
    if not isInfluent:
        flow = -flow
    
    return flow,isInfluent

###################################################
#######  Methods for Material Stream  #############
###################################################
def recreateFracs(fracs):
    '''
    This function will recreate the fraction using symbols instead of strings

    Parameters
    ----------
    fracs : list
        the fractions
    -------
    correctFracs : list
        the fractions with numbers and symbols instead of numbers and strings

    '''
    lenFracs = len(fracs)
    if lenFracs == 0:
        fracs = []
    else:
        k = 0
        for n in range(0,lenFracs):
            if isinstance(fracs[n],str):
                fracs[n] = symbols(fracs[n])
                k = k+1
        if k == 0: #No symbolic values - correct values to equal 1
            fracs = correctSum(fracs)
            
    return fracs
            
def correctSum(fracs):
    '''
    Correct the sum of a list of fractions to be equal to one
    Does not solve if there is one unknown fraction. 
    Parameters
    ----------
    fracs : array of float64
        list of fractions that may or may not add up to one.
    Returns
    -------
    fracs : array of float64
        list of fractions that does add up to one.
    '''
    s = sum(fracs) #Find the sum of all fractions            
        
    if s != 1 and not isinstance(s,Basic):
        for k in range(0,len(fracs)):
            fracs[k] = round(fracs[k]/s,5) #use sum to normalize everything
                 
    return fracs

def buildCompositions(substances,fracs):
    '''
    Build the composition dictionary using the substance and the fraction
    Parameters
    ----------
    substances : list of Species
        list of species
    fracs : array of float64
        list of fractions.
    Returns
    -------
    comp : dictionary of {Species:float64}
        dictionary where the key is a species and the value is the fraction
    '''
    if len(substances) == 0 or len(fracs) == 0:
        comp = {}
    else:
        comp = {substances[i].getFormula():fracs[i] for i in 
                range(0,len(substances))}
    
    return comp

def calcMixtureMW(substances,moleComp):
    '''
    Calculate a mixture molecular weight
    Parameters
    ----------
    substances : list of Species
        list of species
    moleComp : dictionary of {Speices:float64}
        dictionary where the key is a species and the value is the fraction

    Returns
    -------
    streamMW : float64
        molecular weight based on mole composition of a stream or mixture
    '''
    streamMW = 0
    hasSymbol = False
    if len(substances) == 0 or moleComp == {}:
        return streamMW
    else:
        for s in substances:
            mW = s.getMW() #Find each species molecular weight alone
            moleFrac = moleComp.get(s.getFormula()) 
            if isinstance(moleFrac,Basic):
                hasSymbol = True
            streamMW = streamMW + (mW*moleFrac) #Multiple by its mole fraction
        if hasSymbol:
            return streamMW
        else:
            return round(streamMW,6)
        
def calcSpeciesFlows(comp,flow):
    '''1.2
    calculates the species flow and returns a dictionary with the species
    as the key and the flow as the value
    Parameters
    ----------
    comp : dictionary of {str:float}
        composition
    flow : float
        flow.
    Returns
    -------
    comp : dictionary of {str:float}
        dictionary with species and flow.
    '''
    
    thisComp = dict(comp)
    if comp == {}:
        return thisComp
    else:
        if isinstance(flow,str):
            flow = symbols(flow)
            for species in thisComp:
                thisComp[species] = thisComp[species]*flow
        elif isinstance(flow,Basic):
            for species in thisComp:
                thisComp[species] = thisComp[species]*flow
        else:
            for species in thisComp:
                if isinstance(thisComp[species],Basic):
                    thisComp[species] = thisComp[species]*flow
                else:
                    thisComp[species] = round(thisComp[species]*flow,6)
 
    return thisComp

def setAtomQuantities(substances,comp):
    '''
    Break up the chemical formula into atoms and number of atoms. Returns
    a dictionary that holds number of atoms in the values and uses the 
    atomic symbol as a key.
    Parameters
    ----------
    substances : list of species
        list of speices
    Returns
    -------
    atomsQuant : dictionary
        dictionary with atoms and number of atoms.
    '''
    
    atomQuant = {}
    if len(substances)!=0 and comp != {}:
        for species in substances:
            atoms = species.getAtoms()
            if species.getFormula() in comp:
                frac = comp[species.getFormula()]
            else:
                frac = 0
            for atom in atoms:
                atoms[atom] = atoms[atom]
            
            atomQuant = {x:atoms.get(x,0)*frac+atomQuant.get(x,0)
                         for x in set(atoms).union(atomQuant)}
    
    return atomQuant

def setAtomFlows(atomQuant,flow):
    '''
    Break up the chemical formula into atoms and number of atoms. Returns
    a dictionary that holds flow of atoms in the values and uses the 
    atomic symbol as a key.
    Parameters
    ----------
    substances : list of species
        list of speices
    flow : float
        flow.
    Returns
    -------
    atomQuant : dictionary
        dictionary with atoms and flow of atoms.
    '''
    atomFlow = {}
    if atomQuant != {}:
        if isinstance(flow,str):
            flow = symbols(flow)
            for atom in atomQuant:
                atomFlow[atom] = atomQuant[atom]*flow
        elif isinstance(flow,Basic):
            for atom in atomQuant:
                atomFlow[atom] = atomQuant[atom]*flow
        else:
            for atom in atomQuant:
                if isinstance(atomQuant[atom],Basic):
                    atomFlow[atom] = atomQuant[atom]*flow
                else:
                    atomFlow[atom] = round(atomQuant[atom]*flow,6)  
    return atomFlow

#######################################################
#######################################################
#######################################################