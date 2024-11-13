# Find the longest increasing consecutive sequence with atmost one skip
def solve(arr):
    n = len(arr)
    if n <= 1:
        return n

    # Arrays to store the length of increasing sequences ending at each index
    left = [1] * n
    right = [1] * n

    # Fill left: longest increasing sequence ending at each index
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            left[i] = left[i - 1] + 1

    # Fill right: longest increasing sequence starting at each index
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            right[i] = right[i + 1] + 1

    # Compute the maximum sequence length with at most one skip
    max_len = max(left)  # Maximum length without any skip
    for i in range(1, n - 1):
        if arr[i - 1] < arr[i + 1]:  # Condition to skip arr[i]
            # Combine the lengths from left and right with a skip at arr[i]
            max_len = max(max_len, left[i - 1] + right[i + 1])

    return max_len
    
arr = [int(i) for i in input().split()]
print(solve(arr))