import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];

        long right = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            right = Math.max(right, arr[i]); // 배열에서 가장 큰 값
        }

        long ans = 0;
        long left = 1; // 최소 1부터 시작 (0으로 나누는 문제 방지)
        while (left <= right) {
            long mid = (left + right) / 2;
            int num = 0;

            for (int i = 0; i < n; i++) {
                num += arr[i] / mid; // 현재 mid로 나눌 수 있는 사람 수 계산
            }

            if (num < k) {
                right = mid - 1; // mid가 너무 크므로 감소
            } else {
                ans = mid; // 현재 mid가 가능한 답
                left = mid + 1; // 더 큰 mid 탐색
            }
        }

        System.out.println(ans);
    }
}
