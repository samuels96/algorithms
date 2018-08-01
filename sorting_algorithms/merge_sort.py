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
