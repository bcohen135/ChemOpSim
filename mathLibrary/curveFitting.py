# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:10:36 2021
@author: Ben
This file holds curve-fitting methods
"""

import numpy as np
import errorChecks as eC


def leastSquares(x,y):
    '''
    This function performs least squares on a group of equally sized 
    independent and dependent data to create a first order linear relation.
    
    Parameters
    ----------
    x : Array of float64
        Independent Data.
    y : Array of float64
        Dependent Data.
    Returns
    -------
    a : float64
        Slope.
    b : float64
        y-Intercept.
    '''
    'Check the shape of the inputs'
    n = x.shape[0]
    n2 = y.shape[0]
    'Set error to True - no errors triggered'
    err = True
    'Initialize a and b as none'
    a = None
    b = None
    try:
        if n == 0 or n2 == 0: #One or more of the inputs has no values  
            err = False
            raise eC.zeroShape 

        if n !=n2: #the two inputs are not the same shape
            err = False
            raise eC.equalShapeCheck 

        if err: #If no error has been triggered, perform calucations
            sx = np.sum(x)/n
            sxx = np.sum(x*x)/n
            sy = np.sum(y)/n
            sxy = np.sum(x*y)/n

            if sxx == sx**2: #Check divide by 0
                err = False
                raise eC.divideByZero 

        if err: #Solve for a, & b values
            a = (sxy-sx*sy)/(sxx-sx**2)
            b = (sy*sxx-sx*sxy)/(sxx-sx**2)

    #Exceptions
    except eC.equalShapeCheck:
        eC.equalShapeCheck.printOut()
    except eC.zeroShape:
        eC.zeroShape.printOut()
    except eC.divideByZero:
        eC.divideByZero.printOut()
    #Return values
    return a,b

def linearInterp(x,x1,x2,y1,y2):
    '''
    This function performs least squares on a group of equally sized 
    independent and dependent data to create a first order linear relation.
    
    Parameters
    ----------
    x : float64
        Target data.
    x1 : float64
        x-value point 1
    x2 : float64
        x-value point 2
    y1 : float64
        y-value point 1
    y2 : float64
        y-value point 2
    Returns
    -------
    a : float64
        interpolated value
    '''

    try:
        if x1 == x2:#Check divide by zero
            raise eC.divideByZero 

        #Calculations 
        y = y1 + (x-x1)/(x2-x1)*(y2-y1)
    #Exceptions    
    except eC.divideByZero:
        eC.divideByZero.printOut()

    return y 