import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];
        int max = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            max = Math.max(max, arr[i]);
        }

        int start = max;
        int end = 1000000000;

        while (start < end) {
            int mid = (start + end) / 2;

            if (check(mid) <= m) {
                end = mid;
            } else {
                start = mid+1;
            }
        }
        System.out.println(start);


    }
    static int check (int k) {
        int now = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (now < arr[i]) {
                now = k;
                cnt++;
            }
            now -= arr[i];
        }
        return cnt;
    }
}