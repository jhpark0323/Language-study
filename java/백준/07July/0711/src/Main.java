import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while ((input = br.readLine()) != null) {
            int x = Integer.parseInt(input) * 10000000;
            int n = Integer.parseInt(br.readLine());

            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(br.readLine());
            }
            Arrays.sort(arr);

            int left = 0;
            int right = n-1;

            int[] ans = new int[2];

            boolean found = false;

            while (left < right) {
                if (arr[left] + arr[right] == x) {
                    if (Math.abs(ans[0] - ans[1]) <= Math.abs(arr[left] - arr[right])) {
                        ans[0] = arr[left];
                        ans[1] = arr[right];
                        System.out.println("yes " + ans[0] + " " + ans[1]);
                        found = true;
                        break;
                    }
                }

                if (arr[left] + arr[right] < x) {
                    left++;
                } else {
                    right--;
                }
            }
            if (!found) {
                System.out.println("danger");
            }
        }
    }
}