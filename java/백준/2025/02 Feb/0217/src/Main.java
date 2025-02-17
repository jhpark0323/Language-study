import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

// bj_1208
public class Main {
    static int n, s;
    static long cnt = 0;
    static ArrayList<Integer> leftList = new ArrayList<>();
    static ArrayList<Integer> rightList = new ArrayList<>();
    static int[] arr;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        sum(0, 0, n/2, leftList);
        sum(0, n/2, n, rightList);

        Collections.sort(leftList);
        Collections.sort(rightList);

        int left = 0;
        int right = rightList.size() - 1;

        while (true) {
            if (left == leftList.size() || right < 0) {
                break;
            }
            int leftValue = leftList.get(left);
            int rightValue = rightList.get(right);

            if (leftValue + rightValue == s) {
                long leftCnt = 0;
                while (left <  leftList.size() && leftList.get(left) == leftValue) {
                    leftCnt++;
                    left++;
                }
                long rightCnt = 0;
                while (0 <= right && rightList.get(right) == rightValue) {
                    rightCnt++;
                    right--;
                }
                cnt += leftCnt * rightCnt;
            }

            else if (leftValue + rightValue > s) {
                right--;
            } else {
                left++;
            }

        }
        if (s == 0) {
            System.out.println(cnt - 1);
        } else {
            System.out.println(cnt);
        }
    }

    // 부분수열의 합
    static void sum(int total, int start, int end, ArrayList<Integer> list) {
        if (start == end) {
            list.add(total);
            return;
        }
        sum(total, start + 1, end, list);
        sum(total + arr[start], start+1, end, list);
    }

}