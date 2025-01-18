import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    static int n;
    static int m;
    static boolean find(int mid) {
        int start = 0;

        for (int i = 0; i < m; i++) {
            // 저번 가로등이 비추는 끝 부분 보다 이번 가로등의 시작 부분이 더 작거나 같으면
            // 가능하다는 소리
            if (arr[i] - mid <= start) {
                start = arr[i] + mid;
            }
            // 그렇지 않으면
            else {
                return false;
            }
        }
        if (start >= n) {
            return true;
        }
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        arr = new int[m];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 1;
        int right = n;
        while (left < right) {
            int mid = (left + right) / 2;

            if (find(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        System.out.println(left);

    }
}