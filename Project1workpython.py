
#project by Donald ford, Alyssa scott, Ravon Aaron


def heapify(arr, n, i): 
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] 
  
        heapify(arr, n, largest) 
  
def heapSort(arr): 
    n = len(arr) 
  
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 
        
arr = [ 25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print("The original array is: ", arr)
heapSort(arr)
a = len(arr)
print ("Array after sorting is: ", arr)
