#python 3.6

def find_insert(sorted, insert_value):
    unfinished = True
    count = 0

    while unfinished and count < len(sorted):

        if insert_value == sorted[count]:
                                            # Having same value as the List element
            sorted.insert(count, insert_value)
            unfinished = False
        elif insert_value < sorted[count]:
                                            # Have one element AND array element is smaller then the insert number
                                            # Have more than one element AND inserting before first element
            sorted.insert(0, insert_value)
            unfinished = False
        elif len(sorted) == 1 and insert_value > sorted[count]:
                                                                    # Have one element AND array element is larger then the insert number
            sorted.insert(1, insert_value)
            unfinished = False
        elif count == (len(sorted) -1) and sorted[count] < insert_value:
                                                                         # Inserting and the end of the array
            sorted.insert(count + 1, insert_value)
            unfinished = False
        elif sorted[count] < insert_value and sorted[count + 1] > insert_value:
                                                                                    # Inserting in the middle of the array
            sorted.insert(count + 1, insert_value)
            unfinished = False


        count = count + 1

    return sorted

# Having same value as the List element

print('1 find_insert: ', find_insert([2], 2))
print('2 find_insert: ', find_insert([2, 8 ,9], 8))
print('3 find_insert: ', find_insert([2, 8 ,9], 9))

# Have one element AND inserting before first element
print('4 find_insert: ', find_insert([8], 2))

# Have more than one element AND inserting before first element
print('5 find_insert: ', find_insert([2,8,9], 2))

# Have one element AND array element is larger then the insert number
print('6 find_insert: ', find_insert([2], 8))

# Inserting in the middle of the array
print('7 find_insert: ', find_insert([2, 8], 5))
print('8 find_insert: ', find_insert([2, 5, 8], 3))

# Inserting and the end of the array
print('9 find_insert: ', find_insert([2, 3, 5, 8], 9))
print('-' * 50)

'''
OUTPUT:
1 find_insert:  [2, 2]
2 find_insert:  [2, 8, 8, 9]
3 find_insert:  [2, 8, 9, 9]
4 find_insert:  [2, 8]
5 find_insert:  [2, 2, 8, 9]
6 find_insert:  [2, 8]
7 find_insert:  [2, 5, 8]
8 find_insert:  [2, 3, 5, 8]
9 find_insert:  [2, 3, 5, 8, 9]
--------------------------------------------------
'''

unsorted = [2, 8, 5, 3, 9, 4]


def insertionSort(unsorted):
    sorted = []

    for element in unsorted:
        if len(sorted) == 0:
            sorted.insert(0, element)
        else:
            sorted = find_insert(sorted, element)
    return sorted


print('insertionSort: ', insertionSort(unsorted))
print('-' * 50)

'''
OUTPUT:
insertionSort:  [2, 3, 4, 5, 8, 9]
--------------------------------------------------
'''
