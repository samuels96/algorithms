
def fib(n):
    nums = [1,1]
    for x in range(0,n):
        nums = [nums[-1],nums[-2]+nums[-1]]
    return nums[0]

def fib(n):
    first = 0
    second = 1
    for x in range(n):
        first,second = second,first + second
    return first

# for x in range(30):
#     print(fib(x))
#_____________________
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181
# 6765
# 10946
# 17711
# 28657
# 46368
# 75025
# 121393
# 196418
# 317811
# 514229
# 832040
#_____________________
# Runtime - 0:00:00.000198
