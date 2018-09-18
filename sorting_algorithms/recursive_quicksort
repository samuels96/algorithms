def quicksort(x):
    if len(x) < 2: return x

    piv = x[len(x)//2]
    
    del x[len(x)//2]
    
    less = [x for x in x if x < piv]
    more = [x for x in x if x > piv]

    return quicksort(less) + [piv] + quicksort(more)
