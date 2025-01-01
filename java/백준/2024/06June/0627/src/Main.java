import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);
//        System.out.println(Arrays.toString(arr));

        int left = 1;
        int right = arr[n-1] - arr[0] + 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (func(mid) < c) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        System.out.println(left-1);
    }

    public static int func(int mid) {
        int cnt = 1;
        int lastHouse = arr[0];

        for (int i = 1; i < arr.length; i++) {
            int dist = arr[i] - lastHouse;

            if (dist >= mid) {
                cnt++;
                lastHouse = arr[i];
            }

        }
        return cnt;
    }

}