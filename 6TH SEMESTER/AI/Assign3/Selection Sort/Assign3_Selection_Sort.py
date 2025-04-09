def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Taking user input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("\nOriginal List:", numbers)
selection_sort(numbers)
print("Sorted List:", numbers)
