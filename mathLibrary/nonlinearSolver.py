# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:11:22 2021
@author: Ben
This file holds single variable nonlinear solvers
"""

import errorChecks as eC

def regulaFalsi(f, xn, xp, tol=1e-07):
    '''
    Parameters
    ----------
    f : method
        input function.
    xn : float64
        Lower bound estimate.
    xp : float64
        Upper bound estimate.
    tol : float64
        tolerance for solution
    Returns
    -------
    sol : float64
        independent value solution
    '''

    sol = None #Initialize sol

    'find initial values for lower and upper bounds'
    fp = f(xp)
    fn = f(xn)

    err = True #Initialize error as true (no error)
    k = 0 #Initialize counter for divergence criteria

    try:
        if fp == fn: #Divide by zero catch
            err = False
            raise eC.divideByZero

        'solve for new x value'
        xnew = (xn*fp - xp*fn)/(fp-fn)
        fnew = f(xnew)


        'iterate through to find solution'
        while abs(fnew) > tol and err:
            if fnew<0: #Set new lower bound
                xn = xnew
                fn = f(xn)
            elif fnew>0: #Set new upper bound
                xp = xnew
                fp = f(xp)

            if fp == fn: #Divide by zero catch
                err = False
                raise eC.divideByZero
                break

            if k > 1e07: #Convergence criteria
                k = -1
                raise eC.diverge
                break
            'solve new x value'
            xnew = (xn*fp - xp*fn)/(fp-fn)
            fnew = f(xnew)
            k = k+1
        'record solution for output'
        sol = xnew
    #Exceptions
    except eC.divideByZero:
        eC.divideByZero.printOut()
    except eC.diverge:
        eC.diverge.printOut()

    return sol

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
    x = x0 #First x-value will be x0
    fk = f(x0) #Initial f value 
    k = 0 #Counter

    try:
        while abs(fk)>tol and err:
            #Calculate function and derivative
            fk = f(x)
            fpk = fp(x)

            if fpk == 0: #Divide by zero check
                err = False
                raise eC.divideByZero
                break
            #Exceute Newton's Method
            x = x - (fk/fpk)

            if k>1e07: #Divergence check
                k = -1
                raise eC.diverge
                break
            #Increment counter
            k = k+1
    #Exceptions
    except eC.divideByZero:
        eC.divideByZero.printOut()
    except eC.diverge:
        eC.diverge.printOut()

    return x

def successiveSubstitution(f,x0,tol=1e-07,p=1.0):
    '''
    Parameters
    ----------
    f : method
        input function.
    x0 : float64
        initial guess. 
    tol : float64
        tolerance for solution.
    p : float64
        dampening parameter [0,1].
    Returns
    -------
    x : float64
        independent value solution
    '''

    err = True #Error is True - good
    x = x0 #Initial x-value
    fk = 0
    fk1 = f(x)
    k = 0 #Initialize counter

    try:
        if p < 0 or p>1: #Check valid input
            raise eC.invalidInput

        while abs(fk-fk1)>tol and err:
            #Perform calculations
            fk = fk1
            x = x + p*(fk-x)
            fk1 = f(x)
            k = k+1

            if k > 1e05:#Diverges
                raise eC.diverge
                break
    #Exceptions
    except eC.invalidInput:
        eC.invalidInput.printOut()
    except eC.diverge:
        eC.diverge.printOut()
    return x

def wegsteinAlgorithm(f,x0,tol=1e-07,qmin=-5.0,qmax =0.5):
    '''
    Parameters
    ----------
    f : method
        input function.
    x0 : float64
        initial guess. 
    tol : float64
        tolerance for solution.
    qmin : float64
        minimum wegstein factor
    qmax : float64
        maximum wegstein factor
    Returns
    -------
    x : float64
        independent value solution
    '''

    err = True #Error is True - good
    x1 = x0 #Initial x-value
    fk1 = f(x1)
    x2 = fk1
    fk2 = f(x2)
    k = 0 #Initialize counter

    try:
        if qmin>qmax:
            raise eC.invalidInput

        while abs(fk1-fk2)>tol and err:
            #Perform calculations
            w = (fk1-fk2)/(x1-x2)
            q = w/(w-1)

            if q > qmin:
                q = qmin
            if q < qmax:
                q = qmax

            x1 = x2
            x2 = q*x2 + (1-q)*f(x2)

            fk1 = fk2
            fk2 = f(x2)
            k = k+1

            if k>1e05: #Diverges
                raise eC.diverge
                break
    #Exceptions
    except eC.invalidInput:
        eC.invalidInput.printOut()
    except eC.diverge:
        eC.diverge.printOut()
    return x2 