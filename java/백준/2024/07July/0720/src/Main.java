import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int testcase = 0; testcase < T; testcase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int[] arrA = new int[n];
            int[] arrB = new int[m];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                arrA[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                arrB[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(arrA);
            Arrays.sort(arrB);

            int ans = 0;
            for (int i = 0; i < n; i++) {
                int target = arrA[i];

                if (target <= arrB[0]) {
                    continue;
                }

                int left = 0;
                int right = m-1;

                while (left <= right) {
                    int mid = (left + right) / 2;

                    if (arrB[mid] >= target) {
                        right = mid - 1;
                    } else {
                        left = mid + 1;
                    }
                }
                ans += left;

            }

            System.out.println(ans);

        }
    }
}