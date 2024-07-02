import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        int left = 0;
        int right = n - 1;
        int total = Integer.MAX_VALUE;

        int[] idx = new int[2];

        while (left < right) {
            int sum = Math.abs(arr[left] + arr[right]);

            if (total > sum) {
                total = sum;
                idx[0] = left;
                idx[1] = right;
            }

            if (sum == 0) {
                idx[0] = left;
                idx[1] = right;
                break;
            } else if (arr[left] + arr[right] < 0) {
                left++;
            } else {
                right--;
            }
        }
        System.out.println(arr[idx[0]] + " " + arr[idx[1]]);

    }
}