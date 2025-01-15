import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> map = new HashMap<>();
        String tree;
        int total = 0;
        while ((tree = br.readLine()) != null) {
            map.put(tree, map.getOrDefault(tree, 0) + 1);
            total++;
        }
        List<String> list = new ArrayList<>();
        for (String s : map.keySet()) {
            list.add(s);
        }
        list.sort(Comparator.naturalOrder());

        StringBuilder sb = new StringBuilder();

        for (String s : list) {
            int cnt = map.get(s);
            double per = (double) (cnt * 100) / total;

            sb.append(s + " " + String.format("%.4f", per) + "\n");
        }

        System.out.println(sb);
    }
}