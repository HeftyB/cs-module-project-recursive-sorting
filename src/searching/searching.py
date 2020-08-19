# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if len(arr) == 0:
        return -1

    if target == arr[start] or target == arr[end]:
        return 1

    current_index = int(start + ((end - start) / 2))
    
    if arr[current_index] == target:
        return 1
    
    elif start is end:
        return -1

    elif target > arr[current_index]:
        return binary_search(arr, target, current_index + 1, end)
    
    elif target < arr[current_index]:
        return binary_search(arr, target, start, current_index - 1)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

