import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Integer[] arr = new Integer[n];
        int negative = 0;
        int zero = 0;
        int positive = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            if (arr[i] < 0) {
                negative++;
            } else if (arr[i] == 0) {
                zero++;
            } else {
                positive++;
            }
        }

        Arrays.sort(arr, Collections.reverseOrder());
//        System.out.println(Arrays.toString(arr));

//        System.out.println("positive = " + positive);
//        System.out.println("negative = " + negative);
//        System.out.println("zero = " + zero);

        int ans = 0;
        // 양수 계산 중
        for (int i=0; i<positive-1; i+=2) {
            // 둘 중 하나가 1이면 그냥 곱하지말고 더하는게 나음
            if (arr[i] == 1 || arr[i+1] == 1) {
                ans += arr[i] + arr[i+1];
                continue;
            }
            ans += arr[i] * arr[i+1];
        }

        // 양수의 갯수가 홀수개이면 마지막 양수는 그냥 더해줌
        if ((positive % 2) != 0) {
            ans += arr[positive - 1];
        }

        // 0이 있을 때
        if (zero > 0) {
            // 음수의 갯수가 홀수개면 0이랑 곱해서 절댓값이 제일 작은 음수 하나 없앰
            if (negative % 2 != 0) {
                // 음수 다시 ans에 더하기
                // 두번째 음수 부터 시작
                for (int i = positive + zero + 1; i < n; i += 2) {
                    ans += arr[i] * arr[i + 1];
                }
            }
            // 음수의 갯수가 짝수개 이면 걍 곱함
            else {
                for (int i = positive + zero; i < n; i += 2) {
                    ans += arr[i] * arr[i + 1];
                }
            }
        }
        // 0이 없을 때
        else {
            // 음수의 갯수가 홀수개면 첫번째 음수 제외하고 나머지끼리 곱함
            if (negative % 2 != 0) {
                for (int i = positive + zero + 1; i < n; i += 2) {
                    ans += arr[i] * arr[i + 1];
                }
                ans += arr[positive + zero];
            }
            // 음수의 갯수가 짝수면 그냥 곱해서 더함
            else {
                for (int i = positive + zero; i < n; i += 2) {
                    ans += arr[i] * arr[i + 1];
                }
            }
        }

        System.out.println(ans);


    }
}