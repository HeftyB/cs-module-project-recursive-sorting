# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    for i in range(0, elements - 1):
        if arrA[0] < arrB[0]:
            print("a")
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            print("b")
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
# def merge_sort(arr):
#     # Your code here

#     if len(arr) > 1:
#         arrA = merge_sort(arr[:len(arr) / ])
#         arrB = merge

#     return arr

def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        # recurse on left half
        left = merge_sort(arr[:mid])
        # recurse on right half
        right = merge_sort(arr[mid:])
        # put things back together: merge
        arr = merge(left, right)
    return arr



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

