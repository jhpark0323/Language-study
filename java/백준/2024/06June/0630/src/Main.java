import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/*
 오늘의 꿀팁
 long 타입이어도 별도의 타입 캐스팅이 없으면
 int 타입 3개를 더할때 반환값이 int 타입으로 값이 반환되어 저징되는 이슈가 있네요...
 이래서 문제 풀땐 long 타입 사용시 인풋부터 아웃풋까지 전부 한 타입으로 통일해서 풀으라 하나 봅니다.
*/

public class Main {
    static int n;
    static long arr[];
    static int ans[] = new int[3];
    static long total = Long.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new long[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
//        System.out.println(Arrays.toString(arr));

        // 시작점을 기준으로 돌아감
        // -> arr[n-3]까지 해야 다음 두개가 각각 n-2, n-1로 딱맞음
        for (int i = 0; i < n - 2; i++) {
            twoPointer(i);
        }
        System.out.println(arr[ans[0]] + " " + arr[ans[1]] + " " + arr[ans[2]]);
        br.close();
    }

    public static void twoPointer(int start) {
        int left = start+1;
        int right = n-1;
        while (left < right) {
            long sum = Math.abs(arr[start] + arr[left] + arr[right]);

            if (sum == 0) {
                ans[0] = start;
                ans[1] = left;
                ans[2] = right;
            }

            if (total > sum) {
                ans[0] = start;
                ans[1] = left;
                ans[2] = right;
                total = sum;
            }

            if (arr[start] + arr[left] + arr[right] > 0) {
                right--;
            } else {
                left++;
            }

        }
    }
}