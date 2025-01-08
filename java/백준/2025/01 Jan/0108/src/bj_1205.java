import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj_1205 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int score = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        if (n == 0) {
            System.out.println(1);
            return;
        }

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        int ans = 1;
        int sameNum = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] > score) {
                ans++;
            } else if (arr[i] == score) {
                sameNum++;
            }
        }

        if (sameNum > 0 && ans + sameNum > p || ans > p) {
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }
    }
}
