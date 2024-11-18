def maxSubMatrix(matrix,n):
	rows = len(matrix)
	cols = len(matrix[0])
	dp = [[0] * cols for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			dp[i][j] = matrix[i][j]
			if i > 0:
				dp[i][j] += dp[i-1][j]
			if j > 0:
				dp[i][j] += dp[i][j-1]
			if i > 0 and j > 0:
				dp[i][j] -= dp[i-1][j-1]
	max_sum = float('-inf')
	for size in range(1,n):
	    for i in range(size-1, rows):
		    for j in range(size-1, cols):
			    submatrix_sum = dp[i][j]
			    if i >= size:
				    submatrix_sum -= dp[i-size][j]
			    if j >= size:
				    submatrix_sum -= dp[i][j-size]
			    if i >= size and j >= size:
				    submatrix_sum += dp[i-size][j-size]
			    if submatrix_sum > max_sum:
				    max_sum = submatrix_sum
				    max_submatrix = [row[j-size+1:j+1] for row in matrix[i-size+1:i+1]]
	return max_submatrix

n = int(input())
mat = [[int(i) for i in input().split()] for i in range(n)]
print(maxSubMatrix(mat,n))