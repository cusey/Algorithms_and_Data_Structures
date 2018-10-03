#python 3.5.2

'''
With the Remained Methods first you count the number of elements you what to store. So the length of the 
array will eaual the number of elements you want so each element will have place to be stored. When you
do the divide by array length the remainer will always to equal or less than the number of element in the
array.

The folding method for constructing hash functions begins by dividing the item into equal-size pieces 
(the last piece may not be of equal size). These pieces are then added together to give the resulting 
hash value. For example, if our item was the phone number 436-555-4601, we would take the digits and 
divide them into groups of 2 (43,65,55,46,01). After the addition, 43+65+55+46+01, we get 210. 
If we assume our hash table has 11 slots, then we need to perform the extra step of dividing by 
11 and keeping the remainder. In this case 210 % 11 is 1, so the phone number 436-555-4601 hashes 
to slot 1. Some folding methods go one step further and reverse every other piece before the addition.
 For the above example, we get 43+56+55+64+01=219 which gives 219 % 11=10.
 
'''

def convertPhoneNo(phoneNo):
    firstNo = int(phoneNo[0])*10 + int(phoneNo[1])
    secondNo = int(phoneNo[2])*10 + int(phoneNo[4])
    thirdNo = int(phoneNo[5])*10 + int(phoneNo[6])
    fourthNo = int(phoneNo[8])*10 + int(phoneNo[9])
    fifthNo = int(phoneNo[10])*10 + int(phoneNo[11])
    result =firstNo+secondNo+thirdNo+fourthNo+fifthNo
    print( phoneNo ," = ", result )
    return result


def hash( length ):

    def remainderMethod(phoneNo):
        element = convertPhoneNo(phoneNo)
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
       
            
print ( insertHash( ['436-555-4601','436-555-4600','436-555-4611','436-555-4621','436-555-4634']  ) )

'''
OUTPUT:

436-555-4601  =  210
210  %  5  =  0
Insert Index:  0
['436-555-4601', None, None, None, None]
--------------------
436-555-4600  =  209
209  %  5  =  4
Insert Index:  4
['436-555-4601', None, None, None, '436-555-4600']
--------------------
436-555-4611  =  220
220  %  5  =  0
Collision Index:  0
Insert Index:  1
['436-555-4601', '436-555-4611', None, None, '436-555-4600']
--------------------
436-555-4621  =  230
230  %  5  =  0
Collision Index:  0
Collision Index:  1
Insert Index:  2
['436-555-4601', '436-555-4611', '436-555-4621', None, '436-555-4600']
--------------------
436-555-4634  =  243
243  %  5  =  3
Insert Index:  3
['436-555-4601', '436-555-4611', '436-555-4621', '436-555-4634', '436-555-4600']
--------------------
--------------------
['436-555-4601', '436-555-4611', '436-555-4621', '436-555-4634', '436-555-4600']

'''

        
    
    
