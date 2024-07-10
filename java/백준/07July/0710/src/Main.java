import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer> arr;
    static int n;
    static int max;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        String[] tokens = br.readLine().split(" ");
        arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(tokens[i]));
        }
        Collections.sort(arr);
        // 처음과 끝도 추가
        arr.add(0, 0);
        arr.add(l);
        System.out.println(arr);

        max = 0;
        for (int i = 1; i < n+2; i++) {
            int len = arr.get(i) - arr.get(i-1);
            if (len > max) {
                max = len;
            }
        }

        int left = 0;
        int right = l;

        while (left <= right) {
            int mid = (left + right) / 2;
            Measure(mid);
            
        }

    }

    public static void Measure(int restArea) {
        for (int i = 1; i < n+2; i++) {
            // 처음으로 arr[i]가 restArea보다 커질 때
            if (arr.get(i) > restArea) {
                int len = Math.max(restArea-arr.get(i-1), arr.get(i) - restArea);
                max = Math.max(max, len);
                break;
            }
        }
    }
}