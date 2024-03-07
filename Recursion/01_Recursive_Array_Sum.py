# input_1 = "1 2 3 4"
# input_2 = "-1 0 1"

def arr_sum(arr):
    if len(arr) == 1:
        return arr[0]

    for i in range(len(arr)):
        return arr[i] + arr_sum(arr[(i + 1):])


array = [int(num) for num in input().split()]
print(arr_sum(array))
