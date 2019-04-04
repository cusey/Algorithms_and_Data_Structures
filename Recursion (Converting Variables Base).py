#python 3.5.2

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
        
    
dec_to_hex = Convert_Symbol(48879, 16, '0123456789ABCDEF' )       
        
print( convert_recursion(dec_to_hex) )

print('-'*20)

'''
BEEF
--------------------
'''

dec_to_oct = Convert_Symbol(4242, 8, '01234567' )       
        
print( convert_recursion(dec_to_oct) )

print('-'*20)

'''
10222
--------------------
'''

dec_to_base_six = Convert_Symbol(412, 6, '012345' )       
        
print( convert_recursion(dec_to_base_six) )

print('-'*20)

'''
1524
--------------------
'''
