import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] arr = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = arr[i-1] + Integer.parseInt(st.nextToken());
        }

//        System.out.println(Arrays.toString(arr));
        Map<Integer, Integer> map = new HashMap<>();

        long ans = 0;
        for (int i = 1; i <= n; i++) {
            if (arr[i] == k) {
                ans++;
            }
            ans += map.getOrDefault(arr[i] - k, 0);
            map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
        }
        System.out.println(ans);
    }
}