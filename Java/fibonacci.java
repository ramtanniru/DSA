import java.util.Arrays;
import java.util.Scanner;

public class fibonacci {
    static int[] dp;

    static int fib(int n){
        if(dp[n]!=-1){
            return dp[n];
        }
        dp[n] = fib(n-1) + fib(n-2);
        return dp[n];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        dp = new int[n+1];
        for(int i=0;i<dp.length;i++){
            dp[i] = -1;
        }
        dp[0] = 0;
        dp[1] = 1;
        fib(n);
        System.out.println(Arrays.toString(dp));
    }
}