# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:01:29 2021

@author: Ben
"""

import unittest as ut
from sympy import symbols

from streams import streams as stms

class testStreams(ut.TestCase):
    def testStreamA(self):
        #Expected Input
        testStream = stms.Stream(8.0,True)
        
        expectedFlow = 8.0
        
        self.assertEqual(testStream.getFlow(),expectedFlow)
        self.assertTrue(testStream.getIsInfluent())
        
        copyTestStream = testStream.copy()
        self.assertNotEqual(id(testStream),id(copyTestStream))
        self.assertEqual(testStream.getFlow(),copyTestStream.getFlow())
        self.assertEqual(testStream.getIsInfluent(),
                         copyTestStream.getIsInfluent())
        
    def testStreamB(self):
        #Expected Input
        testStream = stms.Stream(8,True)
        
        expectedFlow = 8.0
        
        self.assertEqual(testStream.getFlow(),expectedFlow)
        self.assertTrue(testStream.getIsInfluent())
        
        copyTestStream = testStream.copy()
        self.assertNotEqual(id(testStream),id(copyTestStream))
        self.assertEqual(testStream.getFlow(),copyTestStream.getFlow())
        self.assertEqual(testStream.getIsInfluent(),
                         copyTestStream.getIsInfluent())
    
    def testStreamC(self):
        #Expected Input
        testStream = stms.Stream(8,False)
        
        expectedFlow = -8.0
        
        self.assertEqual(testStream.getFlow(),expectedFlow)
        self.assertFalse(testStream.getIsInfluent())
        
        copyTestStream = testStream.copy()
        self.assertNotEqual(id(testStream),id(copyTestStream))
        self.assertEqual(testStream.getFlow(),copyTestStream.getFlow())
        self.assertEqual(testStream.getIsInfluent(),
                         copyTestStream.getIsInfluent())
        
    def testStreamD(self):
        #No Input
        testStream = stms.Stream()
        
        expectedFlow = 0
        
        self.assertEqual(testStream.getFlow(),expectedFlow)
        self.assertTrue(testStream.getIsInfluent())
        
        copyTestStream = testStream.copy()
        self.assertNotEqual(id(testStream),id(copyTestStream))
        self.assertEqual(testStream.getFlow(),copyTestStream.getFlow())
        self.assertEqual(testStream.getIsInfluent(),
                         copyTestStream.getIsInfluent())
        
    def testStreamE(self):
        #Non-numeric Input
        q = symbols('q')
        testStream = stms.Stream('q',True)
        
        expectedFlow = q
        
        self.assertEqual(testStream.getFlow(),expectedFlow)
        self.assertTrue(testStream.getIsInfluent())
        
        copyTestStream = testStream.copy()
        self.assertNotEqual(id(testStream),id(copyTestStream))
        self.assertEqual(testStream.getFlow(),copyTestStream.getFlow())
        self.assertEqual(testStream.getIsInfluent(),
                         copyTestStream.getIsInfluent())
        
    def testStreamF(self):
        #None input
        testStream = stms.Stream(None)
        
        expectedFlow = 0
        
        self.assertEqual(testStream.getFlow(),expectedFlow)
        self.assertTrue(testStream.getIsInfluent())
        
        copyTestStream = testStream.copy()
        self.assertNotEqual(id(testStream),id(copyTestStream))
        self.assertEqual(testStream.getFlow(),copyTestStream.getFlow())
        self.assertEqual(testStream.getIsInfluent(),
                         copyTestStream.getIsInfluent())
        
    def testStreamG(self):
        #Non-numeric Input
        q = symbols('q')
        testStream = stms.Stream('q',False)
        
        expectedFlow = -q
        
        self.assertEqual(testStream.getFlow(),expectedFlow)
        self.assertFalse(testStream.getIsInfluent())
        
        copyTestStream = testStream.copy()
        self.assertNotEqual(id(testStream),id(copyTestStream))
        self.assertEqual(testStream.getFlow(),copyTestStream.getFlow())
        self.assertEqual(testStream.getIsInfluent(),
                         copyTestStream.getIsInfluent())
        
    def testStreamH(self):
        #Invalid Input
        testStream = stms.Stream(False)
        
        expectedFlow = 0
        
        self.assertEqual(testStream.getFlow(),expectedFlow)
        self.assertTrue(testStream.getIsInfluent())
        
        copyTestStream = testStream.copy()
        self.assertNotEqual(id(testStream),id(copyTestStream))
        self.assertEqual(testStream.getFlow(),copyTestStream.getFlow())
        self.assertEqual(testStream.getIsInfluent(),
                         copyTestStream.getIsInfluent())