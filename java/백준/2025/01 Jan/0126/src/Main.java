import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int cnt;
    static int[][] map;
    static boolean[][] visited;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        visited = new boolean[n][m];

        PriorityQueue<Field> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                // 겉 부분 pq에 삽입
                if (i == 0 || j == 0 || i == n-1 || j == m-1) {
                    pq.add(new Field(i, j, map[i][j]));
                    visited[i][j] = true;
                }
            }
        }

        cnt = Integer.parseInt(br.readLine());
        bfs(n, m, pq);
        System.out.println(sb.toString());

    }
    static void bfs(int n, int m, PriorityQueue<Field> pq) {
        int[] dx = {0, 1, 0, -1};
        int[] dy = {-1, 0, 1, 0};

        while (!pq.isEmpty()) {
            Field field = pq.poll();
            cnt--;
            sb.append(field.row + 1).append(" ").append(field.col + 1).append("\n");
            if (cnt == 0) {
                return;
            }

            int row = field.row;
            int col = field.col;

            for (int i = 0; i < 4; i++) {
                int y = row + dx[i];
                int x = col + dy[i];

                if (y < 0 || y >= n || x < 0 || x >= m || visited[y][x]) {
                    continue;
                }
                visited[y][x] = true;
                pq.add(new Field(y, x, map[y][x]));
            }

        }

    }
}

class Field implements Comparable<Field> {
    int row, col, cost;
    public Field(int row, int col, int cost) {
        this.row = row;
        this.col = col;
        this.cost = cost;
    }

    @Override
    public int compareTo(Field o) {
        return o.cost - this.cost;
    }
}