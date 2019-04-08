#python 3.5.2

unsorted_list = [2,8,5,3,9,4,1]

print('BEFORE: ' + str(unsorted_list) )

def swap(result,index_left,index_right):
     value_left = result[index_left]
     result[index_left] = result[index_right] 
     result[index_right] = value_left
        
     return result
        
# print('AFTER swap: ' + str( swap(unsorted_list, 2 ,5) ) )
print('_'*20)
     

def selectionSort(sorting_list):
    
    length = len(sorting_list)
    
    
    for start_unsorted in range( length ):
        
        minimum_value = sorting_list[start_unsorted]
        index_minimum_value = start_unsorted
        do_swap = False

        for minimum in range( start_unsorted +1, length ):
            # print(start_unsorted,minimum)
            
            if minimum_value > sorting_list[minimum]:
                minimum_value = sorting_list[minimum]
                index_minimum_value = minimum
                do_swap = True
                
                
        if do_swap:
            swap(sorting_list,start_unsorted,index_minimum_value)
            
        # print('_'*20)
        
    return sorting_list


print('AFTER selectionSort: ' + str( selectionSort(unsorted_list)) )

```
OUTPUT:
BEFORE: [2, 8, 5, 3, 9, 4, 1]
____________________
AFTER selectionSort: [1, 2, 3, 4, 5, 8, 9]
```  
