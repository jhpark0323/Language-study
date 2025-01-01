import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    static ArrayList<Integer> list;
    static int n;
    static int[] sum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        list = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }
        Arrays.sort(list.toArray());
//        System.out.println(Arrays.toString(list.toArray()));

        // x + y = k - z를 이용하기 위해 x+y에 대한 배열을 만듬
        sum = new int[n * (n+1)/2];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                sum[idx] = list.get(i) + list.get(j);
                idx++;
            }
        }

        Arrays.sort(sum);
//        System.out.println(Arrays.toString(sum));
        int ans = 0;
        for (int i = n-1; i >= 0; i--) {
            for (int j = 0; j < i; j++) {
                int target = list.get(i) - list.get(j);

                if (BinarySearch(target) && list.get(i) > ans) {
                    ans = target + list.get(j);
                }
            }
        }
        System.out.println(ans);

    }

    static boolean BinarySearch(int target) {
        int left = 0, right = n * (n+1)/2;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (target == sum[mid]) {
                return true;
            }

            if (target > sum[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}