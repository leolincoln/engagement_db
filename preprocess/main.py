import sys



#main takes in 3 parameters, X,Y and c. 
#X is the X series, 
#Y is the Y series, 
#c is the cut
def main():
    if len(sys.argv)<4:
        print 'preprocess needs 3 parameters, X, Y and c where X and Y are comma seperated arrays, c is the integer value of our cut. '
        sys.exit(1)
    X = sys.argv[1].split(',')
    Y = sys.argv[2].split(',')
    c = int(sys.argv[3])
    print 'parameters:',X,Y,c





if __name__=='__main__':
    main()
