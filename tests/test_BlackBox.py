# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 08:13:04 2021

@author: Ben
"""

import unittest as ut
from sympy import symbols,Eq

from unitOperations import unitOperations as uO
from streams import streams as stms

class testBlackBox(ut.TestCase):
    def __init__(self,*args,**kwargs):
        super(testBlackBox,self).__init__(*args,**kwargs)
        self.stream1 = stms.Stream(8,True)
        self.stream2 = stms.Stream(8,False)
        self.stream3 = stms.Stream(5.2,True)
        self.stream4 = stms.Stream('q',True)
        self.stream5 = stms.Stream('q',False)
        self.stream6 = stms.Stream('w',True)
        self.stream7 = stms.Stream('u')
        
    def testBlackBoxA(self):
        #Expected Inputs
        stream1 = self.stream1
        stream2 = self.stream2
        stream3 = self.stream3
        streams = [stream1,stream2,stream3]
        relations = []
        accumulation = 2.1
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = 5.2
        expectedCopyNetFlow = 5.2
        expectedSolution = None
        expectedFlowVars = {'q1':8,'q2':-8,'q3':5.2}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxB(self):
        #No Inputs
        testBB = uO.BlackBox()
        
        expectedNetFlow = 0
        expectedCopyNetFlow = 0
        expectedSolution = None
        expectedFlowVars = {}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxC(self):
        #One Stream with non-numeric flow
        stream1 = self.stream1
        stream2 = self.stream3
        stream3 = self.stream5
        q = symbols('q')
        streams = [stream1,stream2,stream3]
        relations = []
        accumulation = 0
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = 13.2-q
        expectedCopyNetFlow = 0
        expectedSolution = {q:13.2}
        expectedFlowVars = {'q1':8,'q2':5.2,'q3':-13.2}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxD(self):
        #One Stream with non-numeric flow and accumulated flow != 0
        stream1 = self.stream1
        stream2 = self.stream3
        stream3 = self.stream5
        q = symbols('q')
        streams = [stream1,stream2,stream3]
        relations = []
        accumulation = 3
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = 13.2-q
        expectedCopyNetFlow = accumulation
        expectedSolution = {q:10.2}
        expectedFlowVars = {'q1':8,'q2':5.2,'q3':-10.2}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxE(self):
        #Two streams with non-numeric flow and one relation no accumulation
        stream1 = self.stream1
        stream2 = self.stream5
        stream3 = self.stream6
        q = symbols('q')
        w = symbols('w')
        streams = [stream1,stream2,stream3]
        rel1 = Eq(q-5*w)
        relations = [rel1]
        accumulation = 0
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = -q+w+8
        expectedCopyNetFlow = 0
        expectedSolution = {q:10,w:2}
        expectedFlowVars = {'q1':8,'q2':-10,'q3':2}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxF(self):
        #All streams non-numeric and two relations no accumulation
        stream1 = self.stream5
        stream2 = self.stream6
        stream3 = self.stream7
        q = symbols('q')
        w = symbols('w')
        u = symbols('u')
        streams = [stream1,stream2,stream3]
        rel1 = Eq(q-4*w,0)
        rel2 = Eq(u-w,4)
        relations = [rel1,rel2]
        accumulation = 0
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = -q+w+u
        expectedCopyNetFlow = 0
        expectedSolution = {q:8,w:2,u:6}
        expectedFlowVars = {'q1':-8,'q2':2,'q3':6}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getSolution(),expectedSolution)
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxG(self):
        #Two streams with non-numeric flow and one relation and accumulation
        stream1 = self.stream1
        stream2 = self.stream5
        stream3 = self.stream6
        q = symbols('q')
        w = symbols('w')
        streams = [stream1,stream2,stream3]
        rel1 = Eq(q-5*w)
        relations = [rel1]
        accumulation = 2.0
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = -q+w+8
        expectedCopyNetFlow = accumulation
        expectedSolution = {q:7.5,w:1.5}
        expectedFlowVars = {'q1':8,'q2':-7.5,'q3':1.5}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxH(self):
        #All streams non-numeric and two relations no accumulation
        stream1 = self.stream5
        stream2 = self.stream6
        stream3 = self.stream7
        q = symbols('q')
        w = symbols('w')
        u = symbols('u')
        streams = [stream1,stream2,stream3]
        rel1 = Eq(q-4*w,0)
        rel2 = Eq(u-w,4)
        relations = [rel1,rel2]
        accumulation = 2
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = -q+w+u
        expectedCopyNetFlow = accumulation
        expectedSolution = {q:4,w:1,u:5}
        expectedFlowVars = {'q1':-4,'q2':1,'q3':5}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxI(self):
        #Expected Inputs
        stream1 = self.stream1
        stream2 = self.stream2
        stream3 = self.stream3
        streams = [stream1,stream2,stream3]
        relations = []
        accumulation = -2.0
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = 5.2
        expectedCopyNetFlow = 5.2
        expectedSolution = None
        expectedFlowVars = {'q1':8,'q2':-8,'q3':5.2}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxJ(self):
        #One non-numeric stream and negative accumulation
        stream1 = self.stream1
        stream2 = self.stream3
        stream3 = self.stream5
        q = symbols('q')
        streams = [stream1,stream2,stream3]
        relations = []
        accumulation = -2.0
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = 13.2-q
        expectedCopyNetFlow = accumulation
        expectedSolution = {q:15.2}
        expectedFlowVars = {'q1':8,'q2':5.2,'q3':-15.2}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxK(self):
        #All streams non-numeric and two relations no accumulation
        stream1 = self.stream5
        stream2 = self.stream6
        stream3 = self.stream7
        q = symbols('q')
        w = symbols('w')
        u = symbols('u')
        streams = [stream1,stream2,stream3]
        rel1 = Eq(q-4*w,0)
        rel2 = Eq(u-w,4)
        relations = [rel1,rel2]
        accumulation = -2
        testBB = uO.BlackBox(streams,relations,accumulation)
        
        expectedNetFlow = -q+w+u
        expectedCopyNetFlow = accumulation
        expectedSolution = {q:12,w:3,u:7}
        expectedFlowVars = {'q1':-12,'q2':3,'q3':7}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxL(self):
        #None input
        testBB = uO.BlackBox(None)
        
        expectedNetFlow = 0
        expectedCopyNetFlow = 0
        expectedSolution = None
        expectedFlowVars = {}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxM(self):
        #Boolean input
        testBB = uO.BlackBox(False)
        
        expectedNetFlow = 0
        expectedCopyNetFlow = 0
        expectedSolution = None
        expectedFlowVars = {}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxN(self):
        #All streams non-numeric and two relations accumulation omitted
        stream1 = self.stream5
        stream2 = self.stream6
        stream3 = self.stream7
        q = symbols('q')
        w = symbols('w')
        u = symbols('u')
        streams = [stream1,stream2,stream3]
        rel1 = Eq(q-4*w,0)
        rel2 = Eq(u-w,4)
        relations = [rel1,rel2]
        testBB = uO.BlackBox(streams,relations)
        
        expectedNetFlow = -q+w+u
        expectedCopyNetFlow = 0
        expectedSolution = {q:8,w:2,u:6}
        expectedFlowVars = {'q1':-8,'q2':2,'q3':6}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None:
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getSolution(),expectedSolution)
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(None,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    def testBlackBoxO(self):
        #All streams non-numeric relations and accumulation omitted
        stream1 = self.stream5
        stream2 = self.stream6
        stream3 = self.stream7
        q = symbols('q')
        w = symbols('w')
        u = symbols('u')
        streams = [stream1,stream2,stream3]
        testBB = uO.BlackBox(streams)
        
        expectedNetFlow = -q+w+u
        expectedCopyNetFlow = expectedNetFlow
        expectedSolution = 'Unsolved -- Need more information to solve.'
        expectedFlowVars = {'q1':-q,'q2':w,'q3':u}
        
        self.assertEqual(testBB.getNetFlow(),expectedNetFlow)
        if expectedSolution == None or isinstance(expectedSolution,str):
            self.assertEqual(testBB.getSolution(),expectedSolution)
        else:
            self.assertDictContainsSubset(expectedSolution,
                                          testBB.getSolution())
        self.assertEqual(testBB.getSolution(),expectedSolution)
        self.assertEqual(testBB.getFlowVars(),expectedFlowVars)
        
        copyTestBB = testBB.copy()
        self.assertNotEqual(id(testBB),id(copyTestBB))
        self.assertEqual(expectedCopyNetFlow,copyTestBB.getNetFlow())
        self.assertEqual(expectedSolution,copyTestBB.getSolution())
        self.assertEqual(testBB.getFlowVars(),copyTestBB.getFlowVars())
        
    