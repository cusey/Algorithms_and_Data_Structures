#python 3.5.2

def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]   
    
    print('pivot: ' + str( pivot) ) 
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 

            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]  

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high:
        
        print('quickSort - partition - arr:' + str(arr) +' low:'+ str(low) + ' high: '+ str(high) )
        pi = partition(arr,low,high)
        
        print('quickSort - partition - pivot index: ' str(pi) )
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
        
        
unsorted_array = [2,6,5,3,8,7,1,0]

n = len(unsorted_array) 
quickSort(unsorted_array,0,n-1) 

print ("Sorted array:" + str(unsorted_array) ) 
