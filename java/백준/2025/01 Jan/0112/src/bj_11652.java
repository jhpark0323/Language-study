import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

public class bj_11652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<Long, Integer> map = new HashMap<>();
        int max = 0;
        for (int i = 0; i < n; i++) {
            long a = Long.parseLong(br.readLine());
            map.put(a, map.getOrDefault(a, 0) + 1);
            max = Math.max(max, map.get(a));
        }

        List list = new ArrayList<>();
        for (Long key : map.keySet()) {
            if (map.get(key) == max) {
                list.add(key);
            }
        }

        list.sort(Comparator.naturalOrder());
        System.out.println(list.get(0));

    }
}
