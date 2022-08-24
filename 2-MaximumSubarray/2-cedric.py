import matplotlib.pyplot as plt
import numpy as np
import time



def max_crossing(A, low, mid, high):
    
    # loop through left
    s = 0
    left_sum = -100000
    for i in range(mid, low-1, -1):
        s = s + A[i]
        
        if s > left_sum:
            left_sum = s
            left_max = i
    
    
    s = 0
    right_sum = -100000
    for j in range(mid+1, high+1, 1):
        s = s + A[j]
        
        if s > right_sum:
            right_sum = s
            right_max = j
    
    return (left_max, right_max, left_sum + right_sum)

def max_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    
    mid = (low + high) // 2
    
    left_low, left_high, left_sum = max_subarray(A, low, mid)
    right_low, right_high, right_sum = max_subarray(A, mid+1, high)
    cross_low, cross_high, cross_sum = max_crossing(A, low, mid, high)
    
    
    if left_sum > right_sum and left_sum > cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum > left_sum and right_sum > cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)




# class
arr = [2, -1, 4, -5, 4, 3]
n = len(arr)
print(max_subarray(arr, 0, n-1))

list_range = np.arange(100, 100000, 50)

times = []
elements = []

for idx, n in enumerate(list_range):
    print("Iter {} of {}".format(idx, len(list_range)))
    arr = np.random.randint(0, n, n)
    start = time.time()
    max_subarray(arr, 0, len(arr) -1)
    end = time.time()
    elements.append(len(arr))
    times.append(end-start)
    
    
plt.plot(elements, times, label="Max Subarray")
plt.legend()
plt.show()