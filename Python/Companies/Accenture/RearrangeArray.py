# Statement: Function that rearranges the given array in such a way that smallest number comes first, 
# largest comes second and second smallest comes third and so on.
# input: 6 2 4 1 3 5
# output: 1 6 2 5 3 4
def rearrangeArray(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i%2!=0 and arr[i]<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            elif i%2==0 and arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
arr = [int(i) for i in input().split()]
print(rearrangeArray(arr))