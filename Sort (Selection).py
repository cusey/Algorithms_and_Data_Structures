#python 3.5.2

def swap(alist,indexTo,indexFrom):
    temp = alist[indexFrom] 
    alist[indexFrom] = alist[indexTo]
    alist[indexTo] = temp
    return alist

def findLargest(alist):
    print(alist)
    counter = 0
    maxIndex = 0
    while tail > counter:
       if alist[counter] > alist[maxIndex]:
          maxIndex = counter
       counter = counter + 1
     
     print('Largest :',alist[maxIndex])
     return maxIndex
    
#python 3.5.2

def swap(alist,indexTo,indexFrom):
    temp = alist[indexFrom] 
    alist[indexFrom] = alist[indexTo]
    alist[indexTo] = temp
    return alist

def findLargest(alist):
    print('FIND LARGEST FROM THIS LIST',alist)
    counter = 0
    maxIndex = 0
    while len(alist) > counter:
       if alist[counter] > alist[maxIndex]:
          maxIndex = counter
       counter = counter + 1
     
    print('Largest :',alist[maxIndex])
    return maxIndex
    

def selectionSoft(alist):
   
    tail = len(alist)
    
    while tail != 0:

        tempList = swap ( alist, findLargest(alist[:tail]) , tail -1)
        
        alist = tempList.copy()
        print ('SWAP LIST',alist)
        print('-'*20)
        
        tail = tail - 1
    
    return alist
        

startList = [23,43,24,94,21,12]
print('STARTING LIST', startList )
print('-'*20)  
print('-'*20)  

finalList = selectionSoft(startList)

print('-'*20)   
print('Final List', finalList  )

'''
OUTPUT:

STARTING LIST [23, 43, 24, 94, 21, 12]
--------------------
--------------------
FIND LARGEST FROM THIS LIST [23, 43, 24, 94, 21, 12]
Largest : 94
SWAP LIST [23, 43, 24, 12, 21, 94]
--------------------
FIND LARGEST FROM THIS LIST [23, 43, 24, 12, 21]
Largest : 43
SWAP LIST [23, 21, 24, 12, 43, 94]
--------------------
FIND LARGEST FROM THIS LIST [23, 21, 24, 12]
Largest : 24
SWAP LIST [23, 21, 12, 24, 43, 94]
--------------------
FIND LARGEST FROM THIS LIST [23, 21, 12]
Largest : 23
SWAP LIST [12, 21, 23, 24, 43, 94]
--------------------
FIND LARGEST FROM THIS LIST [12, 21]
Largest : 21
SWAP LIST [12, 21, 23, 24, 43, 94]
--------------------
FIND LARGEST FROM THIS LIST [12]
Largest : 12
SWAP LIST [12, 21, 23, 24, 43, 94]
--------------------
--------------------
Final List [12, 21, 23, 24, 43, 94]
'''
