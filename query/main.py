import sys

def main():
    if len(sys.argv)<3:
        print 'ERROR: call with python main.py t1 t2'
    else:
        print 't1,t2',t1, t2

if __name__ == '__main__':
    main()
