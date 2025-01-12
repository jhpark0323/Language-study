import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int na = Integer.parseInt(st.nextToken());
        int nb = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        HashSet<Integer> setA = new HashSet<>();
        for (int i = 0; i < na; i++) {
            setA.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> list = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < nb; i++) {
            int a = Integer.parseInt(st.nextToken());
            if (setA.contains(a)) {
                list.add(a);
            }
        }
        System.out.println(na + nb - 2*list.size());
    }
}