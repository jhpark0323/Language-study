import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// bj_1520
public class Main {
    static int m, n;
    static int[][] arr, dp;
    static int[] di = {1, -1, 0, 0};
    static int[] dj = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        arr = new int[m+1][n+1];
        for (int i = 1; i <= m; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp = new int[m+1][n+1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = -1;
            }
        }
        System.out.println(dfs(1, 1));
    }

    static int dfs(int row, int col) {
        if (row == m && col == n) {
            return 1;
        }

        if (dp[row][col] != -1) {
            return dp[row][col];
        }

        dp[row][col] = 0;
        for (int dij = 0; dij < 4; dij++) {
            int newRow = row + di[dij];
            int newCol = col + dj[dij];

            if (newRow < 1 || newRow > m || newCol < 1 || newCol > n) {
                continue;
            }

            if (arr[row][col] > arr[newRow][newCol]) {
                dp[row][col] += dfs(newRow, newCol);
            }

        }
        return dp[row][col];
    }
}