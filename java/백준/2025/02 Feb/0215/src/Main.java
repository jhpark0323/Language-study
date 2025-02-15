import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long n, a, b, c, d;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Long.parseLong(st.nextToken());
        a = Long.parseLong(st.nextToken());
        b = Long.parseLong(st.nextToken());
        c = Long.parseLong(st.nextToken());
        d = Long.parseLong(st.nextToken());

        // 효율적인거 하나로 통일
        // d / c > b / a
        if (a * d > b * c) {
            long x = a;
            a = c;
            c = x;
            x = b;
            b = d;
            d = x;
        }

        long ans = Long.MAX_VALUE;

        for (int i = 0; i < c; i++) {
            long idx = (long) Math.ceil((double) (n - i * a) / c);

            if (idx < 0) {
                idx = 0;
            }
            ans = Math.min(ans, i * b + idx * d);
            if (idx == 0) {
                break;
            }
        }
        System.out.println(ans);

    }
}