import java.util.LinkedList;
import java.util.Queue;

public class QueueTest {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(10);

        for (int i=0; i < 5; i++) {
            queue.offer(i);
        }

        while (!queue.isEmpty()) {
            System.out.println(queue.poll());
        }

    }
}
