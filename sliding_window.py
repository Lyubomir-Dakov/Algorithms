from math import inf

arr = [30, 50, -60, 90, 100, -13, 27]
k = 2


def sliding_window(arr, k):
    max_sum = -inf
    current_sum = sum([arr[i] for i in range(k)])

    for i in range(len(arr) - k):
        current_sum = current_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, current_sum)

    return max_sum


result = sliding_window(arr, k)
print(result)
