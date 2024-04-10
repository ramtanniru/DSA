// Number of permutations and combinations
import java.util.*;
public class numOfperm {
    static int fact(int n){
        n++;
        int[] a = new int[n];
        a[0] = 1;
        a[1] = 1;
        for(int i=2;i<n;i++){
            a[i] = a[i-1]*i;
        }
        return a[n-1];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int nPr = fact(a)/fact(a-b);
        int nCr = fact(a)/(fact(b)*fact(a-b));
        System.out.println(nPr);
        System.out.println(nCr);
    }
}
