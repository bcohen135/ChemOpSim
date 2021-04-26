# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:50:09 2021

@author: Ben
"""

import unittest as ut
from sympy import symbols

from materials import materialClasses as mC
from streams import streams as stms
 
class testMaterialStream(ut.TestCase):
    def __init__(self,*args,**kwargs):
        super(testMaterialStream,self).__init__(*args,**kwargs)
        self.spec1 = mC.Species('C1H4')
        self.spec2 = mC.Species('H2O1')
        self.spec3 = mC.Species('Na1Cl2')
        
    def testMaterialStreamA(self):
        #Expected Inputs
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.3,0.25,0.45],6,True)
        
        expectedMoleFracs = [0.3,0.25,0.45]
        expectedMoleFlow = 6
        expectedMoleComp = {'C1H4':0.3,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMW = 51.56715
        expectedSpeciesFlow = {'C1H4':1.8,'H2O1':1.5,'Na1Cl2':2.7}
        expectedAtomQuants = {'C':0.3,'H':1.7,'O':0.25,'Na':0.45,'Cl':0.9}
        expectedAtomicFlows = {'C':1.8,'H':10.2,'O':1.5,'Na':2.7,'Cl':5.4}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamB(self):
        #No input
        stream = stms.MaterialStream()
        
        expectedMoleFracs = []
        expectedMoleFlow = 0
        expectedMoleComp = {}
        expectedMW = 0
        expectedSpeciesFlow = {}
        expectedAtomQuants = {}
        expectedAtomicFlows = {}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamC(self):
        #Non-numeric flow
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        q = symbols('q')
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.3,0.25,0.45],'q',True)
        
        expectedMoleFracs = [0.3,0.25,0.45]
        expectedMoleFlow = q
        expectedMoleComp = {'C1H4':0.3,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMW = 51.56715
        expectedSpeciesFlow = {'C1H4':0.3*q,'H2O1':0.25*q,'Na1Cl2':0.45*q}
        expectedAtomQuants = {'O': 0.25, 'C': 0.3, 'Cl': 0.9,'Na': 0.45,
                              'H':1.7}
        expectedAtomicFlows = {'O': 0.25*q, 'C': 0.3*q, 'Cl': 0.9*q,
                               'Na': 0.45*q, 'H': 1.7*q}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamD(self):
        #Non-numeric mole fraction
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        x = symbols('x')
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,['x',0.25,0.45],6,True)
        
        expectedMoleFracs = [x,0.25,0.45]
        expectedMoleFlow = 6
        expectedMoleComp = {'C1H4':x,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMW = 16.043*x+46.75425
        expectedSpeciesFlow = {'C1H4':6*x,'H2O1':1.5,'Na1Cl2':2.7}
        expectedAtomQuants = {'C':1.0*x,'H':4.0*x+0.5,'O':0.25,'Na':0.45,
                                 'Cl':0.9}
        expectedAtomicFlows = {'C':6.0*x,'H':24.0*x+3.0,'O':1.5,'Na':2.7,
                                 'Cl':5.4}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamE(self):
        #No numeric inputs
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        x = symbols('x')
        y = symbols('y')
        z = symbols('z')
        q = symbols('q')
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,['x','y','z'],'q',True)
        
        expectedMoleFracs = [x,y,z]
        expectedMoleFlow = q
        expectedMoleComp = {'C1H4':x,'H2O1':y,'Na1Cl2':z}
        expectedMW = 16.043*x+18.015*y+93.89*z
        expectedSpeciesFlow = {'C1H4':x*q,'H2O1':q*y,'Na1Cl2':q*z}
        expectedAtomQuants = {'O':1.0*y,'C':1.0*x,'Cl':2.0*z,'Na':1.0*z,
                                 'H':4.0*x+2.0*y}
        expectedAtomicFlows = {'O':1.0*q*y,'C':1.0*q*x,'Cl':2.0*z*q,
                                 'Na':1.0*q*z,'H':q*(4.0*x+2.0*y)}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamF(self):
        #Expected Inputs
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.3,0.25,0.45],6,False)
        
        expectedMoleFracs = [0.3,0.25,0.45]
        expectedMoleFlow = -6
        expectedMoleComp = {'C1H4':0.3,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMW = 51.56715
        expectedSpeciesFlow = {'C1H4':-1.8,'H2O1':-1.5,'Na1Cl2':-2.7}
        expectedAtomQuants = {'C':0.3,'H':1.7,'O':0.25,'Na':0.45,'Cl':0.9}
        expectedAtomicFlows = {'C':-1.8,'H':-10.2,'O':-1.5,'Na':-2.7,'Cl':-5.4}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamG(self):
        #Non-numeric inputs
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        x = symbols('x')
        y = symbols('y')
        z = symbols('z')
        q = symbols('q')
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,['x','y','z'],'q',False)
        
        expectedMoleFracs = [x,y,z]
        expectedMoleFlow = -q
        expectedMoleComp = {'C1H4':x,'H2O1':y,'Na1Cl2':z}
        expectedMW = 16.043*x+18.015*y+93.89*z
        expectedSpeciesFlow = {'C1H4':-x*q,'H2O1':-q*y,'Na1Cl2':-q*z}
        expectedAtomQuants = {'O':1.0*y,'C':1.0*x,'Cl':2.0*z,'Na':1.0*z,
                                 'H':4.0*x+2.0*y}
        expectedAtomicFlows = {'O':-1.0*q*y,'C':-1.0*q*x,'Cl':-2.0*z*q,
                                 'Na':-1.0*q*z,'H':-q*(4.0*x+2.0*y)}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamH(self):
        #Species input only
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs)
        
        expectedMoleFracs = []
        expectedMoleFlow = 0
        expectedMoleComp = {}
        expectedMW = 0
        expectedSpeciesFlow = {}
        expectedAtomQuants = {}
        expectedAtomicFlows = {}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamI(self):
        #Species and fraction inputs only
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.3,0.25,0.45])
        
        expectedMoleFracs = [0.3,0.25,0.45]
        expectedMoleFlow = 0
        expectedMoleComp = {'C1H4':0.3,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMW = 51.56715
        expectedSpeciesFlow = {'C1H4':0,'H2O1':0,'Na1Cl2':0}
        expectedAtomQuants = {'C':0.3,'H':1.7,'O':0.25,'Na':0.45,'Cl':0.9}
        expectedAtomicFlows = {'C':0,'H':0,'O':0,'Na':0,'Cl':0}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamJ(self):
        #Invalid input
        stream = stms.MaterialStream([0.25,0.3,0.45])
        
        expectedMoleFracs = []
        expectedMoleFlow = 0
        expectedMoleComp = {}
        expectedMW = 0
        expectedSpeciesFlow = {}
        expectedAtomQuants = {}
        expectedAtomicFlows = {}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamK(self):
        #None input
        stream = stms.MaterialStream(None)
        
        expectedMoleFracs = []
        expectedMoleFlow = 0
        expectedMoleComp = {}
        expectedMW = 0
        expectedSpeciesFlow = {}
        expectedAtomQuants = {}
        expectedAtomicFlows = {}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamL(self):
        #None input for species with valid fraction input
        stream = stms.MaterialStream(None,[0.25,0.3,0.45])
        
        expectedMoleFracs = [0.25,0.3,0.45]
        expectedMoleFlow = 0
        expectedMoleComp = {}
        expectedMW = 0
        expectedSpeciesFlow = {}
        expectedAtomQuants = {}
        expectedAtomicFlows = {}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())
        
    def testMaterialStreamM(self):
        #Mole fraction input != 1
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.2,0.3,0.45])
        
        expectedMoleFracs = [0.21053,0.31579,0.47368]
        expectedMoleFlow = 0
        expectedMoleComp = {'C1H4':0.21053,'H2O1':0.31579,'Na1Cl2':0.47368}
        expectedMW = 53.540305
        expectedSpeciesFlow = {'C1H4':0,'H2O1':0,'Na1Cl2':0}
        expectedAtomQuants = {'C':0.21053,'O':0.31579,'H':1.4737,'Na':0.47368,
                              'Cl':0.94736}
        expectedAtomicFlows = {'C':0,'O':0,'H':0,'Na':0,'Cl':0}
        
        self.assertEqual(stream.getMoleFracs(),expectedMoleFracs)
        self.assertEqual(stream.getMoleFlow(),expectedMoleFlow)
        self.assertEqual(stream.getMoleComp(),expectedMoleComp)
        self.assertEqual(stream.getMW(),expectedMW)
        self.assertEqual(stream.getSpeciesFlow(),expectedSpeciesFlow)
        self.assertEqual(stream.getAtomQuants(),expectedAtomQuants)
        self.assertEqual(stream.getAtomicFlows(),expectedAtomicFlows)
        
        copyStream = stream.copy()
        self.assertNotEqual(id(stream),id(copyStream))
        self.assertEqual(stream.getMoleFracs(),copyStream.getMoleFracs())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        self.assertEqual(stream.getMoleComp(),copyStream.getMoleComp())
        self.assertEqual(stream.getMW(),copyStream.getMW())
        self.assertEqual(stream.getSpeciesFlow(),copyStream.getSpeciesFlow())
        self.assertEqual(stream.getAtomQuants(),copyStream.getAtomQuants())
        self.assertEqual(stream.getAtomicFlows(),copyStream.getAtomicFlows())