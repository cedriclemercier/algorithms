
arr = [21,65,44,1,7,7,68,10]

print("Array:", arr)
print("------ Insertion sort -------")
def insertionSort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                keep = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = keep
            j-=1
        i += 1
    print("Result:", arr)
    
insertionSort(arr)


print("------ Merge sort -------")
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
print("Result", arr)