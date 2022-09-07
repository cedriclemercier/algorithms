import timeit
import numpy as np

quicksort = '''


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):

    
    x = A[r]
    i = p - 1
    
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[r] = A[r], A[i+1]
    
    return i + 1

quicksort(arr, 0, len(arr)-1)

'''


heap = '''

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
    
    start = (len(A) // 2) - 1
    for i in range(start, -1, -1):
        max_heapify(A, i)
        
build_max_heap(arr)

'''


mergesort ='''

def merge_sort(arr):
    if len(arr) > 1:
        # calculate mid with floor division if length of arr is 5, then 5//2 = 2
        mid = len(arr) // 2
        
        # select left and right side
        left = arr[:mid]
        right = arr[mid:]
        
        # sort halfs
        merge_sort(left)
        merge_sort(right)
        
    
        a=b=c=0
        
        while a < len(left) and b < len(right):
            if left[a] < right[a]:
                arr[c] = left[a]
                a+=1
            else:
                arr[c] = right[a]
                b+=1
            c+=1
                
        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1
            


merge_sort(arr)

'''


# print(arr)



n_list = [10, 100, 1000, 10000, 100000]

for n in n_list:
    print(f"\n============ Complexity n = {n} ===============")
    setup = f'import numpy as np\narr = np.random.randint(0, {n}, {n})'
    
    quicksort_times = timeit.timeit(setup=setup, stmt = quicksort,number = 1)
    print('QUICK SORT : {}'.format(quicksort_times)) 
    
    heap_times = timeit.timeit(setup=setup, stmt = heap,number = 1)
    print('HEAP SORT : {}'.format(heap_times)) 
    
    merge_sort_times = timeit.timeit(setup=setup, stmt = mergesort,number = 1)
    print('Merge SORT : {}'.format(merge_sort_times)) 