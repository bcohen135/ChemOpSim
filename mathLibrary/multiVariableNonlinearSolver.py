# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:36:00 2021
@author: Ben
This file holds multi-variable nonlinear solvers
"""

import numpy as np
import errorChecks as eC
import miscMath as mM

def successiveSubstitution(f,x0,tol=1e-07,p=1.0):
    '''
    Parameters
    ----------
    f : method
        input function.
    x0 : array of float64
        initial guess. 
    tol : float64
        tolerance for solution.
    p : float64
        dampening parameter [0,1].
    Returns
    -------
    x : array of float64
        independent value solution
    '''
    err = True #Error is True - good
    x = x0 #Initial Value
    fk = 0
    k = 0 #Initialize counter
    cond = True #Condition record for convergence

    try:
        fk1 = f(x)

        if p<0 or p>1:
             raise eC.invalidInput

        while cond and err:
               #Perform calculations
               fk = fk1
               x = x + p*(fk-x)
               fk1 = f(x)
               k = k+1
               cond = mM.vector1DTolCheck(fk,fk1,tol)

               if k>1e05:#Diverge
                   raise eC.diverge
                   break

    except eC.inavlidInput:
          eC.invalidInput.printOut()
    except eC.diverge:
          eC.diverge.printOut()
    return x

def newtonMethod(f,fp,x0,tol=1e-07):
    '''
    Parameters
    ----------
    f : method
        input function.
    fp : method
        input derivative function.
    x0 : float64
        initial guess. 
    tol : float64
        tolerance for solution.
    Returns
    -------
    x : float64
        independent value solution
    '''

    #Initialize values
    err = True #Error True - good
    x = x0 #First x-values will be x0
    k = 0 #Iteration counter
    cond = True #Condition for convergence

    try: 
        while cond and err:
            fk = f(x) #Initial f values
            print("fk ",fk)
            fpk = fp(x) #Initial fp values
            print("fpk ",fpk)
            #Calculations
            d = np.linalg.solve(fpk, -fk)

            xnew = x + d
            print("xnew: ",xnew)
            print("d: ",d)
            print("x: ",x)
            cond = mM.vector1DTolCheck(xnew,x,tol)

            x = xnew
            k = k+1
            if k>1e05:
                raise eC.diverge
    #Exceptions
    except eC.diverge:
        eC.diverge.printOut()
    return x