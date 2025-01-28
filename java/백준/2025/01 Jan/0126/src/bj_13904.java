import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class bj_13904 {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        List<Node> list = new ArrayList<>();
        int maxDay = 0;
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            list.add(new Node(d, w));
            maxDay = Math.max(maxDay, d);
        }

        int sum = 0;

        for (int i = maxDay; i > 0; i--) {
            Node ans = new Node(0, 0);

            for (Node node : list) {
                if (node.d >= i) {
                    if (ans.w < node.w) {
                        ans = node;
                    }
                }
            }
            sum += ans.w;
            list.remove(ans);
        }
        System.out.println(sum);
    }
}
class Node {
    int d, w;
    Node(int d, int w) {
        this.d = d;
        this.w = w;
    }
}