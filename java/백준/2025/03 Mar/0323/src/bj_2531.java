import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class bj_2531 {
    static int n, d, k, c;
    static int[] sushiTable;
    static int[] sushi;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        sushiTable = new int[n];
        for (int i = 0; i < n; i++) {
            sushiTable[i] = Integer.parseInt(br.readLine());
        }
        sushi = new int[d+1];
        System.out.println(check());
    }

    static int check() {
        int cnt = 0;
        for (int i = 0; i < k; i++) {
            int a = sushiTable[i];

            if (sushi[a] == 0) {
                cnt++;
            }
            sushi[a]++;
        }
        int max = cnt;

        for (int i = 0; i < n; i++) {
            if (cnt >= max) {
                if (sushi[c] == 0) {
                    max = cnt + 1;
                } else {
                    max = cnt;
                }
            }
            sushi[sushiTable[i]]--;
            if (sushi[sushiTable[i]] == 0) {
                cnt--;
            }

            if (sushi[sushiTable[(i + k) % n]] == 0) {
                cnt++;
            }
            sushi[sushiTable[(i + k) % n]]++;
        }
        return max;
    }
}