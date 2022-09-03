
import math
from io import StringIO

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

def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

def build_max_heap(A):
    print("Start array:", A)
    
    start = (len(A) // 2) - 1
    for i in range(start, -1, -1):
        max_heapify(A, i)
        show_tree(A)
        
        
    print("Sorted:", A)

arr = [2,8,5,3,9,1]
build_max_heap(arr)