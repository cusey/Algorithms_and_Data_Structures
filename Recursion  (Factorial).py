#python 3.5.2

def factorial(n):
    
    result = 1
    
    while n != 1:
        print( '{}  * {}'.format(result, n) )
        result = result * n
        
        n = n -1
        
    return result 


def recfactorial(n):
    
    if n == 1:
        print( ' {} '.format(n ) )
        
        return n
    else:
        print(' {}  * recfactorial ( {} )'.format(n, n-1) )
        return n * recfactorial( n -1 )
    
    
    
print( factorial( 5 ) )   
print('-'*20)
    
print( recfactorial( 5 ) )
print('-'*20)


'''
OUTPUT:

1  * 5
5  * 4
20  * 3
60  * 2
120
--------------------
 5  * recfactorial ( 4 )
 4  * recfactorial ( 3 )
 3  * recfactorial ( 2 )
 2  * recfactorial ( 1 )
 1 
120
--------------------

'''
