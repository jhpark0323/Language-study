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


    }

    public static int CanShoot(int shooter) {
        int ans = 0;
        for (int[] animal : animals) {
            int x = animal[0];
            int y = animal[1];

            int count = Math.abs(x - shooter) + y;

            if (count <= l) {
                ans++;
            }
        }
        return ans;
    }

    public static void BinarySearch() {
        int canShoot = 0;
        int left = 0;
        int right = m-1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (CanShoot(shoot[mid]) >= canShoot) {

            }


        }

    }
}