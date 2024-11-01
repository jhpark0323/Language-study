import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] now = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            now[i] = Integer.parseInt(st.nextToken());
        }
        int[] real = new int[n];
        st=  new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            real[i] = Integer.parseInt(st.nextToken());
        }

        int[] status = new int[n];
        for (int i = 0; i < n; i++) {
            status[i] = real[i] - now[i];
        }
//        System.out.println(Arrays.toString(status));

        int ans = Math.abs(status[0]);
        if (n > 1) {
            int last = status[0];
            for (int i = 1; i < n; i++) {
                if (status[i] * last < 0) {
                    ans += Math.abs(status[i]);
                } else if (Math.abs(last) < Math.abs(status[i])) {
                    ans += Math.abs(status[i]) - Math.abs(last);
                }
                last = status[i];
            }
        }
        System.out.println(ans);
    }
}