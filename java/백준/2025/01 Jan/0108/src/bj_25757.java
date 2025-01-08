import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class bj_25757 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        char typeGame = st.nextToken().charAt(0);
        int numPeople;
        if (typeGame == 'Y') {
            numPeople = 2;
        } else if (typeGame == 'F') {
            numPeople = 3;
        } else {
            numPeople = 4;
        }

        HashSet<String> people = new HashSet<>();
        for (int i = 0; i < n; i++) {
            people.add(br.readLine());
        }
//        System.out.println(Arrays.toString(people.toArray()));

        int ans = people.size() / (numPeople-1);
        System.out.println(ans);
    }
}