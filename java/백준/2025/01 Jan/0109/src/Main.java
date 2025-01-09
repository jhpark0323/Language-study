import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        int[] answer = new int[T];

        for (int testcase = 0; testcase < T; testcase++) {
            int n = Integer.parseInt(br.readLine());
            int[] arr = new int[n];
            Map<Integer, Integer> cntMap = new HashMap<>();
            int teamNum = Integer.MIN_VALUE;

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                int x = Integer.parseInt(st.nextToken());
                cntMap.put(x, cntMap.getOrDefault(x, 0) + 1);
                arr[i] = x;
                teamNum = Math.max(teamNum, x);
            }

            int[] fifth = new int[teamNum + 1];
            Map<Integer, Integer> scoreMap = new HashMap<>();
            Map<Integer, Integer> tmpMap = new HashMap<>();
            int score = 1;

            for (int rank : arr) {
                if (cntMap.get(rank) == 6) {
                    tmpMap.put(rank, tmpMap.getOrDefault(rank, 0) + 1);

                    if (tmpMap.get(rank) <= 4) {
                        scoreMap.put(rank, scoreMap.getOrDefault(rank, 0) + score);
                    }

                    if (tmpMap.get(rank) == 5) {
                        fifth[rank] = score;
                    }
                    score++;
                }
            }

            int result = Integer.MAX_VALUE;
            int fifthScore = Integer.MAX_VALUE;

            for (Integer key : scoreMap.keySet()) {
                int tmp = scoreMap.get(key);

                if (tmp < result) {
                    result = tmp;
                    fifthScore = fifth[key];
                    answer[testcase] = key;
                }
                else if (tmp == result) {
                    if (fifthScore > fifth[key]) {
                        answer[testcase] = key;
                    }
                }
            }
        }
        for (int i : answer) {
            System.out.println(i);
        }
    }
}