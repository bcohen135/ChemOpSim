# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:18:06 2021

@author: Ben
"""

import unittest as ut

from materials import materialClasses as mC

class testSpecies(ut.TestCase):
    def testSpeciesA(self):
        #Expected Inputs
        spec = mC.Species('H2O1')
        
        expectedMW = 18.015
        expectedAtoms = {'H':2.0,'O':1.0}
        
        self.assertEqual(spec.getMW(),expectedMW)
        self.assertEqual(spec.getAtoms(),expectedAtoms)
        
        copySpec = spec.copy()
        self.assertNotEqual(id(spec),id(copySpec))
        self.assertEqual(spec.getMW(),copySpec.getMW())
        self.assertEqual(spec.getAtoms(),copySpec.getAtoms())
        
    def testSpeciesB(self):
        #None input
        spec = mC.Species(None)
        
        expectedMW = 0
        expectedAtoms = {}
        
        self.assertEqual(spec.getMW(),expectedMW)
        self.assertEqual(spec.getAtoms(),expectedAtoms)
        
        copySpec = spec.copy()
        self.assertNotEqual(id(spec),id(copySpec))
        self.assertEqual(spec.getMW(),copySpec.getMW())
        self.assertEqual(spec.getAtoms(),copySpec.getAtoms())
    
    def testSpeciesC(self):
        #Empty Str input
        spec = mC.Species('')
        
        expectedMW = 0
        expectedAtoms = {}
        
        self.assertEqual(spec.getMW(),expectedMW)
        self.assertEqual(spec.getAtoms(),expectedAtoms)
        
        copySpec = spec.copy()
        self.assertNotEqual(id(spec),id(copySpec))
        self.assertEqual(spec.getMW(),copySpec.getMW())
        self.assertEqual(spec.getAtoms(),copySpec.getAtoms())
        
    def testSpeciesD(self):
        #Invalid Input
        spec = mC.Species('H2O')
        
        expectedMW = 0
        expectedAtoms = {}
        
        self.assertEqual(spec.getMW(),expectedMW)
        self.assertEqual(spec.getAtoms(),expectedAtoms)
        
        copySpec = spec.copy()
        self.assertNotEqual(id(spec),id(copySpec))
        self.assertEqual(spec.getMW(),copySpec.getMW())
        self.assertEqual(spec.getAtoms(),copySpec.getAtoms())
        
    def testSpeciesE(self):
        #Complex Valid Input
        spec = mC.Species('C33H45N3S2O8')
        
        expectedMW = 675.856
        expectedAtoms = {'C':33,'H':45,'N':3,'S':2,'O':8}
        
        self.assertEqual(spec.getMW(),expectedMW)
        self.assertEqual(spec.getAtoms(),expectedAtoms)
        
        copySpec = spec.copy()
        self.assertNotEqual(id(spec),id(copySpec))
        self.assertEqual(spec.getMW(),copySpec.getMW())
        self.assertEqual(spec.getAtoms(),copySpec.getAtoms())
        
    def testSpeciesF(self):
        #Invalid Input
        spec = mC.Species('C1.3H5.3')
        
        expectedMW = 0
        expectedAtoms = {}
        
        self.assertEqual(spec.getMW(),expectedMW)
        self.assertEqual(spec.getAtoms(),expectedAtoms)
        
        copySpec = spec.copy()
        self.assertNotEqual(id(spec),id(copySpec))
        self.assertEqual(spec.getMW(),copySpec.getMW())
        self.assertEqual(spec.getAtoms(),copySpec.getAtoms())
        
    def testSpeciesG(self):
        #No Input
        spec = mC.Species()
        
        expectedMW = 0
        expectedAtoms = {}
        
        self.assertEqual(spec.getMW(),expectedMW)
        self.assertEqual(spec.getAtoms(),expectedAtoms)
        
        copySpec = spec.copy()
        self.assertNotEqual(id(spec),id(copySpec))
        self.assertEqual(spec.getMW(),copySpec.getMW())
        self.assertEqual(spec.getAtoms(),copySpec.getAtoms())
        
    def testSpeciesH(self):
        #Invalid Input
        spec = mC.Species('21')
        
        expectedMW = 0
        expectedAtoms = {}
        
        self.assertEqual(spec.getMW(),expectedMW)
        self.assertEqual(spec.getAtoms(),expectedAtoms)
        
        copySpec = spec.copy()
        self.assertNotEqual(id(spec),id(copySpec))
        self.assertEqual(spec.getMW(),copySpec.getMW())
        self.assertEqual(spec.getAtoms(),copySpec.getAtoms())