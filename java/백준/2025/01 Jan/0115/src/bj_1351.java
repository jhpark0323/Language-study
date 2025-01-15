import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class bj_1351 {
    static Map<Long, Long> map = new HashMap<>();
    static long p, q;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long n = Long.parseLong(st.nextToken());
        p = Long.parseLong(st.nextToken());
        q = Long.parseLong(st.nextToken());

        System.out.println(func(n));
    }

    static long func(long num) {
        if (num == 0) {
            return 1;
        }

        if (map.containsKey(num)) {
            return map.get(num);
        }

        long ans = func(num / p) + func(num / q);
        map.put(num, ans);
        return ans;
    }
}
