# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:08:02 2021

@author: Ben
"""

from streams import streamMethods as sM

class Stream():
    '''
    A stream is aflow of something in or out
    Attributes:
        flow: the flow of the stream
        isInfluent: True if the stream is positive, False if negative
    Methods:
        get and set methods
        copy: makes a copy of the object
    '''
    def __init__(self,flow=0,isInfluent=True):
        if flow == None or isinstance(flow,bool):
            flow = 0
        self.setIsInfluent(isInfluent)
        self.setFlow(flow)
    
    def setIsInfluent(self,isInfluent):
        self.isInfluent = isInfluent
        
    def setFlow(self,flow):
        self.flow = sM.flowSign(flow,self.isInfluent)
    
    def getIsInfluent(self):
        return self.isInfluent
    
    def getFlow(self):
        return self.flow
    
    def copy(self):
        flow,isInfluent = sM.copy(self)
        return Stream(flow,isInfluent)
    
class MaterialStream(Stream):
    '''
    A Material Stream is a a mixture of species.
    Inherits:
        Stream from steams (see Streams/streams.py)
    Attributes:
        susbtances: a list of species in material stream
        moleFracs: a list of molar fractions of substances
        moleFlow: the molar flow of the material stream
        isInfluent: True if the material stream is an influent
            stream or the direction of the flow does not matter
        moleComp: a dictionary of {species formula: mole frac}
        isInfluent: True if steam is influent (default). False signifies
            effluent and will show negative flows
    Methods:
        get and set methods
        __calcMW: calculates the molecular weight of the stream
        __calcSpeciesFlow: calculates the molar flow of each species
        __calcAtomicFlows: cacluates the molar flow of each type of atom
        __caclAtomQuants: calculates the number of atoms per mole of material
        copy: makes a copy of the object
        
    '''
    def __init__(self,substances=[],moleFracs=[],moleFlow=0,isInfluent=True):
        if not isinstance(substances,list):
            substances = []
        super().__init__(moleFlow,isInfluent)
        self.moleFlow = self.flow
        self.substances = substances
        self.moleFlow = moleFlow
        self.__setMoleComp(substances,moleFracs)
        self.setInOrOut(isInfluent)
        
    def __setMoleComp(self,substances,moleFracs):
        self.substances = substances
        self.moleFracs = sM.recreateFracs(moleFracs)
        self.moleComp = sM.buildCompositions(substances,moleFracs)
        self.__calcMW()
        self.__calcSpeciesFlow()
        self.__calcAtomicQuants()
    
    def setInOrOut(self,isInfluent):
        self.isInfluent = isInfluent
        self.setMoleFlow(self.moleFlow)
        self.moleFlow = self.flow
    
    def setMoleFlow(self,moleFlow):
        super().setFlow(moleFlow)
        self.moleFlow = self.flow
        self.__calcSpeciesFlow()
        self.__calcAtomicFlows()
        
    def setSubstances(self,substances):
        self.__setMoleComp(self,substances,self.moleFracs)
        
    def setMoleFracs(self,moleFracs):
        self.__setMoleComp(self,self.substances,moleFracs)
        
    def getSubstances(self):
        return self.substances
    
    def getIsInfluent(self):
        super().getIsInfluent()
    
    def getMoleFracs(self):
        return self.moleFracs
    
    def getMoleFlow(self):
        return self.flow
    
    def getMoleComp(self):
        return self.moleComp 
    
    def getMW(self):
        return self.mW
    
    def getSpeciesFlow(self):
        return self.speciesFlow
    
    def getAtomQuants(self):
        return self.atomQuants
    
    def getAtomicFlows(self):
        return self.atomicFlows
    
    def __calcMW(self):
        self.mW = sM.calcMixtureMW(self.substances, self.moleComp)
        
    def __calcSpeciesFlow(self):
        self.speciesFlow = sM.calcSpeciesFlows(self.moleComp,self.moleFlow)
    
    def __calcAtomicFlows(self):
        self.__calcAtomicQuants()
        self.atomicFlows = sM.setAtomFlows(self.atomQuants,self.moleFlow)
        
    def __calcAtomicQuants(self):
        self.atomQuants = sM.setAtomQuantities(self.substances,
                                                 self.moleComp)
    
    def copy(self):
        moleFlow,isInfluent = sM.copy(self)
        return MaterialStream(self.substances,self.moleFracs,moleFlow,
                              isInfluent)