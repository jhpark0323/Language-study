import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[][] animals;
    static int[] shoot;
    static int m;
    static int n;
    static int l;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        shoot = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(shoot);
//        for (int s : shoot) {
//            System.out.print(s + " ");
//        }

        animals = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            animals[i][0] = Integer.parseInt(st.nextToken());
            animals[i][1] = Integer.parseInt(st.nextToken());
        }

//        System.out.println(Arrays.deepToString(animals));

        // animals를 순회하며 잡을수있는지 판단
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int left = 0;
            int right = m-1;
            int[] target = animals[i];

            while (left <= right) {
                int mid = (left + right) / 2;

                if (Math.abs(shoot[mid] - target[0]) + target[1] <= l) {
                    cnt++;
                    break;
                }

                if (target[0] > shoot[mid]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }

            }

        }
        System.out.println(cnt);


    }
}