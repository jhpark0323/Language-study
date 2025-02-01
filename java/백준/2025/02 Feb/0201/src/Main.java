import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static char[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new char[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = line.charAt(j);
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == 'L') {
                    int newAns = bfs(i ,j);
                    ans = Math.max(ans, newAns);
                }
            }
        }

        System.out.println(ans);

    }
    static class Point {
        int row, col, cnt;

        Point(int row, int col, int cnt) {
            this.row = row;
            this.col = col;
            this.cnt = cnt;
        }
    }

    static int bfs(int row, int col) {
        int max = 0;
        int[] di = {1, -1, 0, 0};
        int[] dj = {0, 0, 1, -1};
        boolean[][] visited = new boolean[n][m];
        visited[row][col] = true;
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(row, col, 0));
        while (!q.isEmpty()) {
            Point cur = q.poll();
            int curRow = cur.row;
            int curCol = cur.col;
            int curCnt = cur.cnt;

            max = Math.max(max, curCnt);

            for (int dij = 0; dij < 4; dij++) {
                int newRow = curRow + di[dij];
                int newCol = curCol + dj[dij];

                if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= m || visited[newRow][newCol]) {
                    continue;
                }

                if (arr[newRow][newCol] == 'W') {
                    continue;
                }

                visited[newRow][newCol] = true;
                q.offer(new Point(newRow, newCol, curCnt + 1));

            }

        }
        return max;
    }

}