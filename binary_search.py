arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            left = mid - 1

    return -1


result = binary_search(arr, target)

if not result == -1:
    print(f"The target is on {result} index in out array!")
else:
    print(f"The target is not presented in out array!")
