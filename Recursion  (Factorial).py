#python 3.5.2

def fact_while(n):
    
    result = 1
    
    while n != 1:
        result_temp = result # FOR PRINT
        
        result = result * n
        print( '(result= {}) = (result= {})  * (n= {})'.format( result, result_temp, n) )
        
        n = n -1
        
    return result 

print( fact_while( 3 ) )   
print('-'*20)

'''
(result= 3) = (result= 1)  * (n= 3)
(result= 6) = (result= 3)  * (n= 2)
6
--------------------
'''


def fact_recurion(n , print_out):
    
    if n != 1:
        print_out = print_out + str(n) + '*'
        return n * fact_recurion( n -1 , print_out)    
 
    else:  
      print( print_out + str(n) )
      return n
    
    
print( fact_recurion( 3 , '' ) )
print('-'*20)

'''
3*2*1
6
--------------------
'''

'''
