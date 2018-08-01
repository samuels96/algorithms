#Selection sort
# Time complexity: O(n2)
# Space Complexity: O(1)

def selection_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr
