'''

Selection sort is a simple sorting algorithm that repeatedly selects the minimum element from the unsorted part of the array and puts it at the beginning. The algorithm maintains two subarrays - the sorted subarray, which is built from left to right, and the unsorted subarray.

'''

def selection_sort(array):
   
    n = len(array)

    # Traverse through all array elements
    for i in range(n - 1):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]

    return array


# Example usage:
array = [0, 5, 3, 2, 9, 7, 4, 1, 6, 8]
print("Original Array:", array)
print("Sorted Array:", selection_sort(array))

'''
Approach:

The array is divided into two parts: the sorted part on the left and the unsorted part on the right.
In each iteration, the algorithm finds the minimum element in the unsorted part and swaps it with the first element of the unsorted part.
This process is repeated until the entire array is sorted.

Time Complexity:

The time complexity of selection sort is O(n^2) for the worst and average cases, where 'n' is the number of elements in the array.
The number of comparisons is (n-1) + (n-2) + ... + 1 = n*(n-1)/2, which is asymptotically O(n^2).
Space Complexity:

Selection sort has a space complexity of O(1) since it only requires a constant amount of extra space for temporary variables.

Pros:

Simple to understand and implement.
In-place sorting algorithm (requires only a constant amount of additional memory).
Can perform better than other quadratic time complexity algorithms for small datasets or when the list is mostly sorted.

Cons:

Inefficient for large datasets due to its quadratic time complexity.
Not stable: the relative order of equal elements might not be preserved.
Not adaptive: the time complexity remains the same regardless of the input order.
Better alternatives like quicksort or mergesort are often preferred for larger datasets.

'''
