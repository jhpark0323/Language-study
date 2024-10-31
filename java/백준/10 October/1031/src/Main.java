import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[][] arr;
    static int[][] dp;
    static int[] di = {1, -1, 0, 0};
    static int[] dj = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

//        System.out.println(Arrays.deepToString(arr));
        dp = new int[n][n];

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int newAns = dfs(i, j);
                dp[i][j] = newAns;
                if (newAns > answer) {
                    answer = newAns;
                }
            }
        }

        System.out.println(answer);
//        System.out.println(Arrays.deepToString(dp));
    }
    static class RowCol {
        public int row;
        public int col;
        public int target;
        public int cnt;
        public RowCol(int r, int c, int t, int cnt) {
            this.row = r;
            this.col = c;
            this.target = t;
            this.cnt = cnt;
        }
        @Override
        public String toString() {
            return "(" + row + "," + col + ")";
        }
    }
    static int dfs(int row, int col) {
        boolean[][] visited = new boolean[n][n];
        visited[row][col] = true;
        Deque<RowCol> stack = new LinkedList<>();
        stack.push(new RowCol(row, col, arr[row][col], 1));
        int ans = 0;

        while (!stack.isEmpty()) {
            RowCol cur = stack.pop();
            int r = cur.row;
            int c = cur.col;
            int t = cur.target;
            int cnt = cur.cnt;

            if (ans < cnt) {
                ans = cnt;
            }

            if (dp[r][c] != 0) {
                int new_cnt = dp[r][c] + 1;
                ans = Math.max(ans, new_cnt);
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int newRow = r + di[i];
                int newCol = c + dj[i];

                if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= n) {
                    continue;
                }
                if (!visited[newRow][newCol] && arr[newRow][newCol] > t) {
                    stack.push(new RowCol(newRow, newCol, arr[newRow][newCol], cnt+1));
                }

            }

        }
        return ans;
    }
}