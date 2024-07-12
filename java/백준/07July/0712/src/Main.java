import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        String[] str = br.readLine().split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }
        Arrays.sort(arr);
//        System.out.println(Arrays.toString(arr));

        // a + b + c = 0
        // a + b = -c
        // -c들을 순회
        long ans = 0;
        for (int i = n-1; i >= 2; i--) {
            int c = -arr[i];
            int left = 0;
            int right = i-1;

            while (left < right) {
                if (arr[left] + arr[right] == c) {
                    if (arr[left] == arr[right]) {
                        int cnt = right - left + 1;
                        ans += cnt * (cnt - 1) / 2;
                        break;
                    } else {
                        int l = 1;
                        int r = 1;
                        while (left+1 < right && arr[left] == arr[left + 1]) {
                            l++;
                            left++;
                        }
                        while (left < right-1 && arr[right] == arr[right - 1]) {
                            r++;
                            right--;
                        }
                        ans += l*r;
                        left++;
                        right--;
                    }
                } else if (arr[left] + arr[right] < c) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        System.out.println(ans);
    }
}