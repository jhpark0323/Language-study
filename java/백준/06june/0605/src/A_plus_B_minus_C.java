import java.util.Scanner;

public class A_plus_B_minus_C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.println(a+b-c);

        String strA = Integer.toString(a);
        String strB = Integer.toString(b);

        String d =strA + strB;

        System.out.println(Integer.parseInt(d) - c);

        sc.close();
    }
}