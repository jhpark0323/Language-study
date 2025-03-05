import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_9466 {
    static int n, start, ans;
    static int[] arr;
    static boolean[] visited, done;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr = new int[n+1];
            for (int i = 1; i <= n; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            ans = 0;
            visited = new boolean[n+1];
            done = new boolean[n+1];

            for (int i = 1; i <= n; i++) {
                if (!done[i]) {
                    dfs(i);
                }
            }
            System.out.println(n-ans);
        }
    }

    static void dfs(int nxt) {
        if (visited[nxt]) {
            done[nxt] = true;
            ans++;
        } else {
            visited[nxt] = true;
        }

        if (!done[arr[nxt]]) {
            dfs(arr[nxt]);
        }

        visited[nxt] = false;
        done[nxt] = true;

    }
}
