# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

def gen_01(ind, arr):
    if ind >= len(arr):
        print(*arr, sep='')
        return
    for num in range(0, 2):
        arr[ind] = num
        gen_01(ind + 1, arr)


array = [None for n in range(int(input()))]

gen_01(0, array)
