import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int k;
    static char[] arr;
    static boolean[] visited = new boolean[10];
    static ArrayList<String> result = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new char[k];
        for (int i = 0; i < k; i++) {
            arr[i] = st.nextToken().charAt(0);
        }

        for (int i = 0; i < 10; i++) {
            visited[i] = true;
            back(i, 0, i+"");
            visited[i] = false;
        }
        System.out.println(result.get(result.size()-1));
        System.out.println(result.get(0));

    }

    static void back(int now, int cnt, String number) {
        if (cnt == k) {
            result.add(number);
            return;
        }

        for (int next = 0; next < 10; next++) {
            if (!visited[next]) {
                if ((arr[cnt] == '<' && now < next) || (arr[cnt] == '>' && now > next)) {
                    visited[next] = true;
                    back(next, cnt + 1, number+next);
                    visited[next] = false;
                }
            }
        }

    }
}