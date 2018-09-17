#python 3.5.2

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
