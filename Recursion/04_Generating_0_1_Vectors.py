# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

def gen_01(ind, arr):
    if ind > len(arr) - 1:
        return

    for num in range(0, 2):
        arr[ind] = num
        gen_01(ind + 1, arr)
    print(arr)


array = [0 for n in range(int(input()))]
gen_01(0, array)
