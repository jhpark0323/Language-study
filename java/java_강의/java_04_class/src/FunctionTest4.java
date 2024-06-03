import java.util.Random;

public class FunctionTest4 {
    public static void main(String[] args) {
        System.out.println("아침에 일어난다");
        이동("교육장", "대중교통");
        boolean homework = 교육();
        이동("집", "대중교통");
        if (homework) {
            System.out.println("숙제 해결 하기");
        } else {
            System.out.println("숙제 없음");
        }
        System.out.println("잠");

        System.out.println("아침에 일어난다");
        이동("교육장", "대중교통");
        homework = 교육();
        이동("집", "대중교통");
        if (homework) {
            System.out.println("숙제 해결 하기");
        } else {
            System.out.println("숙제 없음");
        }
        System.out.println("잠");
    }

    static void 이동(String 장소, String 탈것) {
        System.out.println(장소+"(으)로" + 탈것 + "(을)를 이용해 이동");
    }

    static boolean 교육() {
        System.out.println("오전 수업");
        System.out.println("점심");
        System.out.println("오후 수업");

        Random random = new Random();
        return random.nextBoolean();
    }
}
