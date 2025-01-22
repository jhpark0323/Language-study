import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

class Node {
    int idx, height;
    Node(int idx, int height) {
        this.idx = idx;
        this.height = height;
    }
}
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] ans = new int[n+1];
        Stack<Node> stack = new Stack<>();

        for (int i = 1; i <= n; i++) {
            int height = Integer.parseInt(st.nextToken());

            if (stack.isEmpty()) {
                stack.push(new Node(i, height));
            } else {
                while (true) {
                    if (stack.isEmpty()) {
                        stack.push(new Node(i, height));
                        break;
                    }

                    Node top = stack.peek();

                    if (top.height > height) {
                        ans[i] = top.idx;
                        stack.push(new Node(i, height));
                        break;
                    } else {
                        stack.pop();
                    }

                }
            }
        }
        // ans 배열을 1부터 n까지 출력, 공백으로 구분
        for (int i = 1; i <= n; i++) {
            System.out.print(ans[i] + " ");
        }
    }
}
