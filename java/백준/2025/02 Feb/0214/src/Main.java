import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// bj_1365
public class Main {
    static int[] lis;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        lis = new int[n+1];
        int idx = 0;
        int len = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] > lis[len]) {
                len++;
                lis[len] = arr[i];
            } else {
                idx = binarySearch(len, arr[i]);
                lis[idx] = arr[i];
            }
        }
        System.out.println(n - len);
    }

    static int binarySearch(int right, int target) {
        int left = 0;
        while (left < right) {
            int mid = (left + right) / 2;

            if (lis[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return right;
    }
}