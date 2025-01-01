import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static int h;
    static int w;
    static int[][] arr;
    static boolean[][] visited;
    static int[] di = new int[]{-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dj = new int[]{0, 1, 1, 1, 0, -1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            h = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            if (w == 0 && h == 0) {
                break;
            }

            arr = new int[w][h];
            visited = new boolean[w][h];

            for (int i = 0; i < w; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < h; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

//            System.out.println(Arrays.deepToString(arr));

            int ans = 0;
            for (int i = 0; i < w; i++) {
                for (int j = 0; j < h; j++) {
                    if (arr[i][j] == 1 && !visited[i][j]) {
                        dfs(i, j);
                        ans++;
                    }
                }
            }
            System.out.println(ans);


        }
    }

    public static void dfs(int row, int col) {
        visited[row][col] = true;
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{row, col});

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int cur_row = cur[0];
            int cur_col = cur[1];

            for (int dij = 0; dij < 8; dij++) {
                int next_r = cur_row + di[dij];
                int next_c = cur_col + dj[dij];

                if (next_r >= 0 && next_r < w && next_c >= 0 && next_c < h && !visited[next_r][next_c] && arr[next_r][next_c] == 1) {
                    stack.push(new int[]{next_r, next_c});
                    visited[next_r][next_c] = true;
                }
            }
        }

    }
}