import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int [] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // n, m
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());

        // 왼쪽 값은 모든 강의 내용이 적어도 하나는 들어가야하기 때문에 강의들 중에 제일 큰값으로 잡는다.
        int left = 0;
        // 오른쪽 값은 모든 강의내용의 합으로 한다.
        int right = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (left < arr[i]) {
                left = arr[i];
            }
            right += arr[i];
        }
//        System.out.println(Arrays.toString(arr));

        while (left <= right) {
            int mid = (left + right) / 2;

            int cnt = find(mid);

            if (cnt > m) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(left);

    }

    public static int find(int mid) {
        int sum = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (sum + arr[i] > mid) {
                sum = 0;
                cnt++;
            }
            sum += arr[i];
        }
        if (sum != 0) {
            cnt++;
        }
        return cnt;
    }
}