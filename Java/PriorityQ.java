import java.util.*;

//Queue with priority
class QueueElement {
    int element,priority;
    public QueueElement(int a,int b){
        this.element = a;
        this.priority = b;
    }
}

//compare method
class PQ implements Comparator<QueueElement>{
    public int compare(QueueElement e1,QueueElement e2){
        return e1.priority-e2.priority;
    }
}
public class PriorityQ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        PriorityQueue<QueueElement> pq = new PriorityQueue<>(n,new PQ());
        for (int i = 0; i < n; i++) {
            pq.add(new QueueElement(sc.nextInt(), sc.nextInt()));
        }
        for (int i = 0; i < n; i++) {
            System.out.println(pq.poll().element+" ");
        }
    }    
}