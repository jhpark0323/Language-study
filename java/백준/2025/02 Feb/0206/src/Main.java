import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, m, k;
    static char[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new char[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = line.charAt(j);
            }
        }

        System.out.println(Math.min(solve('B'), solve('W')));
    }

    static int solve(char color) {
        int cnt = Integer.MAX_VALUE;
        int val;
        int[][] pSum = new int[n+1][m+1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // 그 자리도 바꿔야 하는지
                if ((i + j) % 2 == 0) {
                    val = arr[i][j] != color ? 1 : 0;
                } else {
                    val = arr[i][j] == color ? 1 : 0;
                }
                // 그 칸의 왼쪽, 위쪽 값의 합에 왼쪽위 값을 빼고 그 자리 값을 더해줌
                pSum[i+1][j+1] = pSum[i][j+1] + pSum[i+1][j] - pSum[i][j] + val;
            }
        }
//        System.out.println(Arrays.deepToString(pSum));
        for (int i = 1; i <= n - k + 1; i++) {
            for (int j = 1; j <= m - k + 1; j++) {
                cnt = Math.min(cnt, pSum[i+k-1][j+k-1] - pSum[i+k-1][j-1] - pSum[i-1][j+k-1] + pSum[i-1][j-1]);
            }
        }
        return cnt;
    }
}