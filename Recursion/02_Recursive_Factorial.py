# input_1 = 5
# input_2 = 10
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


number = int(input())
print(factorial(number))
