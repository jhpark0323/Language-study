import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        HashSet<String> set = new HashSet<>();
        int idx = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String Ai = st.nextToken();
            String Bi = st.nextToken();
            if (Ai.equals("ChongChong") || Bi.equals("ChongChong")) {
                set.add(Ai);
                set.add(Bi);
                idx = i;
                break;
            }
        }
        int ans = 2;

        for (int i = idx+1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String Ai = st.nextToken();
            String Bi = st.nextToken();
            if (set.contains(Ai) && !set.contains(Bi)) {
                ans++;
                set.add(Bi);
            }
            if (set.contains(Bi) && !set.contains(Ai)) {
                ans++;
                set.add(Ai);
            }
        }

        System.out.println(ans);

    }
}