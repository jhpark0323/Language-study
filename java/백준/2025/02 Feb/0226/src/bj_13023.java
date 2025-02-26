import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

// bj_13023
public class bj_13023 {
    static int n, m;
    static List<List<Integer>> list;
    static boolean[] visited;
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list.get(a).add(b);
            list.get(b).add(a);
        }

        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (ans == 0) {
                dfs(i, 1);
            }
        }

        System.out.println(ans);

    }

    static void dfs(int me, int cnt) {
        if (cnt == 5) {
            ans = 1;
            return;
        }

        visited[me] = true;

        for (int friend : list.get(me)) {
            if (!visited[friend]) {
                dfs(friend, cnt + 1);
            }
        }
        visited[me] = false;
    }
}
