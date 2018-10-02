#python 3.5.2

'''
With the Remained Methods first you count the number of elements you what to store. So the length of the 
array will eaual the number of elements you want so each element will have place to be stored. When you
do the divide by array length the remainer will always to equal or less than the number of element in the
array.
'''

def hash( length ):

    def remainderMethod(element):
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
       
            
print ( insertHash( [3,5,9,11,15,17,22]  ) )

'''
OUTPUT:

3  %  7  =  3
Insert Index:  3
[None, None, None, 3, None, None, None]
--------------------
5  %  7  =  5
Insert Index:  5
[None, None, None, 3, None, 5, None]
--------------------
9  %  7  =  2
Insert Index:  2
[None, None, 9, 3, None, 5, None]
--------------------
11  %  7  =  4
Insert Index:  4
[None, None, 9, 3, 11, 5, None]
--------------------
15  %  7  =  1
Insert Index:  1
[None, 15, 9, 3, 11, 5, None]
--------------------
17  %  7  =  3
Collision Index:  3
Collision Index:  4
Collision Index:  5
Insert Index:  6
[None, 15, 9, 3, 11, 5, 17]
--------------------
22  %  7  =  1
Collision Index:  1
Collision Index:  2
Collision Index:  3
Collision Index:  4
Collision Index:  5
Collision Index:  6
Insert Index:  0
[22, 15, 9, 3, 11, 5, 17]
--------------------
--------------------
[22, 15, 9, 3, 11, 5, 17]

'''

        
    
    
