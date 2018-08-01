#Bubble sort
#Time complexity: О(n2)
#Space complexity: O(1)

def bubble_sort(arr):
    for _ in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i+1],arr[i] = arr[i],arr[i+1]
    return arr

#Merge sort
#Time complexity: O(n log(n))
#Space compplexity: O(n)

def merge_sort(arr):
    def merge(a,b):
        res = []
        a_idx,b_idx = 0,0
        while a_idx<len(a) and b_idx<len(b):
            if a[a_idx]<b[b_idx]:
                res.append(a[a_idx])
                a_idx += 1
            else:
                res.append(b[b_idx])
                b_idx+=1
        res.extend(b[b_idx:]) if a_idx==len(a) else res.extend(a[a_idx:])
        return res

    def m_sort(arr):
        if len(arr)<=1: return arr
        first,last = m_sort(arr[:len(arr)//2]),m_sort(arr[len(arr)//2:])
        return merge(first,last)

    return m_sort(arr)

#Insertion and selection sort
# Time complexity: O(n2)
# Space Complexity: O(1)

def selection_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            else:
                break
    return arr

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
