import java.util.Scanner;

public class RotateArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i = 0;i<n;i++){
            a[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        if(m>n){m=m-n;}
        for(int i=0;i<m;i++){
            int p = a[0];
            for(int j=0;j<n-1;j++){
                a[j] = a[j+1];
            }
            a[n-1] = p;
        }
        for(int i:a){
            System.out.print(i+" ");
        }
    }
}
