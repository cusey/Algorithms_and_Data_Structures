#python 3.5.2

'''
Checking Off - This method uses the first list compares to the second list. When the method finds a match it setting the
value it the second list to None.

Python Built-in Functions: (https://docs.python.org/3/library/functions.html#any)
any(iterable)- Return True if any element of the iterable is true. If the iterable is empty, return False. 
https://www.programiz.com/python-programming/methods/built-in/any

'''

def areAnagram(firstWord, secondWord, debug):
        firstList = list(firstWord)
        secondList = list(secondWord)
        
        if debug:    
            print('firstList=', firstList )
            print('secondList=', secondList )
            print( '*'*20)
        
        while len(firstList) != 0:
            temp = firstList.pop(0)
            found = False
            count = 0
            
            while not found:
            
                if(debug):
                    print( 'temp=', temp) 
                    print( 'secondList[',count,']=',secondList[count])
                    print ('MATCH:', secondList[count] == temp )

                if count <= len(secondList) -1:
                    if secondList[count] == temp:
                        found = True
                        secondList[count] = None
                    
                        if(debug):
                            print( secondList )
                else:
                    if debug:
                        print( '_'*20)
                    return False
                    
                
                count += 1
                if debug:
                    print( '_'*20)
                    
        return not any(secondList)
                    
    
# Checking same word (Result should be True)
print ( 'Is "earth" and "earth" an anagram ?' , areAnagram('earth','earth', False) ) 

# Checking two anagrams (Result should be True)
print ( 'Is "heart" and "earth" an anagram ?' , areAnagram('heart','earth', False) ) 

# Checking two words that are not anagrams (Result should be False)
print ( 'Is "eartj" and "earth" an anagram ?' , areAnagram('eartj','earth', False) ) 

# Checking not the same number of characters (Result should be False)
print ( 'Is "eart" and "earth" an anagram ?' , areAnagram('eart','earth', False) ) 

# Checking not the same number of characters (Result should be False)
print ( 'Is "earth" and "earthh" an anagram ?' , areAnagram('earth','earthh', False) ) 

'''
OUTPUT:
Is "earth" and "earth" an anagram ? True
Is "heart" and "earth" an anagram ? True
Is "eartj" and "earth" an anagram ? False
Is "eart" and "earth" an anagram ? False
Is "earth" and "earthh" an anagram ? False
'''





        
