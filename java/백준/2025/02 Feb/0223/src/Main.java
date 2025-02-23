import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < 2*n-1; i++) {
            String s = br.readLine();
            map.put(s, map.getOrDefault(s, 0)+1);
        }
        for (String s : map.keySet()) {
            if (map.get(s) % 2 != 0) {
                System.out.println(s);
                break;
            }
        }
    }
}