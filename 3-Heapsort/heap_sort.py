arr = [2,8,5,3,9,1]



def heapsort(A):
    pass


def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len(A) and A[left] > A[i]:
        largest = left
    else:
        largest = i
        
    if right < len(A) and A[right] > A[largest]:
        largest = right
        
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        
        max_heapify(A, largest)


def build_max_heap(A):
    print("Start array:", A)
    
    start = (len(A) // 2) - 1
    for i in range(start, -1, -1):
        max_heapify(A, i)
        
        
    print("Sorted:", A)


build_max_heap(arr)