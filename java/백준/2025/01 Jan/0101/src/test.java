public class test {
    public static void main(String[] args) {
        // break문 label 쓰는법
        out:
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 5) {
                    System.out.println(i + " " + j);
                    break out;
                }
            }
        }
        pos1:
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (j == 3) {
                    continue pos1;
                }
                System.out.println(i + ", " + j);
            }
        }
    }
}