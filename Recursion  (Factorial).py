#python 3.5.2

def factorial(n):
    
    if n == 1:
        print( ' {} '.format(n ) )
        print('-'*20)
        return n
    else:
        print(' {}  * factorial ( {} )'.format(n, n-1) )
        return n * factorial( n -1 )
    
    

    
print( factorial( 5 ) )


'''
OUTPUT:

 5  * factorial ( 4 )
 4  * factorial ( 3 )
 3  * factorial ( 2 )
 2  * factorial ( 1 )
 1 
--------------------
120

'''