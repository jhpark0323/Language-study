import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 웰컴키트 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int [] arr = new int[st.countTokens()];
        for (int i=0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        int tShirt = 0;
        for (int i=0; i < arr.length; i++) {
            // 나머지없이 딱 떨어지면
            if (arr[i] % t == 0) {
                tShirt += arr[i] / t;
            }
            // 나머지가 있으면
            else {
                tShirt += arr[i] / t + 1;
            }
        }

        int penBundle = n / p;
        int onePen = n % p;

        System.out.println(tShirt);
        System.out.print(penBundle + " ");
        System.out.println(onePen);

    }
}
