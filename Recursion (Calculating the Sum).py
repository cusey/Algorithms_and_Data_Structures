#python 3.5.2


def cal_sum_while(numList):
    
    result = 0
    
    while len(numList) != 0:
        resultTemp = result # FOR PRINT 
        print('numList=' + str( numList) )

        
        result = result + numList[0]
        print('(result = {}) = (result = {}) + (numList[ 0 ]= {} ) '.format(result, resultTemp, numList[0]) )
        # numList[1:]  - Removing first element and make second element the first element
        numList =  numList[1:] 
        
    return result

print( str( cal_sum_while([1,3,2]) ) + ' RETURN' )
print('-'*20 )

'''

numList=[1, 3, 2]
(result = 1) = (result = 0) + (numList[ 0 ]= 1 ) 
numList=[3, 2]
(result = 4) = (result = 1) + (numList[ 0 ]= 3 ) 
numList=[2]
(result = 6) = (result = 4) + (numList[ 0 ]= 2 ) 
6 RETURN
'''


def cal_sum_recursion(numList, print_out):
   if len(numList) != 0:

        print(' {}  + {} '.format(print_out, numList[0]) )
        print_out = print_out +' + ' + str( numList[0] ) 
        # numList[1:]  - Removing first element and make second element the first element
        return cal_sum_recursion(numList[1:], print_out) + numList[0] 
       
   else:
        print( '0 ' + print_out )
        return 0
    
    
print( str( cal_sum_recursion([1,3,2], '') ) + ' RETURN' )
print('-'*20 )

'''
OUTPUT:
   + 1 
  + 1  + 3 
  + 1 + 3  + 2 
0  + 1 + 3 + 2
6 RETURN
--------------------
'''
