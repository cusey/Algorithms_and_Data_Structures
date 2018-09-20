#python 3.5.2

def convertBase(number, base):
    
    convertString = '0123456789ABCDEF'
    result = ''
    
    while number != 0:
        print( ' {} {}'.format(convertString [number % base ] , result)  ) 
        result = convertString [number % base ] + result
        number = number // base
    return result

def recConvertBase(number, base):
    
    convertString = '0123456789ABCDEF'
    
    if number != 0:
       print(' recConvertBase( {} ,{})  {} )'.format(number // base , base , convertString [number % base ])  ) 
       return recConvertBase(number // base, base) + convertString [number % base ]
    else:
       return '' 
        
    
print('-'*20)        
        
print( convertBase(48879, 16) )

print('-'*20)

print (recConvertBase(48879, 16) ) 

print('-'*20)

'''
OUTPUT:

--------------------
 F 
 E F
 E EF
 B EEF
BEEF
--------------------
 recConvertBase( 3054 ,16)  F )
 recConvertBase( 190 ,16)  E )
 recConvertBase( 11 ,16)  E )
 recConvertBase( 0 ,16)  B )
BEEF
--------------------

'''