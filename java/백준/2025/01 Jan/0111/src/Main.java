import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<String, String> map = new HashMap<>();
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            map.put(st.nextToken(), st.nextToken());
        }
        List<String> list = new ArrayList<>();
        for (String key : map.keySet()) {
            if (map.get(key).equals("enter")) {
                list.add(key);
            }
        }
        list.sort(Comparator.reverseOrder());
        for (String key : list) {
            System.out.println(key);
        }
    }
}