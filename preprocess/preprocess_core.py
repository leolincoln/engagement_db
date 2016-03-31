# -*- coding: utf-8 -*-
'''
#functions needed:
Preprocessing after preprocessing input:
    [x] Normalize the X and Y with definition2.
    [x] Use the current cut c to cut both X and Y into smaller pieces. E.g. for N(X), I will have N(X) [0:c], N(X)[c:2c], N(X)[2c:3c]… etc. Same thing goes for N(Y).
    [x] For each pair of N(X) and N(Y), calculate the Euclidean distance E between each pair with definition 4.
    [ ] Store the results into E0, E1, E2 ….E2 For later retrieval.

'''
import sys
testing = True
import numpy as np
def normalize_d2(X):
    '''
    N(x) = (x-x_avg)/sqrt(sum((x-x_avg)^2))
    Args:
        X is an array of floats. 
    Returns: 
        Normalzied(X)
    '''
    #use numpy arrays
    X = np.array(X).astype(float)
    #denominator = sqrt(sum((x-x_avg)^2))
    denominator = np.sqrt(np.sum([(item-X.mean())**2 for item in X]))
    
    if denominator ==0:
        print '0 denominator in normalize_def2'
        sys.exit(1)
    #testing
    if testing:
        print 'denom',denominator
    #(x-x_avg)/denominator
    result = [(item-X.mean())/denominator for item in X]
    return np.array(result)

def cut(X,c):
    '''
    Args:
        X, array of normalized X. Warning: must be normalized
        c, an integer cut for cutting X into [0:c],[c:2c]],[2c:3c].....
    '''
    c = int(c)
    return [X[c*i:c*(i+1)]for i in xrange(len(X)/c)]
def euclidean_d4(X,Y):
    '''
    Et ̄tˆ(X, Y ) = Dt ̄tˆ(Nt ̄tˆ(X), Nt ̄tˆ(Y ))
    Definition 4 
    Args:
        X, Y: arrays of floats. 
    Returns: 
        E from X and Y. 
    '''
    N_x = normalize_d2(X)
    N_y = normalize_d2(Y)
    return np.linalg.norm(N_x-N_y)
def store():
    pass
if testing:
    X = [0,2,4,4,0]
    c =  2
    print 'X',X
    print 'c',c
    N = normalize_d2(X)
    print 'normalized',N
    C = cut(N,c)
    print 'cutted',C
    E = euclidean_d4(X,X) 
    print 'euclidean',E
