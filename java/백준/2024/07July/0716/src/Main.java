import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        int max = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            max = Math.max(max, arr[i]);
        }

        long ans = 0;

        int left = 1;
        int right = max;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (mid == 0) {
                break;
            }

            int nephew = find(mid);
//            System.out.println(nephew + " " + mid);


            if (nephew >= m) {
                left = mid + 1;
                ans = mid;
            } else {
                right = mid - 1;
            }
        }
        System.out.println(ans);

    }

    public static int find(int val) {
        int nephew = 0;
        for (int i = 0; i < n; i++) {
            nephew += arr[i] / val;
        }
        return nephew;
    }
}