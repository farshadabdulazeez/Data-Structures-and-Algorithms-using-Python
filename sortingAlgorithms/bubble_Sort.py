'''

A Bubble sort is an easy algorithm among the various sorting algorithms. We learn it as a first sorting algorithm. It is easy to learn and highly intuitive. It can be easy to implement into the code, which is much beneficial for beginner software developers. But it is the worst algorithm for sorting the elements in every except because it checks every time the array is sorted or not.

'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Usage:
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(unsorted_array)
print("Bubble Sort:", unsorted_array)


'''

Time Complexity:

The worst-case time complexity of Bubble Sort is O(n^2), where n is the number of elements in the array.
The best-case time complexity occurs when the array is already sorted, resulting in O(n).
The average-case time complexity is O(n^2).

Space Complexity:

Bubble Sort is an in-place sorting algorithm, meaning it uses a constant amount of extra memory (excluding the input array).

Pros:

Simplicity: Bubble Sort is straightforward and easy to understand. It's a good algorithm for educational purposes and small datasets.
In-Place Sorting: Since it only requires a constant amount of additional memory, Bubble Sort can be useful when memory space is limited.

Cons:

Inefficiency for Large Datasets: Bubble Sort is inefficient for large datasets due to its quadratic time complexity. It's not suitable for sorting large arrays or lists.
Poor Performance on Nearly Sorted Data: Even if the array is almost sorted, Bubble Sort requires multiple passes through the entire dataset, making it inefficient.
Comparison with Other Algorithms:

Bubble Sort is usually outperformed by more advanced algorithms like Quick Sort, Merge Sort, and even Insertion Sort for many practical scenarios.

Algorithmic Steps:

Start from the first element and compare it with the next element.
If the first element is greater than the next, swap them.
Move to the next pair of elements and repeat the comparison and swapping process until the end of the array.
After the first pass, the largest element is guaranteed to be at the end of the array.
Repeat the process for the remaining elements, excluding the last sorted one, until the entire array is sorted.

'''