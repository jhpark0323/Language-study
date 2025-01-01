import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException {
        // 가장 긴 증가하는 부분 수열2_12015
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
//        System.out.println(Arrays.toString(arr));

        int[] newArr = new int[n];
        newArr[0] = arr[0];

        int idx = 0;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            // 들어오는 값이 더 크면 추가
            if (key > newArr[idx]) {
                idx++;
                newArr[idx] = key;
            } else {
                // 들어오는 값이 기존 마지막값보다 작으면 안에 있는것중 본인보다 큰것중 제일 작은걸 들어오는값으로 대체
                int left = 0;
                int right = idx;

                while (left < right) {
                    int mid = (left + right) / 2;

                    // 안에서 같은 값 찾으면 종료
//                    System.out.println(Arrays.toString(newArr));
//                    System.out.println("left  : " + left + ", right : " + right + " mid : " + mid);
//                    System.out.println(idx);
                    if (key == newArr[mid]) {
                        left = mid;
                        break;
                    } else if (key < newArr[mid]) {
                        right = mid;
                    } else {
                        left = mid+1;
                    }
                }
                newArr[left] = key;
            }
//            System.out.println(Arrays.toString(newArr));

        }
        System.out.println(idx+1);
    }
}