#python 3.5.2

'''
Python Built-in Functions: (https://docs.python.org/3/library/functions.html)
ord(c) - Given a string representing one Unicode character, return an integer representing the Unicode code 
point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364.
This is the inverse of chr().

Python list initialization - http://zetcode.com/lang/python/lists/
Sometimes we need to initialize a list in advance to  have a particular number of elements. 
[0]*26 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0 for i in range(26)]  =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

The method cmp() compares elements of two lists. (https://www.tutorialspoint.com/python/list_cmp.htm ) - Python 3 does not have cmp
"(If you really need the cmp() functionality, you could use the expression (a > b) - (a < b) as the equivalent for cmp(a, b).)"

'''


def countOccurance(word):
    countLetters = [0]*26
    for x in word:
        index = ord(x) - ord('a')
        countLetters[ index ] = countLetters[ index ] + 1
    return countLetters

#print ( countOccurance('earth') )
#print ( countOccurance('heart') )


def areAnagram(firstWord, secondWord):
    a = countOccurance(firstWord)
    b = countOccurance(secondWord)
    return (a > b) - (a < b) == 0


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
