package java_05_loop;

public class loop_for {
    public static void main(String[] args) {
//        for (int i = 0; i < 10; i++) {
//            System.out.println(i);
//        }
//        for (int i = 0, j = 30; i < 10 && j >= 20; i += 10, j += 2) {
//            System.out.println(i + " " + j);
//        }

        // 중첩 반복문
        for (int i = 2; i <= 9; i++) {
            System.out.println(i + "단");
            for (int j = 1; j <= 9; j++) {
                System.out.printf("%d + %d = %d\n", i, j, i * j);
            }
        }
    }
}
