# -*- coding: utf-8 -*-
'''
#functions needed:
Preprocessing after preprocessing input:
    [x] Normalize the X and Y with definition2.
    [ ] definition2Use the current cut c to cut both X and Y into smaller pieces. E.g. for N(X), I will have N(X) [0:c], N(X)[c:2c], N(X)[2c:3c]… etc. Same thing goes for N(Y).
    [ ] For each pair of N(X) and N(Y), calculate the Euclidean distance E between each pair with definition 4.
    [ ] Store the results into E0, E1, E2 ….E2 For later retrieval.

'''

testing = True
import numpy as np
def normalize_def2(X):
    '''
    N(x) = (x-x_avg)/sqrt(sum((x-x_avg)^2))
    Args:
        X is an array of floats. 
    Returns: 
        Normalzied(X)
    '''
    X = np.array(X).astype(float)

    denominator = np.sqrt(np.sum([(item-X.mean())**2 for item in X]))
    #testing
    if testing:
        print 'denom',denominator
    result = [(item-X.mean())/denominator for item in X]
    return np.array(result)

if testing:
    print 'normalized',normalize_def2([0,2,4,4,0])
