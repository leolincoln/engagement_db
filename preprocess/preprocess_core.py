# -*- coding: utf-8 -*-
'''
#functions needed:
Preprocessing after preprocessing input:
    [x] Normalize the X and Y with definition2.
    [x] Use the current cut c to cut both X and Y into smaller pieces. E.g. for N(X), I will have N(X) [0:c], N(X)[c:2c], N(X)[2c:3c]… etc. Same thing goes for N(Y).
    [x] For each pair of N(X) and N(Y), calculate the Euclidean distance E between each pair with definition 4.
    [ ] Store the results into E0, E1, E2 ….E2 For later retrieval.

'''
import sys,os
testing = False
import numpy as np
def N_(X):
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

def E_(X,Y):
    '''
    Et ̄tˆ(X, Y ) = Dt ̄tˆ(Nt ̄tˆ(X), Nt ̄tˆ(Y ))
    Definition 4 
    Args:
        X, Y: arrays of floats. 
    Returns: 
        E from X and Y. 
    '''
    N_x = N_(X)
    N_y = N_(Y)
    return np.linalg.norm(N_x-N_y)**2

def store(X,Y,c,key,desc,key_path = '/keys/'):
    '''
    Store the euclidean distance of c in files. from X and Y
    E(X[0:c],Y[0:c]) --- file ../db_store/key/0_1
    E(X[c:2c],Y[c:2c]) -- file ../db_store/key/1_2
    E(X[2c:3c],[Y[2c:3c]]) -- file ../db_store/key/2_3
    '''
    cutX = cut(X,c)
    cutY = cut(Y,c)
    for i in xrange(len(cutX)):
        file_name = str(i)+'_'+str(c)+'.dt'
        dir_path = get_storage_path()+key+'/'
        full_path = dir_path+file_name
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(full_path,'w') as f:
            f.write(str(E_(cutX[i],cutY[i])))
    with open(get_storage_path()+key_path+key,'w') as f:
        f.write(desc)
    return True 

def get_storage_path():
    full_path = os.path.realpath(__file__)
    dir_name = (os.path.dirname(full_path))
    return dir_name+'/../db_storage/'

if testing:
    X = [0,2,4,4,0]
    c =  2
    print 'X',X
    print 'c',c
    N = N_(X)
    print 'normalized',N
    C = cut(N,c)
    print 'cutted',C
    E = E_(X,X) 
    print 'euclidean',E
