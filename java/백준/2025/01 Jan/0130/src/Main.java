import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] di = {-1, -2, -2, -1, 1, 2, 2, 1};
    static int[] dj = {-2, -1, 1, 2, 2, 1, -1, -2};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int startRow = Integer.parseInt(st.nextToken());
            int startCol = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int endRow = Integer.parseInt(st.nextToken());
            int endCol = Integer.parseInt(st.nextToken());

            int ans = bfs(startRow, startCol, endRow, endCol, n);
            System.out.println(ans);

        }
    }

    static class Node {
        int row, col, cnt;
        Node(int row, int col, int cnt) {
            this.row = row;
            this.col = col;
            this.cnt = cnt;
        }
    }

    static int bfs(int startRow, int startCol, int endRow, int endCol, int n) {
        boolean[][] visited = new boolean[n][n];
        visited[startRow][startCol] = true;
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(startRow, startCol, 0));
        while (!q.isEmpty()) {
            Node cur = q.poll();
            int curRow = cur.row;
            int curCol = cur.col;
            int curCnt = cur.cnt;

            if (curRow == endRow && curCol == endCol) {
                return curCnt;
            }

            for (int dij = 0; dij < 8; dij++) {
                int newRow = curRow + di[dij];
                int newCol = curCol + dj[dij];

                if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= n || visited[newRow][newCol]) {
                    continue;
                }

                visited[newRow][newCol] = true;
                q.offer(new Node(newRow, newCol, curCnt + 1));

            }

        }
        return -1;
    }
}















