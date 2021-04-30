# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:57:58 2021

@author: Ben
"""

from sympy import symbols,Basic,preorder_traversal,Float
from materials import materialMethods as mM

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
        if k == 0: 
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
    
    for k in range(0,len(fracs)):
        nF = fracs[k]/s
        if isinstance(s,Basic) or isinstance(fracs[k],Basic):
            newFrac = nF
            for a in preorder_traversal(nF):
                if isinstance(a,Float):
                    newFrac = newFrac.subs(a,round(a,5))
        else:
            newFrac = round(nF,5)
        fracs[k] = newFrac                 
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

def calcMoleComps(substances,speciesMoleFlow):
    '''
    calcMoleComps will calculate the molar composition of the material stream

    Parameters
    ----------
    substances : list[Species]
        list of species present.
    speciesMoleFlow : dict{str:Basic}
        a dictionary of molar flow of each species in stream.

    Returns
    -------
    moleFracs : list[Basic]
        list of molar fractions.
    moleComp : dict[str:Basic]
        dictionary of molar composition.

    '''
    sMF = speciesMoleFlow
    moleComp = {}
    moleFracs = []
    
    if len(substances)!=0 and sMF!={}:
        for spec in sMF:
            moleFracs.append(sMF[spec])
        moleFracs = correctSum(moleFracs)
        k = 0
        for spec in sMF:
            moleComp[spec] = moleFracs[k]
            k+=1
    return moleFracs,moleComp
    
def massToMoleFlows(substances,speciesMassFlows):
    '''
    massToMoleFlows converts the mass flows of each species to molar
    flows.

    Parameters
    ----------
    substances : list[Species]
        list of species present.
    speciesMassFlows : dict{str:Basic}
        dictionary of the mass flows of each species.

    Returns
    -------
    sMoleF : dict{str:Basic}
        dictionary of the mole flows of each species.

    '''
    sMassF = speciesMassFlows
    sMoleF = {}
    if len(substances) == 0 or sMassF == {}:
        return sMoleF
    else:
        for s in substances:
            mW = s.getMW()
            thisKey = s.getFormula()
            massFlow = sMassF[thisKey]
            if isinstance(massFlow,str):
                massFlow = symbols(massFlow)
            moleFlow = massFlow/mW
            if isinstance(moleFlow,Basic):
                for a in preorder_traversal(moleFlow):
                    if isinstance(a,Float):
                        moleFlow = moleFlow.subs(a,round(a,5))
            else:
                moleFlow = round(moleFlow,5)
            sMoleF[thisKey] = moleFlow
        return sMoleF
    
def calcMixtureMW(massFlow,moleFlow):
    '''
    Calculate a mixture molecular weight
    Parameters
    ----------
    massFlow : Basic
        mass flow of material stream
    moleFlow : Basic
        molar flow of material stream
        
    Returns
    -------
    streamMW : float64
        molecular weight based on mole composition of a stream or mixture
    '''
    if moleFlow == 0:
        streamMW = 0
    else:
        sMW = massFlow/moleFlow
        if isinstance(sMW,Basic):
            streamMW = sMW
            for a in preorder_traversal(sMW):
                if isinstance(a,Float):
                    streamMW = streamMW.subs(a,round(a,5))
        else:
            streamMW = round(sMW,5)
        
    return streamMW

def calcMoleFlow(speciesMoleFlows):
    '''
    Calculates the molar flow of the material stream
    Parameters
    ----------
    speciesMoleFlows : dict{str:Basic}
        dictionary of the mole flows of each species.
        
    Returns
    -------
    moleFlow : Basic
        molar flow of material stream
    '''
    sMF = speciesMoleFlows
    mF = 0
    if sMF == {}:
        return mF
    else:
        for spec in sMF:
            newMF = sMF[spec]
            mF = mF + newMF
        if isinstance(mF,Basic):
            moleFlow = mF
            for a in preorder_traversal(mF):
                if isinstance(a,Float):
                    moleFlow = moleFlow.subs(a,round(a,5))
        else:
            moleFlow = round(mF,5)
        return moleFlow

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
    
    thisFlow = dict(comp)
    if comp == {}:
        return thisFlow
    else:
        if isinstance(flow,str):
            flow = symbols(flow)
        for species in thisFlow:
            if isinstance(thisFlow[species],str):
                thisFlow[species] = symbols(thisFlow[species])
            nF = thisFlow[species]*flow
            newFlow = nF
            if isinstance(nF,Basic):
                for a in preorder_traversal(nF):
                    if isinstance(a,Float):
                        newFlow = newFlow.subs(a,round(a,5))
            else:
                newFlow = round(newFlow,5)
            thisFlow[species] = newFlow
        return thisFlow

def setAtomQuantities(substances,comp):
    '''
    Break up the chemical formula into atoms and number of atoms. Returns
    a dictionary that holds number of atoms in the values and uses the 
    atomic symbol as a key.
    Parameters
    ----------
    substances : list of species
        list of speices
    comp : dict{str:Basic}
        dictionary of either mass or molar composition
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
            
            for x in set(atoms).union(atomQuant):
                nQ = atoms.get(x,0)*frac+atomQuant.get(x,0)
                if isinstance(nQ,Basic):
                    newQuant = nQ
                    for a in preorder_traversal(nQ):
                        if isinstance(a,Float):
                            newQuant = newQuant.subs(a,round(a,7))
                else:
                    newQuant = round(nQ,7)
                atomQuant[x] = newQuant
            
    for atom in atomQuant:
        atomNum = atomQuant[atom]
        if isinstance(atomNum,Basic):
            aN = atomNum
            for a in preorder_traversal(atomNum):
                if isinstance(a,Float):
                    replaceVal = round(a,5)
                    aN = aN.subs(a,replaceVal)
        else:
            aN = round(atomNum,5)
        atomQuant[atom] = aN
    return atomQuant

def setAtomFlows(atomQuant,flow):
    '''
    Break up the chemical formula into atoms and number of atoms. Returns
    a dictionary that holds flow of atoms in the values and uses the 
    atomic symbol as a key.
    Parameters
    ----------
    atomQuant : dictionary
        dictionary with atoms and number of atoms.
    flow : float
        flow.
    Returns
    -------
    atomFlow : dictionary
        dictionary with atoms and flow of atoms.
    '''
    atomFlow = {}
    if atomQuant != {}:
        if flow == 0:
            for atom in atomQuant:
                atomFlow[atom] = 0
        else:
            if isinstance(flow,str):
                flow = symbols(flow)
            for atom in atomQuant:
                nF = atomQuant[atom]*flow
                if isinstance(nF,Basic):
                    newFlow = nF
                    for a in preorder_traversal(nF):
                        if isinstance(a,Float):
                            tempVar = round(a,5)
                            newFlow = newFlow.subs(a,tempVar)
                else:
                    newFlow = round(nF,5)
                atomFlow[atom] = newFlow
    return atomFlow
       
def calcAtomMassFlows(substances,atomMoleFlows):
    '''
    calcAtomMassFlows calculatesthe mass flow of the atoms in the material
    stream

    Parameters
    ----------
    substances : list[Species]
        list of species present.
    atomFlow : dictionary
        dictionary with atoms and molar flow of atoms.

    Returns
    -------
    atomFlow : dictionary
        dictionary with atoms and mass flow of atoms.

    '''
    atomMassFlows = {}
    if len(substances) == 0 or atomMoleFlows == {}:
        return atomMassFlows
    else:
        for s in substances:
            atoms = s.getAtoms()
            for atom in atoms:
                if atom not in atomMassFlows:
                    aW = mM.getAtomicWeight(atom)
                    nF = atomMoleFlows[atom]*aW
                    newFlow = nF
                    if isinstance(nF,Basic):
                        for a in preorder_traversal(nF):
                            if isinstance(a,Float):
                                newFlow = newFlow.subs(a,round(a,5))
                    else:
                        newFlow = round(newFlow,5)
                    atomMassFlows[atom] = newFlow
        return atomMassFlows
#######################################################
#######################################################
#######################################################