# input_1 = 5
# input_2 = 10

def f(num):
    if num == 1:
        return 1
    return num * f(num - 1)


number = int(input())
print(f(number))
