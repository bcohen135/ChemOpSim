# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:44:45 2021
@author: Ben
This file has the matrix math functions
"""

import numpy as np
import errorChecks as eC

def vector1DTolCheck(v1,v2,tol):
    '''
    Parameters
    ----------
    v1 : Array of float64
        1-D Vector 1.
    v2 : Array of float64
        1-D Vector 2.
    tol : float64
        Tolerance.
    Returns
    -------
    inTol : Boolean
        True - in tolerance
        False - out of tolerance.
    '''
    n1 = v1.shape[0]
    n2 = v2.shape[0]
    inTol = True

    if n1 != n2:
        eC.equalShapeCheck.printOut
    else:
        for k in range(0,n1-1):
            if abs(v1[k]-v2[k])>tol:
                inTol = True
            else:
                inTol = False
                break      
    return inTol

def discretize(f,x1,x2,n=100):
    x = np.linspace(x1,x2,num = n)
    y = f(x)

    return x,y 