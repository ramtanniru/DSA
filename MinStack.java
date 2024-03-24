import java.util.*;
class Main{
    static Stack<Integer> s = new Stack<>();
    static Stack<Integer> a = new Stack<>();
    static void push(int n){
        if(s.isEmpty()){
            s.push(n);
            a.push(n);
        }
        else{
            s.push(n);
        }
        if(n<a.peek()){
            a.push(n);
        }
    }
    static void min(){
        if(s.empty()){
            System.out.println("No elements");
        }
        System.out.println(a.peek());
    }
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0;i<n;i++){
            push(sc.nextInt());
        }
        min();
    }
}