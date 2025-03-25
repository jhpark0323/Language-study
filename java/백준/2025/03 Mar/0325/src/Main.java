import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] arr, sign;
    static int resultMin = Integer.MAX_VALUE;
    static int resultMax = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        sign = new int[4];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            sign[i] = Integer.parseInt(st.nextToken());
        }


        dfs(1, arr[0]);

        System.out.println(resultMax);
        System.out.println(resultMin);

    }
    static void dfs(int idx, int sum) {
        if (idx == n) {
            resultMin = Math.min(sum, resultMin);
            resultMax = Math.max(sum, resultMax);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (sign[i] == 0) {
                continue;
            }
            sign[i]--;
            switch (i) {
                case 0:
                    dfs(idx+1, sum+arr[idx]);
                    break;
                case 1:
                    dfs(idx+1, sum-arr[idx]);
                    break;
                case 2:
                    dfs(idx+1, sum*arr[idx]);
                    break;
                case 3:
                    dfs(idx+1, sum/arr[idx]);
                    break;
            }
            sign[i]++;
        }

    }
}