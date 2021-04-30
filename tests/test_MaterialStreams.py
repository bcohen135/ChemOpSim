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
        stream = stms.MaterialStream(specs,[0.3,0.25,0.45],10,True)
        
        expectedMoleFlow = 0.3737
        expectedMW = 26.75943
        expectedMassComp = {'C1H4':0.3,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMoleComp = {'C1H4':0.5004,'H2O1':0.37134,
                            'Na1Cl2':0.12826}
        expectedSpeciesMassFlow = {'C1H4':3.0,'H2O1':2.5,'Na1Cl2':4.5}
        expectedSpeciesMoleFlow = {'C1H4':0.187,'H2O1':0.13877,
                                   'Na1Cl2':0.04793}
        expectedAtomicMassFlow = {'C':2.24606,'H':1.03374,'O':2.22018,
                                  'Na':1.10191,'Cl':3.39824}
        expectedAtomicMoleFlow = {'C':0.187,'H':1.02554,'O':0.13877,
                                  'Na':0.04793,'Cl':0.09586}
        
        self.assertEqual(expectedMoleFlow,stream.getMoleFlow())
        self.assertEqual(expectedMW,stream.getMW())
        self.assertDictContainsSubset(expectedMassComp,stream.getMassComp())
        self.assertDictContainsSubset(expectedMoleComp,stream.getMoleComp())
        self.assertDictContainsSubset(expectedSpeciesMassFlow,
                                      stream.getSpeciesMassFlow())
        self.assertDictContainsSubset(expectedSpeciesMoleFlow,
                                      stream.getSpeciesMoleFlow())
        self.assertDictContainsSubset(expectedAtomicMassFlow,
                                      stream.getAtomicMassFlow())
        self.assertDictContainsSubset(expectedAtomicMoleFlow,
                                      stream.getAtomicMoleFlow())
        
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
        
    def testMaterialStreamB(self):
        #No input
        stream = stms.MaterialStream()
        
        expectedMoleFlow = 0
        expectedMW = 0
        expectedMassComp = {}
        expectedMoleComp = {}
        expectedSpeciesMassFlow = {}
        expectedSpeciesMoleFlow = {}
        expectedAtomicMassFlow = {}
        expectedAtomicMoleFlow = {}
        
        self.assertEqual(expectedMoleFlow,stream.getMoleFlow())
        self.assertEqual(expectedMW,stream.getMW(),expectedMW)
        self.assertDictContainsSubset(expectedMassComp,stream.getMassComp())
        self.assertDictContainsSubset(expectedMoleComp,stream.getMoleComp())
        self.assertDictContainsSubset(expectedSpeciesMassFlow,
                                      stream.getSpeciesMassFlow())
        self.assertDictContainsSubset(expectedSpeciesMoleFlow,
                                      stream.getSpeciesMoleFlow())
        self.assertDictContainsSubset(expectedAtomicMassFlow,
                                      stream.getAtomicMassFlow())
        self.assertDictContainsSubset(expectedAtomicMoleFlow,
                                      stream.getAtomicMoleFlow())
        
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamC(self):
        #Non-numeric flow
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        q = symbols('q')
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.3,0.25,0.45],'q',True)
        
        expectedMoleFlow = 0.03737*q
        expectedMW = 26.76
        expectedMassComp = {'C1H4':0.3,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMoleComp = {'C1H4':0.5004,'H2O1':0.3714,
                            'Na1Cl2':0.1282}
        expectedSpeciesMassFlow = {'C1H4':0.3*q,'H2O1':0.25*q,'Na1Cl2':0.45*q}
        expectedSpeciesMoleFlow = {'C1H4':0.0187*q,'H2O1':0.01388*q,
                                   'Na1Cl2':0.00479*q}
        expectedAtomicMassFlow = {'C':0.2246*q,'H':0.10338*q,'O':0.22207*q,
                                  'Na':0.11013*q,'Cl':0.33963*q}
        expectedAtomicMoleFlow = {'C':0.0187*q,'H':0.10256*q,'O':0.01388*q,
                                  'Na':0.00479*q,'Cl':0.00958*q}
        
        self.assertEqual(str(expectedMoleFlow),str(stream.getMoleFlow()))
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        for key in expectedSpeciesMassFlow:    
            self.assertEqual(str(expectedSpeciesMassFlow[key]),
                             str(stream.getSpeciesMassFlow()[key]))
            self.assertEqual(str(expectedSpeciesMoleFlow[key]),
                             str(stream.getSpeciesMoleFlow()[key]))
        for key in expectedAtomicMassFlow:
            self.assertEqual(str(expectedAtomicMassFlow[key]),
                             str(stream.getAtomicMassFlow()[key]))
            self.assertEqual(str(expectedAtomicMoleFlow[key]),
                             str(stream.getAtomicMoleFlow()[key]))
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamD(self):
        #Non-numeric mole fraction
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        x = symbols('x')
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,['x',0.25,0.45],10,True)
        
        expectedMoleFlow = 0.62332*x + 0.1867
        expectedMW = 10/(0.62332*x + 0.1867)
        expectedMassComp = {'C1H4':x,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMoleComp = {'C1H4':0.62332*x/(0.62332*x + 0.1867),
                            'H2O1':0.13877/(0.62332*x + 0.1867),
                            'Na1Cl2':0.04793/(0.62332*x + 0.1867)}
        expectedSpeciesMassFlow = {'C1H4': 10*x, 'H2O1': 2.5, 'Na1Cl2': 4.5} 
        expectedSpeciesMoleFlow = {'C1H4': 0.62332*x, 'H2O1': 0.13877, 
                                   'Na1Cl2': 0.04793} 
        expectedAtomicMassFlow = {'C': 7.48669*x, 
                                  'H': '1.008*(0.62332*x + 0.1867)*(2.49328*x/(0.62332*x + 0.1867) + 0.27754/(0.62332*x + 0.1867))', 
                                  'O': 2.22018, 'Na': 1.10191, 'Cl': 3.39822}  
        expectedAtomicMoleFlow = {'H': (0.62332*x + 0.1867)*(2.49328*x/(0.62332*x + 0.1867) + 0.27754/(0.62332*x + 0.1867)), 
                                  'C': 0.62332*x, 'O': 0.13877, 'Cl': 0.09586,
                                  'Na': 0.04793}  
        
        self.assertEqual(str(expectedMoleFlow),str(stream.getMoleFlow()))
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        for key in expectedSpeciesMassFlow:    
            self.assertEqual(str(expectedSpeciesMassFlow[key]),
                             str(stream.getSpeciesMassFlow()[key]))
            self.assertEqual(str(expectedSpeciesMoleFlow[key]),
                             str(stream.getSpeciesMoleFlow()[key]))
        for key in expectedAtomicMassFlow:
            self.assertEqual(str(expectedAtomicMassFlow[key]),
                             str(stream.getAtomicMassFlow()[key]))
            self.assertEqual(str(expectedAtomicMoleFlow[key]),
                             str(stream.getAtomicMoleFlow()[key]))
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
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
        
        expectedMoleFlow = 0.06233*q*x + 0.05551*q*y + 0.01065*q*z
        expectedMW = q/(0.06233*q*x + 0.05551*q*y + 0.01065*q*z)
        expectedMassComp = {'C1H4': 'x', 'H2O1': 'y', 'Na1Cl2': 'z'}
        expectedMoleComp = {'C1H4': 0.06233*q*x/(0.06233*q*x + 0.05551*q*y + 0.01065*q*z),
                            'H2O1': 0.05551*q*y/(0.06233*q*x + 0.05551*q*y + 0.01065*q*z), 
                            'Na1Cl2': 0.01065*q*z/(0.06233*q*x + 0.05551*q*y + 0.01065*q*z)} 
        expectedSpeciesMassFlow = {'C1H4': q*x, 'H2O1': q*y, 'Na1Cl2': q*z} 
        expectedSpeciesMoleFlow = {'C1H4': 0.06233*q*x, 'H2O1': 0.05551*q*y, 
                                   'Na1Cl2': 0.01065*q*z}  
        expectedAtomicMassFlow = {'C': 0.74864*q*x, 
                                  'H': '1.008*(0.24932*q*x/(0.06233*q*x + 0.05551*q*y + 0.01065*q*z) + 0.11102*q*y/(0.06233*q*x + 0.05551*q*y + 0.01065*q*z))*(0.06233*q*x + 0.05551*q*y + 0.01065*q*z)',
                                  'O': 0.88811*q*y,
                                  'Na': 0.24484*q*z, 'Cl': 0.75509*q*z}  
        expectedAtomicMoleFlow = {'H': (0.24932*q*x/(0.06233*q*x + 0.05551*q*y + 0.01065*q*z) + 0.11102*q*y/(0.06233*q*x + 0.05551*q*y + 0.01065*q*z))*(0.06233*q*x + 0.05551*q*y + 0.01065*q*z), 
                                  'C': 0.06233*q*x, 'O': 0.05551*q*y, 
                                  'Cl': 0.0213*q*z, 'Na': 0.01065*q*z} 
        
        self.assertEqual(str(expectedMoleFlow),str(stream.getMoleFlow()))
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        for key in expectedSpeciesMassFlow:    
            self.assertEqual(str(expectedSpeciesMassFlow[key]),
                             str(stream.getSpeciesMassFlow()[key]))
            self.assertEqual(str(expectedSpeciesMoleFlow[key]),
                             str(stream.getSpeciesMoleFlow()[key]))
        for key in expectedAtomicMassFlow:
            self.assertEqual(str(expectedAtomicMassFlow[key]),
                             str(stream.getAtomicMassFlow()[key]))
            self.assertEqual(str(expectedAtomicMoleFlow[key]),
                             str(stream.getAtomicMoleFlow()[key]))
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamF(self):
        #Expected Inputs
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.3,0.25,0.45],10,False)
        
        expectedMoleFlow = -0.3737
        expectedMW = 26.75943
        expectedMassComp = {'C1H4': 0.3, 'H2O1': 0.25, 'Na1Cl2': 0.45}
        expectedMoleComp = {'C1H4': 0.5004, 'H2O1': 0.37134, 'Na1Cl2': 0.12826} 
        expectedSpeciesMassFlow = {'C1H4': -3.0, 'H2O1': -2.5, 'Na1Cl2': -4.5}  
        expectedSpeciesMoleFlow = {'C1H4': -0.187, 'H2O1': -0.13877, 
                                   'Na1Cl2': -0.04793}   
        expectedAtomicMassFlow = {'C': -2.24606, 'H': -1.03374, 'O': -2.22018,
                                  'Na': -1.10191, 'Cl': -3.39824}  
        expectedAtomicMoleFlow = {'H': -1.02554, 'C': -0.187, 'O': -0.13877,
                                  'Cl': -0.09586, 'Na': -0.04793} 
        
        self.assertEqual(str(expectedMoleFlow),str(stream.getMoleFlow()))
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        for key in expectedSpeciesMassFlow:    
            self.assertEqual(str(expectedSpeciesMassFlow[key]),
                             str(stream.getSpeciesMassFlow()[key]))
            self.assertEqual(str(expectedSpeciesMoleFlow[key]),
                             str(stream.getSpeciesMoleFlow()[key]))
        for key in expectedAtomicMassFlow:
            self.assertEqual(str(expectedAtomicMassFlow[key]),
                             str(stream.getAtomicMassFlow()[key]))
            self.assertEqual(str(expectedAtomicMoleFlow[key]),
                             str(stream.getAtomicMoleFlow()[key]))
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
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
        
        expectedMoleFlow = -0.06233*q*x - 0.05551*q*y - 0.01065*q*z
        expectedMW = -q/(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z)
        expectedMassComp = {'C1H4': 'x', 'H2O1': 'y', 'Na1Cl2': 'z'}
        expectedMoleComp = {'C1H4': -0.06233*q*x/(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z), 
                            'H2O1': -0.05551*q*y/(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z), 
                            'Na1Cl2': -0.01065*q*z/(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z)} 
        expectedSpeciesMassFlow = {'C1H4': -q*x, 'H2O1': -q*y, 'Na1Cl2': -q*z} 
        expectedSpeciesMoleFlow = {'C1H4': -0.06233*q*x, 'H2O1': -0.05551*q*y, 
                                   'Na1Cl2': -0.01065*q*z}  
        expectedAtomicMassFlow = {'C': -0.74864*q*x, 
                                  'H': '1.008*(-0.24932*q*x/(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z) - 0.11102*q*y/(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z))*(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z)',
                                  'O': -0.88811*q*y, 'Na': -0.24484*q*z, 
                                  'Cl': -0.75509*q*z}  
        expectedAtomicMoleFlow = {'H': (-0.24932*q*x/(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z) - 0.11102*q*y/(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z))*(-0.06233*q*x - 0.05551*q*y - 0.01065*q*z), 
                                  'C': -0.06233*q*x, 'O': -0.05551*q*y, 
                                  'Cl': -0.0213*q*z, 'Na': -0.01065*q*z}  
        
        self.assertEqual(str(expectedMoleFlow),str(stream.getMoleFlow()))
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        for key in expectedSpeciesMassFlow:    
            self.assertEqual(str(expectedSpeciesMassFlow[key]),
                             str(stream.getSpeciesMassFlow()[key]))
            self.assertEqual(str(expectedSpeciesMoleFlow[key]),
                             str(stream.getSpeciesMoleFlow()[key]))
        for key in expectedAtomicMassFlow:
            self.assertEqual(str(expectedAtomicMassFlow[key]),
                             str(stream.getAtomicMassFlow()[key]))
            self.assertEqual(str(expectedAtomicMoleFlow[key]),
                             str(stream.getAtomicMoleFlow()[key]))
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamH(self):
        #Species input only
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs)
        
        expectedMoleFlow = 0
        expectedMW = 0
        expectedMassComp = {}
        expectedMoleComp = {}
        expectedSpeciesMassFlow = {}
        expectedSpeciesMoleFlow = {}
        expectedAtomicMassFlow = {}
        expectedAtomicMoleFlow = {}
        
        self.assertEqual(expectedMoleFlow,stream.getMoleFlow())
        self.assertEqual(expectedMW,stream.getMW(),expectedMW)
        self.assertDictContainsSubset(expectedMassComp,stream.getMassComp())
        self.assertDictContainsSubset(expectedMoleComp,stream.getMoleComp())
        self.assertDictContainsSubset(expectedSpeciesMassFlow,
                                      stream.getSpeciesMassFlow())
        self.assertDictContainsSubset(expectedSpeciesMoleFlow,
                                      stream.getSpeciesMoleFlow())
        self.assertDictContainsSubset(expectedAtomicMassFlow,
                                      stream.getAtomicMassFlow())
        self.assertDictContainsSubset(expectedAtomicMoleFlow,
                                      stream.getAtomicMoleFlow())
        
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamI(self):
        #Species and fraction inputs only
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.3,0.25,0.45])
        
        expectedMoleFlow = 0.0
        expectedMW = 26.75943
        expectedMassComp = {'C1H4':0.3,'H2O1':0.25,'Na1Cl2':0.45}
        expectedMoleComp = {'C1H4':0.5004,'H2O1':0.37142,
                            'Na1Cl2':0.12818}
        expectedSpeciesMassFlow = {'C1H4':0,'H2O1':0,'Na1Cl2':0}
        expectedSpeciesMoleFlow = {'C1H4':0,'H2O1':0,
                                   'Na1Cl2':0}
        expectedAtomicMassFlow = {'C':0,'H':0,'O':0,
                                  'Na':0,'Cl':0}
        expectedAtomicMoleFlow = {'C':0,'H':0,'O':0,
                                  'Na':0,'Cl':0}
        
        self.assertEqual(expectedMoleFlow,stream.getMoleFlow())
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        self.assertDictContainsSubset(expectedSpeciesMassFlow,
                                      stream.getSpeciesMassFlow())
        self.assertDictContainsSubset(expectedSpeciesMoleFlow,
                                      stream.getSpeciesMoleFlow())
        self.assertDictContainsSubset(expectedAtomicMassFlow,
                                      stream.getAtomicMassFlow())
        self.assertDictContainsSubset(expectedAtomicMoleFlow,
                                      stream.getAtomicMoleFlow())
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamJ(self):
        #Invalid input
        stream = stms.MaterialStream([0.25,0.3,0.45])
        
        expectedMoleFlow = 0
        expectedMW = 0
        expectedMassComp = {}
        expectedMoleComp = {}
        expectedSpeciesMassFlow = {}
        expectedSpeciesMoleFlow = {}
        expectedAtomicMassFlow = {}
        expectedAtomicMoleFlow = {}
        
        self.assertEqual(str(expectedMoleFlow),str(stream.getMoleFlow()))
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        self.assertDictContainsSubset(expectedSpeciesMassFlow,
                                      stream.getSpeciesMassFlow())
        self.assertDictContainsSubset(expectedSpeciesMoleFlow,
                                      stream.getSpeciesMoleFlow())
        self.assertDictContainsSubset(expectedAtomicMassFlow,
                                      stream.getAtomicMassFlow())
        self.assertDictContainsSubset(expectedAtomicMoleFlow,
                                      stream.getAtomicMoleFlow())
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamK(self):
        #None input
        stream = stms.MaterialStream(None)
        
        expectedMoleFlow = 0
        expectedMW = 0
        expectedMassComp = {}
        expectedMoleComp = {}
        expectedSpeciesMassFlow = {}
        expectedSpeciesMoleFlow = {}
        expectedAtomicMassFlow = {}
        expectedAtomicMoleFlow = {}
        
        self.assertEqual(str(expectedMoleFlow),str(stream.getMoleFlow()))
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        self.assertDictContainsSubset(expectedSpeciesMassFlow,
                                      stream.getSpeciesMassFlow())
        self.assertDictContainsSubset(expectedSpeciesMoleFlow,
                                      stream.getSpeciesMoleFlow())
        self.assertDictContainsSubset(expectedAtomicMassFlow,
                                      stream.getAtomicMassFlow())
        self.assertDictContainsSubset(expectedAtomicMoleFlow,
                                      stream.getAtomicMoleFlow())
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamL(self):
        #None input for species with valid fraction input
        stream = stms.MaterialStream(None,[0.25,0.3,0.45])
        
        expectedMoleFlow = 0
        expectedMW = 0
        expectedMassComp = {}
        expectedMoleComp = {}
        expectedSpeciesMassFlow = {}
        expectedSpeciesMoleFlow = {}
        expectedAtomicMassFlow = {}
        expectedAtomicMoleFlow = {}
        
        self.assertEqual(str(expectedMoleFlow),str(stream.getMoleFlow()))
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        self.assertDictContainsSubset(expectedSpeciesMassFlow,
                                      stream.getSpeciesMassFlow())
        self.assertDictContainsSubset(expectedSpeciesMoleFlow,
                                      stream.getSpeciesMoleFlow())
        self.assertDictContainsSubset(expectedAtomicMassFlow,
                                      stream.getAtomicMassFlow())
        self.assertDictContainsSubset(expectedAtomicMoleFlow,
                                      stream.getAtomicMoleFlow())
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())
        
    def testMaterialStreamM(self):
        #Mole fraction input != 1
        spec1 = self.spec1.copy()
        spec2 = self.spec2.copy()
        spec3 = self.spec3.copy()
        specs = [spec1,spec2,spec3]
        stream = stms.MaterialStream(specs,[0.2,0.3,0.45])
        
        expectedMoleFlow = 0
        expectedMW = 29.48983
        expectedMassComp = {'C1H4':0.2,'H2O1':0.3,'Na1Cl2':0.45}
        expectedMoleComp = {'C1H4':0.36774,'H2O1':0.49101,'Na1Cl2':0.14126}
        expectedSpeciesMassFlow = {'C1H4': 0.0, 'H2O1': 0.0, 'Na1Cl2': 0.0}
        expectedSpeciesMoleFlow = {'C1H4': 0.0, 'H2O1': 0.0, 'Na1Cl2': 0.0}
        expectedAtomicMassFlow = {'C': 0.0, 'H': 0.0, 'O': 0.0, 'Na': 0.0, 'Cl': 0.0}
        expectedAtomicMoleFlow = {'C': 0.0, 'H': 0.0, 'O': 0.0, 'Na': 0.0, 'Cl': 0.0}
        
        self.assertEqual(expectedMoleFlow,stream.getMoleFlow())
        self.assertEqual(str(expectedMW),str(stream.getMW()))
        for key in expectedMassComp:
            self.assertEqual(str(expectedMassComp[key]),
                             str(stream.getMassComp()[key]))
        for key in expectedMoleComp:
            self.assertEqual(str(expectedMoleComp[key]),
                             str(stream.getMoleComp()[key]))
        self.assertDictContainsSubset(expectedSpeciesMassFlow,
                                      stream.getSpeciesMassFlow())
        self.assertDictContainsSubset(expectedSpeciesMoleFlow,
                                      stream.getSpeciesMoleFlow())
        self.assertDictContainsSubset(expectedAtomicMassFlow,
                                      stream.getAtomicMassFlow())
        self.assertDictContainsSubset(expectedAtomicMoleFlow,
                                      stream.getAtomicMoleFlow())
            
        copyStream = stream.copy()
        self.assertNotEqual(id(copyStream),id(stream))
        self.assertEqual(stream.getMassFlow(),copyStream.getMassFlow())
        self.assertEqual(stream.getIsInfluent(),copyStream.getIsInfluent())
        self.assertEqual(stream.getMoleFlow(),copyStream.getMoleFlow())