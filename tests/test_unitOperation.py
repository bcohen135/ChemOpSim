# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:11:04 2021

@author: Ben
"""

import unittest as ut
from sympy import symbols,Eq

from unitOperations import unitOperations as uO
from streams import streams as stms
from materials import materialClasses as mC

class testUnitOperation(ut.TestCase):
    def __init__(self,*args,**kwargs):
        super(testUnitOperation,self).__init__(*args,**kwargs)
        water = mC.Species('H2O1')
        methane = mC.Species('C1H4') 
        co2 = mC.Species('C1O2')
        co = mC.Species('C1O1')
        hydrogen = mC.Species('H2')
        nitrogen = mC.Species('N2')
        salt = mC.Species('Na1Cl2')
        oxygen = mC.Species('O2')
        self.ms1 = stms.MaterialStream([oxygen,nitrogen],[0.21,0.79],8)
        self.ms2 = stms.MaterialStream([methane],[1],5)
        self.ms3 = stms.MaterialStream([methane,co2,co,water],
                                       [0.5,0.2,0.1,0.2],3)
        self.ms4 = stms.MaterialStream([salt,water],['a','b'],4)
        self.ms5 = stms.MaterialStream([hydrogen,oxygen,water],
                                       ['c',0.2,0.4],2)
        self.ms6 = stms.MaterialStream([hydrogen,oxygen,water],
                                       ['d','e',0.4],2)
        self.ms7 = stms.MaterialStream([oxygen,nitrogen],[0.21,0.79],'f')
        self.ms8 = stms.MaterialStream([methane,co2,co],['g','h','k'],'m')
        self.ms9 = stms.MaterialStream([oxygen,nitrogen],[0.21,0.79],8,False)
        self.ms10 = stms.MaterialStream([methane],[1],5,False)
        self.ms11 = stms.MaterialStream([methane,co2,co,water],
                                       [0.5,0.2,0.1,0.2],3,False)
        self.ms12 = stms.MaterialStream([salt,water],['n','o'],4,False)
        self.ms13 = stms.MaterialStream([hydrogen,oxygen,water],
                                       ['p',0.2,0.4],2,False)
        self.ms14 = stms.MaterialStream([hydrogen,oxygen,water],
                                       ['q','r',0.4],2,False)
        self.ms15 = stms.MaterialStream([oxygen,nitrogen],[0.21,0.79],'s',
                                        False)
        self.ms16 = stms.MaterialStream([methane,co2,co],['x','y','z'],'u',
                                        False)
        
