import java.util.Arrays;

public class array_08 {
    public static void main(String[] args) {
        // 홀수개
        int[] arr = {1, 2, 3, 4, 6, 3, 2, 4, 3, 1, 3, 4, 5, 6, 7, 8, 9};
        System.out.println(arr.length);

        int[] count = new int[10];
        for (int i=0; i<arr.length; i++) {
            count[arr[i]] += 1;
        }

        System.out.println(Arrays.toString(count));

        // 개수의 합
        int sum = 0;
        int median = 0;
        for (int i=0; i<=9; i++) {
            sum += count[i];
            System.out.println("현재("+i+"까지 개수의 합:"+sum);
            if (sum >= arr.length/2 + 1) {
                median = i;
                break;
            }
        }

        System.out.println(median);

    }
}
