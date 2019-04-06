#python 3.5.2

def bubbleSort( alist ):
    
    outer_start = len(alist) - 1
    outer_stop = 0
    outer_step = -1 
    
    
    print('Outer Start: ' + str(outer_start) )
    print('Outer Stop:  ' + str(outer_stop) )
    print('Outer Step: ' + str(outer_step) )
    print('START LIST' , alist)
    print('-'*50)

    for passnum in list( range(outer_start , outer_stop, outer_step) ):
        
        for i in range(passnum):
            print(i)
            print('COMPARE[',i, i+1,'] = ', alist)
            
            if alist[i] > alist[i+1]:
                temp = alist[i+1]
                alist[i+1] = alist[i]
                alist[i] = temp
                print('SWAP[',i, i+1,'] = ', alist)
                
            print('-'*50)
        print('-'*50)
                
        
    
    
    
bubbleSort( [2,8,5,3 ] )

'''
OUTPUT:
Outer Start: 3
Outer Stop:  0
Outer Step: -1
START LIST [2, 8, 5, 3]
--------------------------------------------------
0
COMPARE[ 0 1 ] =  [2, 8, 5, 3]
--------------------------------------------------
1
COMPARE[ 1 2 ] =  [2, 8, 5, 3]
SWAP[ 1 2 ] =  [2, 5, 8, 3]
--------------------------------------------------
2
COMPARE[ 2 3 ] =  [2, 5, 8, 3]
SWAP[ 2 3 ] =  [2, 5, 3, 8]
--------------------------------------------------
--------------------------------------------------
0
COMPARE[ 0 1 ] =  [2, 5, 3, 8]
--------------------------------------------------
1
COMPARE[ 1 2 ] =  [2, 5, 3, 8]
SWAP[ 1 2 ] =  [2, 3, 5, 8]
--------------------------------------------------
--------------------------------------------------
0
COMPARE[ 0 1 ] =  [2, 3, 5, 8]
--------------------------------------------------
--------------------------------------------------
