import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int testcase = 0; testcase < T; testcase++) {
            int n = Integer.parseInt(br.readLine());
            int[][] dp = new int[10001][4];
            dp[1][1] = 1;
            dp[2][1] = 1;
            dp[2][2] = 1;
            dp[3][1] = 1;
            dp[3][2] = 1;
            dp[3][3] = 1;
            for (int i = 4; i <= n; i++) {
                dp[i][1] = dp[i-1][1];
                dp[i][2] = dp[i-2][1] + dp[i-2][2];
                dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3];
            }
            System.out.println(dp[n][1] + dp[n][2] + dp[n][3]);
        }
    }
}