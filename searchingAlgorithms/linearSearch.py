'''
Linear search, also known as sequential search, is a straightforward searching algorithm that checks each element in a collection one by one until a match is found or the entire collection has been searched. It works on both sorted and unsorted lists.

Linear Search Algorithm:

**Start from the beginning of the array.
Compare each element with the target element.
If a match is found, return the index.
If the end of the array is reached without finding the target, return -1.

Time Complexity:

Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
Average Case: O(N)
Auxiliary Space: O(1) as except for the variable to iterate through the list, no other variable is used. 

Advantages of Linear Search:

Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays of any data type.
Does not require any additional memory.
It is a well-suited algorithm for small datasets.

Drawbacks of Linear Search:

Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
Not suitable for large arrays.

When to use Linear Search?

When we are dealing with a small dataset.
When you are searching for a dataset stored in contiguous memory.

'''

# Searching for an Element
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found in the list

# Example usage:
my_list = [4, 2, 8, 1, 7, 3, 6]
target_element = 7
result = linear_search(my_list, target_element)



# def LinearSearch(list,key):
#     for i in range(len(list)):
#         if key == list[i]:
#             print("key is found at index : ",i)
#             break
#     else:
#         print("not found")


# list = [1,5,12,6,13,1]
# print(list)
# key = int(input("Enter a key : "))
# LinearSearch(list,key)


# Counting Occurrences of an Element

# def count_occurrences(arr, target):
#     count = 0
#     for element in arr:
#         if element == target:
#             count += 1
#     return count

# # Example usage:
# my_list = [4, 2, 8, 1, 7, 6, 3, 6]
# target_element = 6
# occurrences = count_occurrences(my_list, target_element)
# print(f"Element {target_element} occurs {occurrences} times in the list.")


# Finding All Indices of an Element

# def find_all_indices(arr, target):
#     indices = []
#     for i in range(len(arr)):
#         if arr[i] == target:
#             indices.append(i)
#     return indices

# # Example usage:
# my_list = [4, 2, 8, 1, 7, 3, 6]
# target_element = 4
# all_indices = find_all_indices(my_list, target_element)
# print(f"Indices of element {target_element}: {all_indices}")


