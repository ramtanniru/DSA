import java.util.Scanner;

class Solution
{
    public static int[] calculateSpan(int a[], int n)
    {
        int[] ans = new int[n];
        ans[0] = 1;
        for(int i=1;i<n;i++){
            int c = 1;
            while((i-c>=0) && (a[i]>=a[i-c])){
                c += ans[i-c];
            }
            ans[i] = c;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i=0;i<n;i++){
            a[i] = sc.nextInt();
        }
        System.out.println(calculateSpan(a, n));
    }
}