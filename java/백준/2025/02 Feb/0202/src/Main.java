import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

// bj_3896
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> list = new ArrayList<>();
        int[] arr = new int[1299711];
        for (int i = 2; i < 1299710; i++) {
            if (arr[i] == 0) {
                list.add(i);
            }

            for (int j = i; j < 1299710; j += i) {
                arr[j] = 1;
            }
        }

        int n = list.size();
//        System.out.println(list);
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int k = Integer.parseInt(br.readLine());

            if (k == 1 || list.contains(k)) {
                System.out.println(0);
                continue;
            }

            int left = 0;
            int right = n;

            while (left <= right) {
                int mid = (left + right) / 2;

                if (list.get(mid) < k && list.get(mid + 1) > k) {
                    System.out.println(list.get(mid+1) - list.get(mid));
                    break;
                }

                if (list.get(mid) < k) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }

            }


        }
    }
}