#python 3.5.2

'''
alist = [ 0,1,2,3,4,5,6,7,8,9]

print ( alist[ :3] )
print ( alist[3:]  )
'''


'''
[0, 1, 2]
[3, 4, 5, 6, 7, 8, 9]
'''


def convertIntToList(number):
    tempList = []
    tempList.append(number)
    return tempList

def printList( alist ):
    print('New Array is:', alist)
    print( '-'*20 )
    return alist

    
def insert(alist,insertNo):
    print('ARRAY',alist);
    print('NUMBER TO INSERT',insertNo)
    counter = 0
    temp = convertIntToList(insertNo)

    for element in alist:
        print(element,'< ', insertNo,' = ', element > insertNo )
        if element > insertNo:
            #Insert at the front of the array
            if counter == 0:
                print( 'Insert at the front of the array' )
                return printList( temp + alist )
                
            #Insert in the middle of the array
            else:
                print( 'Insert in the middle of the array' )
                return printList( alist[:counter]+temp+alist[counter:] )
                
        else:
            #Insert at the rear of the array
            print( counter ,' == ', len( alist ) -1, ' = ', counter == len( alist ) -1 )
            if counter == len( alist ) -1:
                print( 'Insert at the rear of the array' )
                return printList(  alist + temp )
                
            
        counter = counter + 1
            
                
   
# Testing insert in the front of the array


'''
listfront = [40, 52, 60]
print( insert(listfront, 39) )
print( '-'*20 )

'''

'''
ARRAY [40, 52, 60]
NUMBER TO INSERT 39
40 <  39  =  True
Insert at the front of the array
[39, 40, 52, 60]
--------------------
'''
# Testing insert in the rear of the array
'''
listRear = [40, 52, 60]
print( insert(listRear, 70) )
print( '-'*20 )
'''

'''
ARRAY [40, 52, 60]
NUMBER TO INSERT 70
40 <  70  =  False
0  ==  2  =  False
52 <  70  =  False
1  ==  2  =  False
60 <  70  =  False
2  ==  2  =  True
Insert at the rear of the array
[40, 52, 60, 70]
--------------------
'''


#Testing insert in the middle of the array
'''
listRear = [40, 52, 60]
print( insert(listRear, 45) )
print( '-'*20 )
'''

'''
ARRAY [40, 52, 60]
NUMBER TO INSERT 45
40 <  45  =  False
0  ==  2  =  False
52 <  45  =  True
Insert in the middle of the array
[40, 45, 52, 60]
--------------------
'''

def sortInsert( alist ):

    tempList = alist.copy()
    counter = 1

    while counter < len( alist ) :
        
        stepList = []
        if counter -1 == 0:
            stepList = convertIntToList(tempList[0])
        else:
            stepList = tempList[:counter]
            
        tempList = insert( stepList, tempList[counter]) + tempList[counter+1:]    
        counter = counter + 1
        
    return  tempList
        
        
    


startList = [ 52, 2, 30, 70, 1]
print( startList )
print( '-'*20 )
print( '-'*20 )
finalList =  sortInsert( startList )
print( '-'*20 )
print( '-'*20 )
print( finalList  )

'''
OUTPUT:

[52, 2, 30, 70, 1]
--------------------
--------------------
ARRAY [52]
NUMBER TO INSERT 2
52 <  2  =  True
Insert at the front of the array
New Array is: [2, 52]
--------------------
ARRAY [2, 52]
NUMBER TO INSERT 30
2 <  30  =  False
0  ==  1  =  False
52 <  30  =  True
Insert in the middle of the array
New Array is: [2, 30, 52]
--------------------
ARRAY [2, 30, 52]
NUMBER TO INSERT 70
2 <  70  =  False
0  ==  2  =  False
30 <  70  =  False
1  ==  2  =  False
52 <  70  =  False
2  ==  2  =  True
Insert at the rear of the array
New Array is: [2, 30, 52, 70]
--------------------
ARRAY [2, 30, 52, 70]
NUMBER TO INSERT 1
2 <  1  =  True
Insert at the front of the array
New Array is: [1, 2, 30, 52, 70]
--------------------
--------------------
--------------------
[1, 2, 30, 52, 70]
'''
