# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:12:14 2021

@author: Ben
"""
from sympy import Eq,solve,Basic

###################################################
#########  Methods for Black Box  #################
###################################################
def sumFlows(streams):
    '''
    sumFlows will sum all influent and effluent flows in the blackBox

    Parameters
    ----------
    streams : list[Stream]
        A list of all streams in and out of the black box

    Returns
    -------
    flow : symbol or float
        the sum of all the streams flowrates.

    '''
    flow = 0
    for stream in streams:
        streamFlow = stream.getFlow()
        flow = flow + streamFlow
    return flow

def solveBox(netFlow,relations,accumulation):
    '''
    solveBox will collect all equations and solve for any unknowns in the 
    black box

    Parameters
    ----------
    netFlow : symbol or float
        the net flow through the black box.
    relations : Eq
        Any custom equations not captured in normal balances.
    accumulation: float
        the amount of material that accumulates in the black box

    Returns
    -------
    sol : dictionary
        all unknowns solved for.

    '''
    equations = relations
    sol = None
    if isinstance(netFlow,Basic):
        balance = Eq(netFlow,accumulation)
        equations.append(balance)
        try:
            sol = solve(equations) 
            for key in sol:
                newVal = sol[key]+1e-08
                sol[key] = float(str(round(newVal,5)).rstrip('0'))
        except:
            sol = 'Unsolved -- Need more information to solve.'
    return sol

def streamDictionary(streams):
    '''
    streamDictionary takes streams and returns a dictionary

    Parameters
    ----------
    streams : list[Stream]
        list of all streams.

    Returns
    -------
    flowVars : dict{str:symbol or float}
        dictionary of flow name:flow rate.

    '''
    flowVars = {}
    fracVars = {}
    k = 1
    for stream in streams:
        thisKey = 'q'+str(k)
        flowVars[thisKey] = stream.getFlow()          
        k += 1
    return flowVars

def reviseStreams(sol,flowVars,streams):
    '''
    reviseStreams will correct all streams to match the black box solution
    
    Parameters
    ----------
    sol : dict{str:float}
        solutions for all unknowns.
    flowVars: dict{str:symbol or float}
        dictionary of all flows paired to the correct streams
    streams: list[Stream]
        list of all streams.

    Returns
    -------
    streams: list[Stream]
        list of all streams.
    '''
    if not isinstance(sol,str) and not sol==None:
        k = 1
        for key in sol:
            if key in flowVars.values() or - key in flowVars.values():
                try:
                    myKey = list(flowVars.keys())[list(flowVars.values()).
                                                  index(key)]
                    flowVars[myKey] = sol[key]
                except:
                    myKey = list(flowVars.keys())[list(flowVars.values()).
                                                  index(-key)]
                    flowVars[myKey] = -sol[key]
                for stream in streams:
                    if stream.getFlow() == key or stream.getFlow() == -key:
                        stream.setFlow(sol[key])
            k += 1
    return streams
###################################################
########  Methods for Unit Operations  ############
###################################################
    def moleFracDictionary(streams):
        flowVars = {}
        k = 1
        for stream in streams:
            m = 1
            for frac in stream.getMoleFlow():
                thisKey = 'x'+str(k)+str(m)
                fracVars[thisKey] = frac
                m+=1
            k+=1
        return fracVars
    
    def atomicDictionary(streams):
        pass
    
    
    def addDictionaries(d1,d2):
        newDict = {}
        for key in d1:
            val1 = d1[key]
            if key in d2:
                val2 = d2[key]
            else:
                val2 = 0
            newVal = val1 + val2
            newDict[key] = newVal
        for key in d2:
            if not key in newDict:
                newDict[key] = d2[key]    
        return newDict