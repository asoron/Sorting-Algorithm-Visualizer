import time

shortingAlgorithms = ["BubbleSort", "SelectionSort","InsertionSort","QuickSort","HeapSort","CountingSort",]

def BubbleSort(data,updateColor,updateVisual):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            updateColor(j,True)
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                updateVisual(j, j+1)
            time.sleep(0.1)
            updateColor(j,False)
            
            
def SelectionSort(data,updateColor,updateVisual):
    n = len(data)
    for i in range(n):
        for j in range(i+1,n):
            updateColor(j,True)
            if(data[j] < data[i]):
                data[j], data[i] = data[i], data[j]
                updateVisual(i, j)
            time.sleep(0.1)
            updateColor(j,False)
            
      
        
def InsertionSort(data,updateColor,updateVisual):
    n = len(data)
    for i in range(1,n):
        for j in range(i,0,-1):
            updateColor(j,True)
            if(data[j] < data[j-1]):
                data[j], data[j-1] = data[j-1], data[j]
                updateVisual(j, j-1)
            time.sleep(0.1)
            updateColor(j,False)
            
def QuickSort(data,updateColor,updateVisual):
    def partition(low, high):
        i = low - 1
        pivot = data[high]
        for j in range(low, high):
            updateColor(j,True)
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                updateVisual(i, j)
            time.sleep(0.1)
            updateColor(j,False)
        data[i+1], data[high] = data[high], data[i+1]
        updateVisual(i+1, high)
        return i+1
    
    def quickSort(low, high):
        if low < high:
            pi = partition(low, high)
            quickSort(low, pi-1)
            quickSort(pi+1, high)
    
    quickSort(0, len(data)-1)
    
def HeapSort(data,updateColor,updateVisual):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and data[i] < data[l]:
            largest = l
        if r < n and data[largest] < data[r]:
            largest = r
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            updateVisual(i, largest)
            heapify(n, largest)
        
    
    n = len(data)
    for i in range(n, -1, -1):
        heapify(n, i)
    for i in range(n-1, 0, -1):
        updateColor(i, True)
        data[i], data[0] = data[0], data[i]
        updateVisual(i, 0)
        heapify(i, 0)
        time.sleep(0.1)
        updateColor(i, False)


def CountingSort(data, updateColor, updateVisual):
    n = len(data)
    output = [0] * n
    count = [0] * (max(data) + 1)
    original_indices = list(range(n))
    for i in range(n):
        count[data[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        correct_position = count[data[i]] - 1
        output[correct_position] = data[i]
        original_indices[correct_position] = original_indices[i]
        count[data[i]] -= 1
        i -= 1
    for i in range(n):
        data_index = original_indices[i]
        data[i] = output[i]
        updateVisual(i, data_index)
        original_indices[i] = i


CountingSort([1,4,1,2,7,5,2],lambda x,y: None,lambda x,y: None)