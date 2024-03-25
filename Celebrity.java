import java.util.Scanner;

class Solution
{ 
    static int celebrity(int M[][], int n)
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
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] m = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                m[i][j] = sc.nextInt();
            }
        }
        System.out.println(celebrity(m,n));
    }
}