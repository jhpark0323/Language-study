import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        BigInteger[] arr = new BigInteger[10001];
        arr[0] = BigInteger.ZERO;
        arr[1] = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            arr[i] = arr[i-1].add(arr[i-2]);
        }
        System.out.println(arr[n]);
    }
}