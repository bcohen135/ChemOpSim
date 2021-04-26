# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:29:26 2021

@author: Ben
"""
from materials import materialMethods as mM

class Species():
    '''
    A Species is a molecule that can be added to a material.
    Attributes:
        formula: the chemical formula of the molecule
        mW: the molecular weight of the molecule
        atoms: a dictionary of the atoms and number of atoms in molecule
    Methods:
        get and set methods
        calcAtoms: calculates the number of atoms based on the chemical
            formula. Outputs the atoms dictionary
        __calcMW: calculates the molecular weight of the molecule
        copy: makes a copy of the object
        
    '''
    def __init__(self,formula=None):
        self.setFormula(formula)
                    
    def setFormula(self,formula):
        self.formula = formula
        self.mW = 0
        self.atoms = {}
        if formula !=None:
            self.__calcAtoms()
            self.__calcMW()
    
    def getFormula(self):
        return self.formula
    
    def getMW(self):
        return self.mW
    
    def getAtoms(self):
        return self.atoms
    
    def __calcAtoms(self):
        self.atoms = mM.parseFormula(self.getFormula())
    
    def __calcMW(self): #See materialMethods for method details
        self.mW = mM.calcMW(self.atoms)
        
    def copy(self):
        return Species(self.formula)