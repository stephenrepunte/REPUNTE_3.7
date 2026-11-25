full_name = "STEPHEN REPUNTE"

# Build the unsorted array: letters only (symbols/spaces excluded), duplicates discarded
unsorted_array = []
for ch in full_name:
    if ch.isalpha() and ch not in unsorted_array:
        unsorted_array.append(ch)

# Bubble Sort
sorted_array = unsorted_array.copy()
n = len(sorted_array)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if sorted_array[j] > sorted_array[j + 1]:
            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

print("Unsorted array:", unsorted_array)
print("Sorted array:  ", sorted_array)
