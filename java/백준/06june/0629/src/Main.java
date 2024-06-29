import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int ans = 0;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
//        System.out.println(Arrays.toString(arr));

        for (int i = 0; i < n; i++) {
            BinarySearch(arr[i], i);
        }

        System.out.println(ans);
        br.close();

    }

    public static void BinarySearch(int num, int index) {
        int start = 0;
        if (start == index) {
            start++;
        }
        int end = n - 1;
        if (end == index) {
            end--;
        }

        while (start < end) {
            int sum = arr[start] + arr[end];

            if (sum == num) {
                ans++;
//                System.out.println(num);
                return;
            }

            if (sum < num) {
                start++;
                // 만약 start가 index와 같아지면 걔는 넘김
                if (start == index) {
                    start++;
                }
            } else {
                end--;
                // 만약 end가 index와 같아지면 걔는 넘김
                if (end == index) {
                    end--;
                }
            }

        }

    }
}