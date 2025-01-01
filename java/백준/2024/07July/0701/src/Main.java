import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long t = Integer.parseInt(br.readLine());

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arrA = new int[n];
        for (int i = 0; i < n; i++) {
            arrA[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] arrB = new int[m];
        for (int i = 0; i < m; i++) {
            arrB[i] = Integer.parseInt(st.nextToken());
        }

//        System.out.println(Arrays.toString(arrA));
//        System.out.println(Arrays.toString(arrB));

        List<Long> subA = new ArrayList<>();
        List<Long> subB = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            long sumA = arrA[i];
            subA.add(sumA);
            for (int j = i + 1; j < n; j++) {
                sumA += arrA[j];
                subA.add(sumA);
            }
        }

        for (int i = 0; i < m; i++) {
            long sumB = arrB[i];
            subB.add(sumB);
            for (int j = i + 1; j < m; j++) {
                sumB += arrB[j];
                subB.add(sumB);
            }
        }


        Collections.sort(subA);
        Collections.sort(subB);

//        System.out.println(subA);
//        System.out.println(subB);

        int idxA = 0;
        int idxB = subB.size()-1;

        long cnt = 0;

        while (idxA < subA.size() && idxB > -1) {
            long a = subA.get(idxA);
            long b = subB.get(idxB);
            long sum = a + b;

            if (sum == t) {
                long ea = 0;
                while (idxA < subA.size() && a == subA.get(idxA)) {
                    idxA++;
                    ea++;
                }

                long eb = 0;
                while (idxB > -1 && b == subB.get(idxB)) {
                    idxB--;
                    eb++;
                }
                cnt += ea*eb;
            } else if (sum > t) {
                idxB--;
            } else {
                idxA++;
            }


        }
        System.out.println(cnt);

    }
}