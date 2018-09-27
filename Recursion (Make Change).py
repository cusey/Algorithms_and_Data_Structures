#python 3.5.2
 
def makeChange( coinValueList, change, debug ):
    
    count = 0
    coinValueList.sort(reverse=True)
    
    result = {}
    for coin in coinValueList:
        result[coin] = 0
    
    
    if debug:
        print( 'COIN VALUES: ', coinValueList )
    
    while len( coinValueList ) > count:
        
        if change  - coinValueList[count] >= 0:
            if debug:
                print(str( change) + ' - ' + '[ ' + str(coinValueList[count]) + ' ]' )
                
            result[coinValueList[count]]  = result[coinValueList[count]]  + 1
                
            change = change - coinValueList[count]
            print(' = ' + str( change ) )
        else:
            count = count +1
            
    return result
            

print ( makeChange( [10,25,5,1] , 63, True ) )
print('-'*20)