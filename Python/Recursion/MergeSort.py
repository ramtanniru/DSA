# merging
def merge(left,right):
    i,j = 0,0
    arr = []
    while i<len(left) and j<len(right):
        if(left[i]>right[j]):
            arr.append(right[j])
            j+=1
        else:
            arr.append(left[i])
            i+=1
    while i<len(left):
        arr.append(left[i])
        i+=1
    while j<len(right):
        arr.append(right[j])
        j+=1
    return arr

# dividing and sorting
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)

arr = [int(i) for i in input().split()]
print(mergeSort(arr))