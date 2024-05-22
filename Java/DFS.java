import java.util.*;
public class DFS {
    static int V;
    static LinkedList<Integer> adj[];
    DFS(int v){
        V = v;
        adj = new LinkedList[v];
        for(int i=0;i<v;i++){
            adj[i] = new LinkedList();
        }
    }
    static void addEdge(int u,int v){
        adj[u].add(v);
    }
    static void dfs(int v){
        boolean[] visited = new boolean[V];
        dfsUtil(v,visited);
    }
    static void dfsUtil(int v,boolean[] visited){
        visited[v] = true;
        System.out.print(v+" ");
        Iterator<Integer> i = adj[v].listIterator();
        while(i.hasNext()){
            int n = i.next();
            if(!visited[n]){
                dfsUtil(n,visited);
            }
        }
    }
    static void bfs(int v){
        boolean[] visited = new boolean[V];
        visited[v] = true;
        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(v);
        while(queue.size()!=0){
            v = queue.poll();
            System.out.print(v+" ");
            Iterator<Integer> i = adj[v].listIterator();
            while(i.hasNext()){
                int n = i.next();
                if(!visited[n]){
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        DFS g = new DFS(sc.nextInt());
        while(sc.hasNext()){
            g.addEdge(sc.nextInt(),sc.nextInt());
        }
        dfs(0);
        bfs(0);
    }
}
