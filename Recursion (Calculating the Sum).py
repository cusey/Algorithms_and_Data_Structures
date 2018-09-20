#python 3.5.2

def listsum(numList):
   if len(numList) == 1:
        print(' {} '.format(numList[0]) )
        print('-'*20)
        return numList[0]
   else:
        print(' {}  + listsum ( {} )'.format(numList[0], numList[1:]) )
        return numList[0] + listsum(numList[1:])
    


print(listsum([1,3,5,7,9]))

'''
OUTPUT:

 1  + listsum ( [3, 5, 7, 9] )
 3  + listsum ( [5, 7, 9] )
 5  + listsum ( [7, 9] )
 7  + listsum ( [9] )
 9 
--------------------
25
'''
