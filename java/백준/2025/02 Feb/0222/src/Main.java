import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        SimpleDateFormat format = new SimpleDateFormat("HH:mm");
        String S = st.nextToken();
        String E = st.nextToken();
        String Q = st.nextToken();

        Date start = format.parse(S);
        Date end = format.parse(E);
        Date quit = format.parse(Q);

        Set<String> setStart = new HashSet<>();
        Set<String> setEnd = new HashSet<>();

        String line;
        int ans = 0;

        while ((line = br.readLine()) != null) {
            st = new StringTokenizer(line);

            Date time = format.parse(st.nextToken());
            String name = st.nextToken();

            // 시작시간 전에 입장여부
            if (time.before(start) || time.equals(start)) {
                setStart.add(name);
            }

            if ((time.after(end) || time.equals(end)) && (quit.after(time) || quit.equals(time))) {
                if (setStart.contains(name) && !setEnd.contains(name)) {
                    ans++;
                    setEnd.add(name);
                }
            }
        }
        System.out.println(ans);
    }
}