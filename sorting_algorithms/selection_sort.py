# Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest
# (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

arr = [64, 25, 25, 12, 22, 64, 22, 11]

sorted_arr = []
x = len(arr)

for _ in range(x):
    nex_number = min(arr)
    arr.remove(nex_number)
    sorted_arr.append(nex_number)

print(sorted_arr)
