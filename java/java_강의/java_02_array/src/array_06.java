import java.util.Arrays;

public class array_06 {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int N = 5;
        int M = 9;

        int sum = 0;
        for (int i = N; i <= M; i++) {
            sum += arr[i];
        }

        System.out.println("sum :" + sum);

        int A = 0;
        int B = 0;
        for (int i=0; i<=M; i++) {
            A += arr[i];
        }
        for (int i=0; i<=N-1; i++) {
            B += arr[i];
        }
        System.out.println(A-B);

        int[] prefixSum = new int[arr.length];
        prefixSum[0] = arr[0];
        for (int i=1; i < arr.length;  i++) {
            prefixSum[i] = prefixSum[i-1] + arr[i];
        }
        System.out.println(Arrays.toString(prefixSum));

        System.out.println(prefixSum[M] - prefixSum[N-1]);

    }
}
