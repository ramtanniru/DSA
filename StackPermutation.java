import java.util.*;
class Solution {
    static int isStackPermutation(int n, int[] ip, int[] op) {
        int j = 0;
        Stack<Integer> s = new Stack<>();
        for(int i=0;i<n;i++){
            //push arr1 first element into stack
            s.push(ip[i]);
            //check whether top in stack == first element in arr2
            while(!s.isEmpty() && s.peek()==op[j]){
                //take out top from stack
                s.pop();
                j++;
            }
        }
        if(n==0||s.isEmpty()) return 1;
        return 0;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] ip = new int[n];
        int[] op = new int[n];
        for(int i=0;i<n;i++){
            ip[i] = sc.nextInt();
        }
        for(int i=0;i<n;i++){
            op[i] = sc.nextInt();
        }
        System.out.println(isStackPermutation(n, ip, op));
    }
}