import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] down;
    static int[] up;
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        // 짝수번째 (석순)
        down = new int[n/2];
        // 홀수번째 (종유석)
        up = new int[n/2];

        for(int i=0; i<n/2; i++) {
            int a = Integer.parseInt(br.readLine());
            int b = Integer.parseInt(br.readLine());
            down[i]=a;
            up[i]=b;
        }
        Arrays.sort(up);
        Arrays.sort(down);
//        System.out.println(Arrays.toString(up));

        int min = Integer.MAX_VALUE;
        int cnt = 0;
        for (int i = 1; i <= h; i++) {
            int total = BinarySearch(down, i) + BinarySearch(up, h-i+1);
//            System.out.println(BinarySearch(up, i));
            if (total < min) {
                min = total;
                cnt = 1;
            } else if (total == min) {
                cnt++;
            }
        }

        System.out.println(min + " " + cnt);
    }

    public static int BinarySearch(int[] arr, int val) {
        int left = 0;
        int right = n / 2;

        while (left < right) {
            int mid = (left + right) / 2;

            if (arr[mid] < val) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return n/2-left;
    }
}