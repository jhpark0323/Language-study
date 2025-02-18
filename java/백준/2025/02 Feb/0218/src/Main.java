import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int nA = Integer.parseInt(st.nextToken());
        int nB = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        HashSet<Integer> setA = new HashSet<>();
        for (int i = 0; i < nA; i++) {
            setA.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        HashSet<Integer> setB = new HashSet<>();
        for (int i = 0; i < nB; i++) {
            setB.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> list = new ArrayList<>();

        for (int i : setA) {
            if (!setB.contains(i)) {
                list.add(i);
            }
        }

        Collections.sort(list);

        System.out.println(list.size());
        if (list.size() != 0) {
            for (int i : list) {
                System.out.print(i + " ");
            }
        }
    }
}