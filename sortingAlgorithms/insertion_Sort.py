'''

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, it performs well for small datasets or nearly sorted datasets.

Algorithm:

Start with the second element (assuming the first element is already sorted).
Compare the current element with its adjacent element.
If the elements are in the wrong order, swap them.
Move the current element back through the sorted part of the array until it's in the correct position.
Repeat the process for the remaining unsorted elements.

Time Complexity:

Worst-case time complexity: O(n^2) comparisons and swaps.
Best-case time complexity: O(n) when the array is nearly sorted.
Average-case time complexity: O(n^2).
Insertion Sort is not the most efficient algorithm for large datasets due to its quadratic time complexity.

Pros:

Simple Implementation: Insertion Sort is easy to understand and implement.
Efficient for Small Datasets: Performs well for small datasets or nearly sorted datasets.
Adaptive: It becomes more efficient when dealing with partially sorted arrays.

Cons:

Inefficiency for Large Datasets: Becomes highly inefficient for large datasets due to its quadratic time complexity.
Not Suitable for Linked Lists: It's less efficient for linked lists compared to arrays because of the sequential nature of array access.

'''

def Insertion(list1):
    # Iterate over the list starting from the second element
    for i in range(1, len(list1)):
        temp = list1[i]  # Store the current element
        j = i - 1  # Initialize a pointer to the previous element

        # Move elements greater than temp to the right
        # until the correct position for temp is found
        while temp < list1[j] and j >= 0:
            list1[j + 1], list1[j] = list1[j], temp
            j -= 1

    return list1

# Example usage:
result = Insertion([0, 10, 6, 3, 8, 5, 2, 7, 4, 1, -1, 9])
print(result)


# Reverse Insertion Sort

# def reverse_insertion_sort(list1):
#     for i in range(1, len(list1)):
#         temp = list1[i]
#         j = i - 1
#         while temp > list1[j] and j > -1:
#             list1[j + 1] = list1[j]
#             j -= 1
#         list1[j + 1] = temp
#     return list1
#
#
# print(reverse_insertion_sort([0, 10, 6, 3, 8, 5, 2, 7, 4, 1, -1, 9]))


# String Insertion Sort

# def string_insertion_sort(list1):
#     for i in range(1, len(list1)):
#         temp = list1[i]
#         j = i - 1
#         while j >= 0 and temp < list1[j]:
#             list1[j + 1] = list1[j]
#             j -= 1
#         list1[j + 1] = temp
#     return list1
#
# words = ["banana", "apple", "grape", "cherry", "pear"]
# print(string_insertion_sort(words))



