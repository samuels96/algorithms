#Bubble sort
#Time complexity: О(n2)
#Space complexity: O(1)

def bubble_sort(arr):
    for _ in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i+1],arr[i] = arr[i],arr[i+1]
    return arr
