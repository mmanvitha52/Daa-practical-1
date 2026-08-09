def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Main program
n = int(input("Enter the number of elements: "))

arr = []

print("Enter", n, "elements:")

for i in range(n):
    arr.append(int(input()))

selection_sort(arr)

print("Sorted array:", end=" ")

for element in arr:
    print(element, end=" ")
# Time Complexity:
# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2)
# Space Complexity: O(1) 