import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());


        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
//        System.out.println(Arrays.toString(arr));

        int start = 0;
        int end = n - 1;
        int minVal = Integer.MAX_VALUE;
        int ans_1 = 0;
        int ans_2 = n-1;

        while (start < end) {
            int sum = Math.abs(arr[start] + arr[end]);


            if (minVal > sum) {
                minVal = sum;
                ans_1 = start;
                ans_2 = end;
            }

            if (sum == 0) {
                break;
            }

            if (arr[start] + arr[end] < 0) {
                start++;
            } else {
                end--;
            }

        }
        System.out.println(arr[ans_1] + " " + arr[ans_2]);
//        System.out.println(arr[start] + " " + arr[end]);

    }
}