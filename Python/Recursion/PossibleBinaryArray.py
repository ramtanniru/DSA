def generate(n,i,arr):
    if i==n:
        print(arr)
        return
    arr[i] = 0
    generate(n,i+1,arr)
    arr[i] = 1
    generate(n,i+1,arr)
    
generate(4,0,[-1,-1,-1,-1])