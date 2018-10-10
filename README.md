


# Algorithms and Data Structures

# Introduction  

### Stack and Queue  

The three nodes are HEAD, TAIL, and POINTER nodes. The HEAD and TAIL nodes are the first and list nodes in the linked list, which does not have any nodes above or below these nodes respectly. The POINTER node is used when travelering the linked list. When traveling the linked list we start at the HEAD node and move down the linked list to the TAIL node moving the POINTER node down the linked list.  Links are what connects the linked list together. The links are property variables of the node, which stores the memory address of the next node. The other property variables of the node can be any variable or variables the language surports. The TOP and BOTTOM POINTER LINK are the links above and below the current POINTER node respectly.

![Linked List Define](https://github.com/cusey/ImageForWiki/blob/master/Algorithms_and_Data_Structures/Linked%20List%20Definition.png)

# Data Strutures ( Stack and Queue )
### Desription

I am just using the INSERT method and POP method of the Array class to write the queue and stack to make it easier to memorizes. 


# Deque
### Description  
(usually pronounced like "deck") is an irregular acronym of double-ended queue. Double-ended queues are sequence containers with dynamic sizes that can be expanded or contracted on both ends (either its front or its back).

### Programming Notes
I used python build-in list as the Data Structure. The rear of the array is the first element while the front of the array is the last
element. I used the Pop Method to remove elements from front and rear of the array. Passing in a zero in the parameter while remove element from the rear of the array and passing in nothing will remove from the front of the array. To added element to the front of array by using the Append Method. The Insert Method is used to added the the rear of the array.  

### References
* [5.1 More on Lists](https://docs.python.org/3.1/tutorial/datastructures.html)

# Hashing (Folding Method)  

### Description  
The folding method for constructing hash functions begins by dividing the item into equal-size pieces 
(the last piece may not be of equal size). These pieces are then added together to give the resulting 
hash value. For example, if our item was the phone number 436-555-4601, we would take the digits and 
divide them into groups of 2 (43,65,55,46,01). After the addition, 43+65+55+46+01, we get 210. 
If we assume our hash table has 11 slots, then we need to perform the extra step of dividing by 
11 and keeping the remainder. In this case 210 % 11 is 1, so the phone number 436-555-4601 hashes 
to slot 1. Some folding methods go one step further and reverse every other piece before the addition.
For the above example, we get 43+56+55+64+01=219 which gives 219 % 11=10.

# Hashing (Mid-Square Method)

### Description 

Another numerical technique for constructing a hash function is called the mid-square method. We first square the item, and 
then extract some portion of the resulting digits. For example, if the item were 44, we would first compute 44^2 =  1,936. 
By extracting the middle two digits, 93, and performing the remainder step, we get 5 (93 % 11). 

# Hashing (Remained Method)

### Description   

With the Remained Methods first you count the number of elements you what to store. So the length of the 
array will eaual the number of elements you want so each element will have place to be stored. When you
do the divide by array length the remainer will always to equal or less than the number of element in the
array.

# Linked List (Order List)

### Description    

The order of the items is sort in ascending order.

# Linked List (Unordered List)

### Description    

The order of the items is not sort in any particular order. Each item is inserted at the end of the Linked List.


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

# List - Anagram (Count and Compare)


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

# List - Maximum Number (Linear Search) 

# Nesting Dictionary

### Description  

This is example how to build nested Dictionary with Python.

# Neting List

### Description  

This is example how to build nested List with Python.

# Queue

# Recursion  (Factorial)

# Recursion (Calculating the Sum)

# Recursion (Converting Base)

### Decimal to Hexadecimal Convertion Table

![ Decimal to Hexadecimal ](https://github.com/cusey/ImageForWiki/blob/master/Algorithms_and_Data_Structures/Converting_Deci_To_Hexa.png)

### Description  

To populate to Result column you uses the Remainder Column and the Decimal to Hexadecimal Convertion Table. In this example in the Remainder Column is 15 (base 10) decimal so by using the table we the demical equality is F (base 16) Hexadecimal. 

### Recursion (Make Currency Change)

### Description 

# Recursion Stack (Converting Base)

# Search - List (Binary)

# Search - List (Sequential Search)

# Sort (Bubble)   

The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.      
![Bubble Sort](https://github.com/cusey/ImageForWiki/blob/master/Algorithms_and_Data_Structures/bubble_pic.PNG)  

# Sort (Insertion)  

It always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger

![Insertion Sort](https://github.com/cusey/ImageForWiki/blob/master/Algorithms_and_Data_Structures/insertion_pic.PNG)

# Sort (Selection)  

The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place.

![Selection Sort](https://github.com/cusey/ImageForWiki/blob/master/Algorithms_and_Data_Structures/insertion_pic.PNG)  

# Stack (Decimal to Binary Conversion)  

### Programming Notes  

I used a Stack Data Structure.   

### References  
* [Decimal to Binary Conversion](https://www.electronics-tutorials.ws/binary/bin_2.html)   

# Stack (Simple Balanced Parentheses)

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
