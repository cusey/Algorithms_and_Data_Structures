# Algorithms and Data Structures

# Deque
### Description  
(usually pronounced like "deck") is an irregular acronym of double-ended queue. Double-ended queues are sequence containers with dynamic sizes that can be expanded or contracted on both ends (either its front or its back).

### Programming Notes
I used python build-in list as the Data Structure. The rear of the array is the first element while the front of the array is the last
element. I used the Pop Method to remove elements from front and rear of the array. Passing in a zero in the parameter while remove element from the rear of the array and passing in nothing will remove from the front of the array. To added element to the front of array by using the Append Method. The Insert Method is used to added the the rear of the array.  

### References
* [5.1 More on Lists](https://docs.python.org/3.1/tutorial/datastructures.html)

# Linked List

### Description   
A linked list is a linear data structure where each element is a separate object. Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list.

# List - Anagram (Checking Off)

### Description  

Checking Off - This method uses the first list to compares to the second list. When this program finds a match it sets the value it the second list to None.


### Programming Notes

I used the Python Built-in **Any** Function to check if the list contains all Nones. The Any Return True if any element of the iterable is true. If the iterable is empty, return False. 

### References

* [Any Method - Programiz](https://www.programiz.com/python-programming/methods/built-in/any)

# List - Anagram(Count and Compare)


### Description

First I initialize two arrays with all zeroes this will prepresent each letter in the alphabet.  Then I count the occuance of letter in both strings.  After counting the occurance of each letter I check to see if both string have the same number letter in each string.

### Programming Notes

ord(c) - Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364.

Sometimes we need to initialize a list in advance to  have a particular number of elements. 
[0]*26 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0 for i in range(26)] =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Python 3 does not have cmp. If you really need the cmp() functionality, you could use the expression (a > b) - (a < b) as the equivalent for cmp(a,b).)

### References  

* [Python list initialization - Zetcode ](http://zetcode.com/lang/python/lists/)
* [Compare List - Tutorialspoint](https://www.tutorialspoint.com/python/list_cmp.htm)
* [Cmp doesn't exist in Python 3](https://stackoverflow.com/questions/22490366/cmp-isnt-woking-for-me-python)

# List - Anagram (Sort and Compare)

### Description

Sort and Compare - So, if we begin by sorting each string alphabetically, from a to z, we will end up with the same string if the original two strings are anagrams

### Programming Notes

I used the Python Build-in **Sort** Function to alphabetical order the two lists before comparing the two lists together to see if they are the same.

### References

* [Sorting HOW TO](https://docs.python.org/3.3/howto/sorting.html)

# Nesting Dictionary

### Description  

This is example how to build nested Dictionary with Python.

# Neting List

### Description  

This is example how to build nested List with Python.

# Stack - Decimal to Binary Conversion

### Programming Notes

I used a Stack Data Structure.

### References  
* [Decimal to Binary Conversion](https://www.electronics-tutorials.ws/binary/bin_2.html)

# Stack - Simple Balanced Parentheses

### Description

Simple Balanced Parentheses -Once you agree that a stack is the appropriate data structure for keeping the parentheses, the statement of
the algorithm is straightforward. Starting with an empty stack, process the parenthesis strings from left to right. If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to appear later. 

If, on the other hand, a symbol is a closing parenthesis, pop the stack. As long as it is possible to pop the stack to match every
closing symbol, the parentheses remain balanced. If at any time there is no opening symbol on the stack to match a closing symbol, the string is not balanced properly. At the end of the string, when all symbols have been processed, the stack should be empty.

### Programming Notes

I used a Stack Data Structure.

# Stack  

### Description  

A stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This end is commonly referred to as the “top.” The end opposite the top is known as the “base.” The base of the stack is significant since items stored in the stack that are closer to the base represent those that have been in the stack the longest. The most recently added item is the one that is in position to be removed first. This ordering principle
is sometimes called LIFO, last-in first-out.
