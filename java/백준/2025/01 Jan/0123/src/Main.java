import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            String a = s.substring(s.indexOf('.') + 1);
            map.put(a, map.getOrDefault(a, 0) + 1);

        }
        Set<String> set = map.keySet();
        String[] arr = set.toArray(new String[set.size()]);

        Arrays.sort(arr);

        for (String s : arr) {
            System.out.println(s + " " + map.get(s));
        }


    }
}