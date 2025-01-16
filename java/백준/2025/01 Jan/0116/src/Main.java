import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// snowman1을 이중 for문으로 만듬
// snowman2는 투 포인터로 해서 snowman1과의 차이를 비교
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

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                int snowman1 = arr[i] + arr[j];

                int left = 0;
                int right = n-1;

                while (left < right) {
                    // 같은 눈덩이 선택시 패스
                    if (left == i || left == j) {
                        left++;
                        continue;
                    }
                    if (right == i || right == j) {
                        right--;
                        continue;
                    }

                    int snowman2 = arr[left] + arr[right];
                    ans = Math.min(ans, Math.abs(snowman1 - snowman2));

                    // 0나오면 끝
                    if (ans == 0) {
                        System.out.println(0);
                        return;
                    }

                    if (snowman1 < snowman2) {
                        right--;
                    } else {
                        left++;
                    }

                }
            }
        }

        System.out.println(ans);

    }
}