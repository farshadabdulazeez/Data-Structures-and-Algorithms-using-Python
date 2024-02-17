'''
Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

Time Complexity: 

Best Case: O(1)
Average Case: O(log N)
Worst Case: O(log N)
Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(logN).

Advantages of Binary Search:

Binary search is faster than linear search, especially for large arrays.
More efficient than other searching algorithms with a similar time complexity, such as interpolation search or exponential search.
Binary search is well-suited for searching large datasets that are stored in external memory, such as on a hard drive or in the cloud.

Drawbacks of Binary Search:

The array should be sorted.
Binary search requires that the data structure being searched be stored in contiguous memory locations. 
Binary search requires that the elements of the array be comparable, meaning that they must be able to be ordered.

Applications of Binary Search:

Binary search can be used as a building block for more complex algorithms used in machine learning, such as algorithms for training neural networks or finding the optimal hyperparameters for a model.
It can be used for searching in computer graphics such as algorithms for ray tracing or texture mapping.
It can be used for searching a database.

How to Implement Binary Search?

The Binary Search Algorithm can be implemented in the following two ways

Iterative Binary Search Algorithm
Recursive Binary Search Algorithm
'''

# Iterative Binary Search Algorithm

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Return -1 if the target is not found in the array

# Example usage:
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7
result = binary_search(my_array, target_element)
print(result)


# Recursive Binary Search Algorithm

# def binary_search_recursive(arr, target, low, high):
#     if low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid  # Return the index if the target is found
#         elif arr[mid] < target:
#             return binary_search_recursive(arr, target, mid + 1, high)  # Search the right half
#         else:
#             return binary_search_recursive(arr, target, low, mid - 1)  # Search the left half
#     else:
#         return -1  # Return -1 if the target is not found in the array

# # Example usage:
# my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target_element = 7
# result = binary_search_recursive(my_array, target_element, 0, len(my_array) - 1)
# print(result)

