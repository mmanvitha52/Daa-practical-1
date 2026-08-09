def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop if no swaps occurred
        if not swapped:
            break


def print_array(arr):
    for element in arr:
        print(element, end=" ")

    print()


# Main program
n = int(input("Enter the number of elements: "))

arr = []

print("Enter", n, "elements:")

for i in range(n):
    arr.append(int(input()))

bubble_sort(arr)

print("Sorted array:", end=" ")
print_array(arr)

print("Roll No: 92460118698")
# Time Complexity:
# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)
# Space Complexity: O(1)