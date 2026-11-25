# Algorithm: Bubble Sort (Full Name: STEPHEN REPUNTE)

1. START
2. Set `full_name` = "STEPHEN REPUNTE".
3. Create an empty array `unsorted_array`.
4. For each character `ch` in `full_name`:
   1. If `ch` is not a letter (space or symbol), skip it.
   2. If `ch` is already in `unsorted_array` (duplicate), skip it.
   3. Otherwise, add `ch` to the end of `unsorted_array`.
5. Copy `unsorted_array` into `sorted_array`.
6. Let `n` = number of elements in `sorted_array`.
7. For `i` from 0 to `n - 2`:
   1. For `j` from 0 to `n - 2 - i`:
      1. If `sorted_array[j]` > `sorted_array[j + 1]`, swap them.
8. Display `unsorted_array`.
9. Display `sorted_array`.
10. END
