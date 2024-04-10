import java.util.Scanner;

class Hanoi {
    static void t(int N,char s,char d,char a){
        if(N==0){
            return;
        }
        t(N-1,s,a,d);
        System.out.println("move disk "+N+" from rod "+s+" to rod "+d);
        t(N-1,a,d,s);
    }
    static long toh(int N, char s, char d, char a) {
        t(N,s,d,a);
        long r = (long) (Math.pow(2,N)-1);
        return r;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(toh(n,'S','D','A'));
    }
}