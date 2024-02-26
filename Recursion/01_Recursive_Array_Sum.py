# input_1 = "1 2 3 4"
# input_2 = "-1 0 1"
def sum_array(arr, ind):
    if ind == len(arr) - 1:
        return arr[ind]
    return arr[ind] + sum_array(arr, ind + 1)


array = [int(num) for num in input().split()]

print(sum_array(array, 0))
