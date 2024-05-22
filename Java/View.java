import java.util.*;
class Treenode{
    int val;
    Treenode left,right;
    Treenode(int data){
        val = data;
        left=right=null;
    }
}
class Pair{
    Treenode node;
    int hd;
    Pair(Treenode temp,int val){
        node = temp;
        hd = val;
    }
}
public class View{
    static Treenode root;
    static Treenode insert(Treenode node,int val){
        if(node==null){
            node = new Treenode(val);
            return node;
        }
        if(node.val>val){
            node.left = insert(node.left,val);
        }
        else if(node.val<val){
            node.right = insert(node.right,val);
        }
        return node;
    }
    static void BST(int [] arr){
        for(int i:arr){
            root = insert(root,i);
        }
    }
    static void printLeftView(Treenode root){

        if(root == null){
            return;
        }
        Queue<Treenode> queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
            int n = queue.size();
            for(int i=0;i<n;i++){
                Treenode temp = queue.poll();
                if(i==0){
                    System.out.print(temp.val+" ");
                }
                if(temp.left!=null){
                    queue.add(temp.left);
                }
                if(temp.right!=null){
                    queue.add(temp.right);
                }
            }
        }
        System.out.println();
    }
    static void printRightView(Treenode root){
        if(root==null){
            return;
        }
        Queue<Treenode> queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
            int n = queue.size();
            for(int i=0;i<n;i++){
                Treenode temp = queue.poll();
                if(i==n-1){
                    System.out.print(temp.val+" ");
                }
                if(temp.left!=null){
                    queue.add(temp.left);
                }
                if(temp.right!=null){
                    queue.add(temp.right);
                }
            }
        }
        System.out.println();
    }
    static void printBottoomView(Treenode root){
        if(root==null){
            return;
        }
        Map<Integer,Integer> map = new TreeMap<>();
        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(root,0));

        while(!queue.isEmpty()){
            Pair x = queue.poll();
            Treenode node = x.node;
            int hd = x.hd;
            map.put(hd,node.val);
            if(node.left!=null){
                queue.add(new Pair(node.left,hd-1));
            }
            if(node.right!=null){
                queue.add(new Pair(node.right,hd+1));
            }
        }
        for(int i:map.keySet()){
            System.out.print(map.get(i)+" ");
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        BST(arr);
        printLeftView(root);
        printRightView(root);
        printBottoomView(root);
    }
}