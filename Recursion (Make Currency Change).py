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
        return ('Coins [ '
                  + 'counter : '+ str( self.counter ) 
                  + ', results : ' + str( self.results )
                  + ', coinValueList : ' + str( self.coinValueList )
                  + ', coin: '+ str( self.coinValueList[ self.counter ] )
                  + ' ] ' )

    
    def makeCoinChange( self, change ):
        
        print ( 'change: ' + str ( change ) )
        
        if change  - self.coin < 0:
             self.counter +=  1

        if change == 0:
             pass
        else:
            if self.coin <= change:
                self.results[ self.coin ] += 1
                
            print( self.__repr__() )

            if self.coin <= change:
                self.makeCoinChange( change - self.coin )
            else:
                self.makeCoinChange( change )

        return self.results


change = Coins( [10,25,5,1])

print('\n')
print ( change.makeCoinChange( 63 ) )
print('-'*20)


'''
OUTPUT:

COIN VALUES:  [25, 10, 5, 1]
63 - [ 25 ]
 = 38
38 - [ 25 ]
 = 13
13 - [ 10 ]
 = 3
3 - [ 1 ]
 = 2
2 - [ 1 ]
 = 1
1 - [ 1 ]
 = 0
{25: 2, 10: 1, 5: 0, 1: 3}
--------------------


change: 63
Coins [ counter : 0, results : {25: 1, 10: 0, 5: 0, 1: 0}, coinValueList : [25, 10, 5, 1], coin: 25 ] 
change: 38
Coins [ counter : 0, results : {25: 2, 10: 0, 5: 0, 1: 0}, coinValueList : [25, 10, 5, 1], coin: 25 ] 
change: 13
Coins [ counter : 1, results : {25: 2, 10: 1, 5: 0, 1: 0}, coinValueList : [25, 10, 5, 1], coin: 10 ] 
change: 3
Coins [ counter : 2, results : {25: 2, 10: 1, 5: 0, 1: 0}, coinValueList : [25, 10, 5, 1], coin: 5 ] 
change: 3
Coins [ counter : 3, results : {25: 2, 10: 1, 5: 0, 1: 1}, coinValueList : [25, 10, 5, 1], coin: 1 ] 
change: 2
Coins [ counter : 3, results : {25: 2, 10: 1, 5: 0, 1: 2}, coinValueList : [25, 10, 5, 1], coin: 1 ] 
change: 1
Coins [ counter : 3, results : {25: 2, 10: 1, 5: 0, 1: 3}, coinValueList : [25, 10, 5, 1], coin: 1 ] 
change: 0
{25: 2, 10: 1, 5: 0, 1: 3}
--------------------
'''



