#python 3.5.2

def listsum (numList):
    
    result = 0
    
    while len(numList) != 0:
        print(' {} + {} '.format(result, numList[0]) )
        result = result + numList[0]
        numList =  numList[1:]
        
    return result
    

def reclistsum(numList):
   if len(numList) == 1:
        print(' {} '.format(numList[0]) )
        return numList[0]
   else:
        print(' {}  + reclistsum ( {} )'.format(numList[0], numList[1:]) )
        return numList[0] + reclistsum(numList[1:])
    
print(listsum([1,3,5,7,9]))
print('-'*20)

print(reclistsum([1,3,5,7,9]))
print('-'*20)


'''
OUTPUT:

 0 + 1 
 1 + 3 
 4 + 5 
 9 + 7 
 16 + 9 
25
--------------------
 1  + reclistsum ( [3, 5, 7, 9] )
 3  + reclistsum ( [5, 7, 9] )
 5  + reclistsum ( [7, 9] )
 7  + reclistsum ( [9] )
 9 
25
--------------------
'''
