#python 3.5.2
'''
Sort and Compare -  So, if we begin by sorting each string alphabetically, 
from a to z, we will end up with the same string if the original two 
strings are anagrams
'''

def areAnagram(firstWord, secondWord):
    firstList = list(firstWord)
    secondList = list(secondWord)
    result = True
      
    if len(firstList) == len(secondList) and result:
      #Sort both list alphabetically
      firstList.sort()
      secondList.sort()
      i = 0
      length =  len(firstList) 
      while i < length :
         if firstList[i] != secondList[i]:
              result = False
         i = i + 1
    else:
      result = False
    
    return result

# Checking same word (Result should be True)
print ( 'Is "earth" and "earth" an anagram ?' , areAnagram('earth','earth') ) 

# Checking two anagrams (Result should be True)
print ( 'Is "heart" and "earth" an anagram ?' , areAnagram('heart','earth') ) 

# Checking two words that are not anagrams (Result should be False)
print ( 'Is "eartj" and "earth" an anagram ?' , areAnagram('eartj','earth') ) 

# Checking not the same number of characters (Result should be False)
print ( 'Is "eart" and "earth" an anagram ?' , areAnagram('eart','earth') )  

# Checking more than one of the same characters (Result should be False)
print ( 'Is "eearth" and "earth" an anagram ?' , areAnagram('eearth','earth') )  

'''
OUTPUT:

Is "earth" and "earth" an anagram ? True
Is "heart" and "earth" an anagram ? True
Is "eartj" and "earth" an anagram ? False
Is "eart" and "earth" an anagram ? False
Is "eearth" and "earth" an anagram ? False
'''
