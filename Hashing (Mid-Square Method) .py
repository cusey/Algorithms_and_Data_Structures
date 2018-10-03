#python 3.5.2

'''

Another numerical technique for constructing a hash function is called the mid-square method. We first square the item, and 
then extract some portion of the resulting digits. For example, if the item were 44, we would first compute 44^2 =  1,936. 
By extracting the middle two digits, 93, and performing the remainder step, we get 5 (93 % 11). 
 
'''

def midSquare( number ):
    
    number = number ** 2
    
    print('Number Squared: ',number)
    
    noDigits = len(str(number))
    
    print('Number of Digits: ', noDigits )
    
    #Check if odd number of digits
    if noDigits % 2 != 0 : 
        number = number * 10
        print('Made even number digits: ', number)
        
    noDigits = len(str(number))
        
    print('Number of Digits: ', noDigits )
    
    result = str(number)
    
    firstNo = result[int(noDigits/2) -1]
    secondNo = result[int(noDigits/2)]

    return  (int(firstNo) *10) + int(secondNo)

def hash( length ):

    def remainderMethod( number ):
        element = midSquare( number )
        print( element , ' % ', length, ' = ',   element % length)
        return element % length
    
    return remainderMethod 



def insertHash( elementList ):

    resultsList = [None] * len( elementList )
    
    func = hash( len( elementList ) )
    
    for element in elementList:
       index = func(element)
       
       while resultsList [ index ] != None:
           print('Collision Index: ' , index)
            
           #if we at the last element in array go to first element in array
           if index == len( elementList ) -1:
               index = 0
           else:
               index = index +1           
                
       resultsList[index] = element
       
       print( 'Insert Index: ', index) 
       print( resultsList )
       print( '-'*20 )
    
    print( '-'*20 )
    return resultsList
       
            
print ( insertHash( [44,1,13,100,12]  ) )

'''
OUTPUT:

Number Squared:  1936
Number of Digits:  4
Number of Digits:  4
93  %  5  =  3
Insert Index:  3
[None, None, None, 44, None]
--------------------
Number Squared:  1
Number of Digits:  1
Made even number digits:  10
Number of Digits:  2
10  %  5  =  0
Insert Index:  0
[1, None, None, 44, None]
--------------------
Number Squared:  169
Number of Digits:  3
Made even number digits:  1690
Number of Digits:  4
69  %  5  =  4
Insert Index:  4
[1, None, None, 44, 13]
--------------------
Number Squared:  10000
Number of Digits:  5
Made even number digits:  100000
Number of Digits:  6
0  %  5  =  0
Collision Index:  0
Insert Index:  1
[1, 100, None, 44, 13]
--------------------
Number Squared:  144
Number of Digits:  3
Made even number digits:  1440
Number of Digits:  4
44  %  5  =  4
Collision Index:  4
Collision Index:  0
Collision Index:  1
Insert Index:  2
[1, 100, 12, 44, 13]
--------------------
--------------------
[1, 100, 12, 44, 13]

'''

        
    
    

