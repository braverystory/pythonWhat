
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    # Select quicksort pivot
    #pivot = arr[len(arr) // 2]		
    #pivot = arr[len(arr) - 1] 		
    pivot = arr[0] 					

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

data = [9,-3,5,2,6,8,-6,1,3]
print("Unsorted data: "	+ " ".join(repr(e) for e in data))
print("Sorted data: "	+ " ".join(repr(e) for e in quicksort(data)))

