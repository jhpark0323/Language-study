import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 9024 두수의 합
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCases = Integer.parseInt(br.readLine());
        for (int testcase = 0; testcase < testCases; testcase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(arr);

            int cnt = 0;
            int left = 0;
            int right = n-1;
            int sum = arr[left] + arr[right];

            while (left < right) {
                int newSum = arr[left] + arr[right];

                // 원래의 sum과 k의 차이보다 새로 만든 newSum과 k의 차이가 같다면
                if (Math.abs(k - sum) == Math.abs(newSum - k)) {
                    cnt++;
                } else if (Math.abs(k - sum) > Math.abs(newSum - k)) {
                    sum = newSum;
                    cnt = 1;
                }

                // newSum이 k보다 작으면
                if (newSum < k) {
                    left++;
                } else if (newSum > k) {
                    right--;
                } else {
                    left++;
                    right--;
                }

            }
            System.out.println(cnt);
        }

    }
}