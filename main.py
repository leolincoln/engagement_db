from preprocess.preprocess_core import cut,E_,store
from glob import glob
import numpy as np
import os,sys

def get_keys():
    return [os.path.basename(item) for item in glob('db_storage/keys/*')]

def modify():
    print 'modify function not implemented'
    pass

def main_menu():
    print 'welcome'
    print '1: create new data set'
    print '2: modify existing data set'
    print '3: destroy exisiting data set'
    print '4: exit'
    number_entered = raw_input('\n')
    if number_entered not in ['1','2','3','4']:
        print 'invalid option. '
        main_menu()
    else:
        if number_entered == '1':
            create()
        if number_entered == '2':
            modify()
        if number_entered == '3':
            destroy()
        else:
            sys.exit(0)

def destroy():
    '''
    1.self.Remove db_storage/KEY folder
    2.self.Remove KEY file in db_storage/keys/ 
    '''
    print 'please enter key to be removed'
    keys = get_keys()
    print 'avaiable keys are: ', keys
    key = raw_input()
    if key not in keys:
        print 'your key is invalid. Please enter again'
        destroy()
    else:
        print 'are you sure you want to destroy key',key,'?'
        choice = raw_input('y')
        if choice.lower()!='y':
            main_menu()
        print 'removing db_storage/'+key,'folder'
        os.system('rm -rf db_storage/'+key)
        print 'removing key file db_storage/keys/'+key
        os.system('rm -rf db_storage/keys/'+key)
        print 'remove key',key,'successful'
        main_menu()

def create():
    print 'Enter X'
    X = raw_input().split(',')
    print 'Enter Y'
    Y = raw_input().split(',')
    print 'Enter cut c'
    #TODO, checking c needed
    c = int(raw_input())
    print 'Enter Key'
    key = raw_input()
    print 'enter description'
    desc = raw_input()
    #now process the Entered X,Y,c,key,desc
    #if succesful, print sucessfully processed Key
    #return to main menu
    X = np.array(X).astype(float)
    Y = np.array(Y).astype(float)
    store(X,Y,c,key,desc)
    main_menu()

def main():
    main_menu()

if __name__ == '__main__':
    main()
