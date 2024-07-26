class Solution:
	def shortest_distance(self, matrix):
	    for i in range(len(matrix)):
	        for j in range(len(matrix)):
	            if matrix[i][j]==-1:
	                matrix[i][j] = float('inf')
	                
		for via in range(len(matrix)):
		    for i in range(len(matrix)):
		        for j in range(len(matrix)):
		            matrix[i][j] = min(matrix[i][j],matrix[i][via]+matrix[via][j])
		
		for i in range(len(matrix)):
		    for j in range(len(matrix)):
		        if matrix[i][j]==float('inf'):
		            matrix[i][j] = -1 