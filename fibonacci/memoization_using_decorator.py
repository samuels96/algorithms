
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n<2: return 1
    return fib(n-1) + fib(n-2)


# for x in range(30):
#     print(fib(x))
#______________________
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
# Runtime - 0:00:00.000117
