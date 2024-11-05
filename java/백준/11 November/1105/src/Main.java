import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int testcase = 0; testcase < t; testcase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            int[] arr = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            ArrayList<ArrayList<Integer>> list = new ArrayList<>();
            for (int i = 0; i < n+1; i++) {
                ArrayList<Integer> list1 = new ArrayList<>();
                list.add(list1);
            }

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                list.get(end).add(start);
            }

            int w = Integer.parseInt(br.readLine());

            System.out.println(list);

        }
    }
}