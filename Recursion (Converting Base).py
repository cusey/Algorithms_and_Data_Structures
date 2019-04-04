#python 3.5.2

'''
CODING NOTES:

    DIVISION 10/3 =  3.3333333333333335

    FlOOR DIVISION so 10//3 = 3 ( Rounds down)

'''


# EXAMPLE How to convert base 10 to base 16

class Convert_Symbol:
    
    def __init__(self, number, base, symbol_list, logger_on=False):
        self.number = number
        self.base = base
        self.symbol_list = symbol_list
        self.logger_on = logger_on
        self.result = ''

    def newSymbol(self):
        return self.symbol_list [ self.number % self.base ]
    
    def floorDivision(self):
        return self.number // self.base
    
    def logger(self):
        if ( self.logger_on) : 
            print( ' base = ' + str(self.base) )
            print( ' number = ' + str(self.number) )
            print( ' (number='+ str( self.number) +') % (base='+ str(self.base)+') = ' + str(self.number % self.base) ) 
            print( ' symbol_list [ (number='+ str( self.number) +') % (base='+ str(self.base)+') ] = ' + str(self.symbol_list[self.number % self.base]) ) 
  
        

# dh = Convert_Symbol(12, 16, '0123456789ABCDEF')

# dh.logger()
# print('-'*20) 

# print( dh.newSymbol() )
# print('-'*20) 

'''
--------------------
C
--------------------
'''

# *************************** MAIN WHILE ***************************
def convert_while(obj):
    
    result = ''

    while obj.number != 0:
        result = obj.newSymbol() + result
        obj.number = obj.floorDivision()
        
        obj.logger()

    return result
	
	
dh = Convert_Symbol(48879, 16, '0123456789ABCDEF', True)

# print( convert_while(dh) ) 
# print('-'*20) 

'''
 base = 16
 number = 3054
 (number=3054) % (base=16) = 14
 symbol_list [ (number=3054) % (base=16) ] = E
 base = 16
 number = 190
 (number=190) % (base=16) = 14
 symbol_list [ (number=190) % (base=16) ] = E
 base = 16
 number = 11
 (number=11) % (base=16) = 11
 symbol_list [ (number=11) % (base=16) ] = B
 base = 16
 number = 0
 (number=0) % (base=16) = 0
 symbol_list [ (number=0) % (base=16) ] = 0
BEEF
--------------------
'''

# *************************** MAIN RECURSION ***************************

def convert_recursion(obj):
    
   result = ''
    
   if( obj.number != 0) :
       obj.logger()
        
       obj.result  = obj.newSymbol() + obj.result
       obj.number = obj.floorDivision()

       return convert_recursion(obj)
   else:
       return obj.result 
        
    
dh = Convert_Symbol(48879, 16, '0123456789ABCDEF', True)       
        
print( convert_recursion(dh) )

print('-'*20)

'''
 base = 16
 number = 48879
 (number=48879) % (base=16) = 15
 symbol_list [ (number=48879) % (base=16) ] = F
 base = 16
 number = 3054
 (number=3054) % (base=16) = 14
 symbol_list [ (number=3054) % (base=16) ] = E
 base = 16
 number = 190
 (number=190) % (base=16) = 14
 symbol_list [ (number=190) % (base=16) ] = E
 base = 16
 number = 11
 (number=11) % (base=16) = 11
 symbol_list [ (number=11) % (base=16) ] = B
BEEF
--------------------
'''




