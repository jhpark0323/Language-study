import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[] start1 = new int[n];
        int[] start2 = new int[n];

        int[] end = new int[n];

        String startString = br.readLine();
        for (int i = 0; i < n; i++) {
            int s = startString.charAt(i) - '0';
            start1[i] = s;
            start2[i] = s;
        }
        String endString = br.readLine();
        for (int i = 0; i < n; i++) {
            end[i] = endString.charAt(i) - '0';
        }

        // 첫번째 스위치를 눌렀을 때
        start1[0] = 1-start1[0];
        start1[1] = 1-start1[1];
        int ans1 = solve(start1, end);
        if (ans1 != Integer.MAX_VALUE) {
            ans1++;
        }

        // 첫번째 스위치를 안 눌렀을 때
        int ans2 = solve(start2, end);

        if (ans1 == Integer.MAX_VALUE && ans2 == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(Math.min(ans1, ans2));
        }

    }

    static int solve(int[] start, int[] end) {
        int ans = 0;
        for (int i = 1; i < n; i++) {
            // 같으면 넘어감
            if (start[i-1] == end[i-1]) {
                continue;
            }
            // 다르면
            else {
                start[i-1] = 1-start[i-1];
                start[i] = 1-start[i];
                if (i != n - 1) {
                    start[i+1] = 1-start[i+1];
                }
                ans++;
            }
        }
        if (start[n-1] != end[n-1]) {
            ans = Integer.MAX_VALUE;
        }
        return ans;
    }

}