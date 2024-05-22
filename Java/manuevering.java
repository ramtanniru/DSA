import java.util.*;
public class manuevering {
    static int man(int m,int n){
        if(m==1 || n==1){
            return 1;
        }
        return man(m-1,n)+man(m,n-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        System.out.println(man(m,n));
    }
}
