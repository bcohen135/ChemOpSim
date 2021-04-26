# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:05:14 2021

@author: Ben
"""
from sympy import Eq,solve,Basic,symbols
from streams import streams as stms

from unitOperations import unitOperationMethods as uOM

class BlackBox():
    '''
    A BlackBox is an object that serves as parent of all unit operations
    Attributes:
        streams: streams that go in (+) or out (-) of black box
        relations: mathematic relations between any variables
        accumulation: The amount that is accumuulated in black box
            + for increase "level"
            - for decrease "level"
        netFlow: The net flow in the blackbox
        solution: any variable solutions will be held in solution
        flowVars: a dictionary of {general variable name: value or symbol}
            ex. {'q1':8,'q2':q,'q3':w}
        
    '''
    def __init__(self,streams=[],relations=[],accumulation=0):
        if not isinstance(streams,list):
            streams = []
        self.__initAddStream(streams)
        self.relations = relations
        self.accumulation = accumulation
        self.__calcNetFlow()
        self.__solveBox()
        self.__setFlowVars()
        self.__balanceBox()
        
    def __initAddStream(self,streams):
        self.streams = []
        for stream in streams:
            self.addStream(stream)
            
    def addStream(self,stream):
        self.streams.append(stream.copy())
        self.__setFlowVars()
    
    def addRelation(self,relation):
        self.relations.append(relation)
        
    def setAccumulation(self,accumulation):
        self.accumulation = accumulation
    
    def getStreams(self):
        return self.streams
    
    def getNetFlow(self):
        return self.netFlow
    
    def getAccumulation(self):
        return self.accumulation
    
    def getSolution(self):
        return self.solution
    
    def getFlowVars(self):
        return self.flowVars
    
    def __calcNetFlow(self):
        netFlow = uOM.sumFlows(self.streams)
        self.netFlow = netFlow
    
    def __solveBox(self):
        self.solution = uOM.solveBox(self.netFlow,self.relations,
                                     self.accumulation)
        
    def __setFlowVars(self):
        self.flowVars = uOM.streamDictionary(self.streams)
    
    def __balanceBox(self):
        self.streams = uOM.reviseStreams(self.solution,self.flowVars,
                                         self.streams)
    
    def copy(self):
        return BlackBox(self.streams,self.relations,self.accumulation)

        
class UnitOperation(BlackBox):
    def __init__(self,streams=0,relations=0):
        super().__init__(streams,relations,0) #No accumulation yet
        
        
    def addStream(self,stream):
        super().addStream(stream)
        
    def addRelation(self,relation):
        super().addRelation()
        
    def setAccumulation(self,accumulation):
        super().setAccumulation()
        
    def getFracVars(self):
        pass
    
    def __calcNetSpeciesFlow(self):
        pass
    
    def __solveUnitOp(self):
        pass
    
    def __setFracVars(self):
        pass
    
    def __balanceBox(self):
        pass
        

class EquilibriumReactor(BlackBox):
    pass

class KineticReactor(BlackBox):
    pass

class ProcessSeparation(BlackBox):
    pass 