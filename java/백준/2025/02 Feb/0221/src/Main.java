import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedHashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        LinkedHashSet<String> set = new LinkedHashSet<>();
        for (int i = 0; i < l; i++) {
            String s = br.readLine();
            if (set.contains(s)) {
                set.remove(s);
            }
            set.add(s);
        }

//        for (int i = 0; i < k; i++) {
//            System.out.println(set.iterator().next());
//        }

        for (String s : set) {
            if (k <= 0) {
                break;
            }
            System.out.println(s);
            k--;
        }

    }
}