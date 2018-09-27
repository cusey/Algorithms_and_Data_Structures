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

class Coins:

    def __init__(self, coinValueList):
        self.counter = 0
        
        coinValueList.sort(reverse=True)
        self.coinValueList = coinValueList.copy()
        
        self.results = {}
        for coin in coinValueList:
            self.results[coin] = 0
    
    @property
    def coin( self ):
        return self.coinValueList[ self.counter ]
        
    def __repr__(self):
        return 'Coins [ counter : ' + str( self.counter ) + ', results : ' + str( self.results ) + ', coinValueList : ' + str( self.coinValueList ) + ', coin:'+ str( self.coinValueList[ self.counter ] ) + ' ] '
        
    def makeCoinChange( self, change ):
        
        print ( 'change: ' + str ( change ) )
        
        if change  - self.coin < 0:
             self.counter +=  1

        if change != 0:
            if self.coin <  change:
                self.results[ self.coin ] += 1
                
            print( self.__repr__() )

            if self.coin <  change:
                self.makeCoinChange( change - self.coin )
            else:
                self.counter +=  1
                self.makeCoinChange( change )
         else:
                    print('Yes')
                
                
        return self.results

change = Coins( [10,25,5,1])


print ( change.makeCoinChange( 63 ) )

print('-'*20)
