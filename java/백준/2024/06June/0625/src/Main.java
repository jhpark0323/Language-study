import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // testCase 갯수 받기
        int testCase = Integer.parseInt(br.readLine());

        // testCase만큼 반복하여 실행
        for (int i = 0; i < testCase; i++) {

            // n받기
            n = Integer.parseInt(br.readLine());

            // arr을 만들기 위한 st 만들기
            StringTokenizer st = new StringTokenizer(br.readLine());

            // arr 만들어서 받기
            arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(arr);

//            System.out.println(Arrays.toString(arr));

            // m받기
            int m = Integer.parseInt(br.readLine());

            // 수첩2의 숫자 하나씩 받기
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < m; j++) {
                int num = Integer.parseInt(st.nextToken());
                int ans = BinarySearch(num);
                sb.append(ans).append("\n");
            }
        }
        System.out.print(sb.toString());
        br.close();

    }

    public static int BinarySearch(int num) {
        int start = 0;
        int end = n - 1;

        while (start <= end) {
            int mid = (start + end) / 2;
            int midVal = arr[mid];

            if (num > midVal) {
                start = mid + 1;
            } else if (num < midVal) {
                end = mid - 1;
            } else {
                return 1;
            }
        }
        return 0;

    }
}