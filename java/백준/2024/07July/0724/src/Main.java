import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int INF = Integer.MAX_VALUE;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int left = 0;
        int right = -1;

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            right = Math.max(right, arr[i]);
        }

        while (left < right) {
            int mid = (left + right) / 2;
            if (solve(mid) <= m) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        System.out.println(right);

    }
    public static int solve(int mid) {
        int cnt = 1;
        int min = INF;
        int max = -INF;

        for (int i = 0; i < n; i++) {
            min = Math.min(min, arr[i]);
            max = Math.max(max, arr[i]);
            if (max - min > mid) {
                cnt++;
                max = -INF;
                min = INF;
                i--;
            }
        }
        return cnt;

    }
}