#python 3.5.2

def seqSearch(searchList, itemSearchFor ):
    
    findIndex = []
    counter = 0
    
    while len(searchList) > counter:
        
        if searchList[counter] == itemSearchFor:
            findIndex.append(counter)
        
        counter = counter + 1
        
    return findIndex
        
        
        
        
print ('1', seqSearch( [ 0,1,2,3], 5 ) )

print ('2', seqSearch( [ 0,1,2,3], 0 ) )

print ('3', seqSearch( [ 0,1,2,3], 3 ) )

print ('4', seqSearch( [ 0,1,2,3], 1 ) )

print ('5', seqSearch( [ 0,1,2,3,3], 3 ) )

print ('6', seqSearch( [ 0,0,2,3,3], 0 ) )

print ('7', seqSearch( [ 0,1,2,2,4], 2 ) )

'''
OUTPUT:

1 []
2 [0]
3 [3]
4 [1]
5 [3, 4]
6 [0, 1]
7 [2, 3]
'''