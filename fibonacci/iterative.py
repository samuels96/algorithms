
def fib(n):
    first = 0
    second = 1
    
    for x in range(n):
        first,second = second,first + second
        
    return first


