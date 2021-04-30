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
        __calcMoleFlow : calculates the molar flow of the stream
        __calcSpeciesFlow : calculates the mass and molar flow for each species
        __calcAtomicFlows : calculates the mass and molar flow for each atom
        __calcAtomicQuants : calculates the coefficient per atom in stream
        __calcMW: calculates the molecular weight of the stream
        __cleanup : corrects values if no flow or bad inputs are entered when
            initializing material stream
        copy: makes a copy of the object
        
    '''
    def __init__(self,substances=[],massFracs=[],massFlow=0,isInfluent=True):
        if not isinstance(substances,list):
            substances = []
        super().__init__(massFlow,isInfluent)
        self.massFlow = self.flow
        self.__setMassComp(substances,massFracs)
        self.__setMoleInfo(self.massComp)
        if self.massFlow == 0 and self.mW == 0:
            self.__cleanup()
        
    def __setMassComp(self,substances,massFracs):
        self.substances = substances
        self.massFracs = massFracs
        self.massComp = sM.buildCompositions(substances,massFracs)
        self.__calcSpeciesFlow()
    
    def __setMoleInfo(self,massComp):
        self.moleFracs,self.moleComp = sM.calcMoleComps(self.substances,
                                                        self.speciesMoleFlow)
        self.__calcMoleFlow()
        self.__calcMW()
        self.__calcAtomicFlows()
        
    def setSubstances(self,substances):
        self.__setMassComp(self,substances,self.massFracs)
        self.__setMoleInfo(self.massComp)
    def setMassFracs(self,massFracs):
        self.__setMassComp(self,self.substances,massFracs)
        self.__setMoleInfo(self.massComp)
    def setMassFlow(self,massFlow):
        super().setFlow(massFlow)
        self.__setMoleInfo(self.massComp)
    def setisInfluent(self,isInfluent):
        self.isInfluent = isInfluent
        self.setMassFlow(self.massFlow)
        self.massFlow = self.flow
    
    def getSubstances(self):
        return self.substances
    def getIsInfluent(self):
        return self.isInfluent
    def getMW(self):
        return self.mW
    def getMassFlow(self):
        return self.massFlow
    def getMoleFlow(self):
        return self.moleFlow
    def getMassFracs(self):
        return self.massFracs
    def getMoleFracs(self):
        return self.moleFracs
    def getMassComp(self):
        return self.massComp
    def getMoleComp(self):
        return self.moleComp
    def getSpeciesMassFlow(self):
        return self.speciesMassFlow
    def getSpeciesMoleFlow(self):
        return self.speciesMoleFlow
    def getAtomicMassFlow(self):
        return self.atomicMassFlow
    def getAtomicMoleFlow(self):
        return self.atomicMoleFlow
    
    def __calcMoleFlow(self):
        self.moleFlow = sM.calcMoleFlow(self.speciesMoleFlow)
    def __calcSpeciesFlow(self):
        self.speciesMassFlow = sM.calcSpeciesFlows(self.massComp,
                                                   self.massFlow)
        self.speciesMoleFlow = sM.massToMoleFlows(self.substances,
                                                  self.speciesMassFlow)
    def __calcAtomicFlows(self):
        self.__calcAtomicQuants()
        self.atomicMoleFlow = sM.setAtomFlows(self.atomQuants,
                                               self.moleFlow)
        self.atomicMassFlow = sM.calcAtomMassFlows(self.substances,
                                                   self.atomicMoleFlow)
    def __calcAtomicQuants(self):
        self.atomQuants = sM.setAtomQuantities(self.substances,
                                                   self.moleComp)
    def __calcMW(self):
        self.mW = sM.calcMixtureMW(self.massFlow,self.moleFlow)
    def __cleanup(self):
        massFlow = 1
        speciesMassFlow = sM.calcSpeciesFlows(self.massComp,massFlow)
        speciesMoleFlow = sM.massToMoleFlows(self.substances,speciesMassFlow)
        moleFlow = sM.calcMoleFlow(speciesMoleFlow)
        self.moleFracs,self.moleComp = sM.calcMoleComps(self.substances,
                                                        speciesMoleFlow)
        self.mW = sM.calcMixtureMW(massFlow,moleFlow)
    def copy(self):
        massFlow,isInfluent = sM.copy(self)
        return MaterialStream(self.substances,self.massFracs,massFlow,
                              isInfluent)