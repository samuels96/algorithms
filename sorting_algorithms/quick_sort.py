# Quick sort
# Time Complexity: O(n2) with O(n log(n)) average
# Space Complexity: O(n)

def quick_sort(arr):
    if len(arr)<=1: return arr
    small,equal,large = [],[],[]
    pivot = arr[randint(0,len(arr)-1)]

    for i in arr:
        if i<pivot: small.append(i)
        if i>pivot: large.append(i)
        if i == pivot: equal.append(i)

    return quick_sort(small)+equal+quick_sort(large)
