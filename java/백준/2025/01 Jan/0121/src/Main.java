import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            String w = br.readLine();
            int k = Integer.parseInt(br.readLine());

            func(w, k);
        }
        System.out.println(sb.toString());
    }
    static void func(String w, int k) {
        if (k == 1) {
            sb.append("1 1").append("\n");
            return;
        }

        int[] alpha = new int[26];
        for (int i = 0; i < w.length(); i++) {
            alpha[w.charAt(i) - 'a']++;
        }

        int min = Integer.MAX_VALUE;
        int max = -1;

        for (int i = 0; i < w.length(); i++) {
            if (alpha[w.charAt(i) - 'a'] < k) {
                continue;
            }

            int cnt = 1;

            for (int j = i+1; j < w.length(); j++) {
                if (w.charAt(i) == w.charAt(j)) {
                    cnt++;
                }

                if (cnt == k) {
                    min = Math.min(min, j-i+1);
                    max = Math.max(max, j-i+1);
                    break;
                }

            }
        }

        if (min == Integer.MAX_VALUE || max == -1) {
            sb.append("-1").append("\n");
            return;
        }

        sb.append(min + " " + max).append("\n");

    }
}