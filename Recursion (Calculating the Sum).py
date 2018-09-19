#python 3.5.2

def listsum(numList):
   if len(numList) == 1:
        print(' {} '.format(numList[0]) )
        print('-'*20)
        return numList[0]
   else:
        print(' {}  + '.format(numList[0]) )
        return numList[0] + listsum(numList[1:])
    


print(listsum([1,3,5,7,9]))

'''
OUTPUT:

 1  + 
 3  + 
 5  + 
 7  + 
 9 
--------------------
25
'''