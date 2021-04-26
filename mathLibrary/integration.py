# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:57:34 2021
@author: Ben
This file has numerical integration methods
"""

import errorChecks as eC
import miscMath as mM

def trapezoidalRule(x,y):
    '''
    Parameters
    ----------
    x : Array of float64
        independent variable.
    y : Array of float64
        dependent variable.
    Returns
    -------
    integral : float64
        integration of discrete function y(x)
    '''
    #Get shape of vectors
    nx = x.shape[0]
    ny = y.shape[0]

    #Initialize integral value
    integral = 0

    try:
        if nx != ny: #Check to see if x and y are the same size
            raise eC.equalShapeCheck
        if nx == 0: #Check to see if the input is valid
            raise eC.zeroShape

        #Perofrm calculations
        for n in range(0,nx-1):
            adder = 0.5*(x[n+1]-x[n])*(y[n+1]+y[n])
            integral = integral+adder
    #Exceptions
    except eC.equalShapeCheck:
        eC.equalShapeCheck.printOut()
    except eC.zeroShape:
        eC.zeroShape.printOUt()
    return integral

def simpsonsRule(x,y):
    '''
    Simpson's rule can only be used when the x-values are regularly spaced
    Parameters
    ----------
    x : Array of float64
        independent variable.
    y : Array of float64
        dependent variable.
    Returns
    -------
    integral : float64
        integration of discrete function y(x)
    '''
    #Get shape of vectors
    nx = x.shape[0]
    ny = y.shape[0]

    try:
        if nx != ny: #Make sure x and y are the same shape
            raise eC.equalShapeCheck
        if nx == 0: #Check to see if the input is valid
            raise eC.zeroShape 

        #Find delta x to be used
        h = x[1]-x[0]

        #Initialize values
        sum1 = 0
        sum2 = 0
        for n in range(1,nx-1): #Perform calculations
            if n%2 == 0:
                sum1 = sum1 + y[n]
            if n%2 == 1:
                sum2 = sum2 + y[n]

        integral = (h/3)*(y[0]+y[n]+4*sum1+2*sum2)
    #Exceptions 
    except eC.equalShapeCheck:
        eC.equalShapeCheck.printOut()
    except eC.zeroShape:
        eC.zeroShape.printOut()
    return integral 