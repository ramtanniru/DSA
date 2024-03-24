class Solution
{ 
    int celebrity(int M[][], int n)
    {
    	int i=0,j=n-1;
    	while(i<j){
    	    if(M[j][i]==1){
    	        j--;
    	    }
    	    else{
    	        i++;
    	    }
    	}
    	int c = i;
    	for(i=0;i<n;i++){
    	    if(M[c][i]==1||M[i][c]==0){
    	        if(i!=c){
    	            return -1;
    	        }
    	    }
    	}
    	return c;
    }
}