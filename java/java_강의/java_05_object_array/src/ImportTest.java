import java.util.*;
import java.util.logging.Logger;

public class ImportTest {
    static String str = "문장";
    String strr = "문장1";
    public static void main(String[] args) {

        System.out.println(str);
//        System.out.println(strr);

        Scanner sc = new Scanner(System.in);
        Date d = new Date();

        int[] arr = new int[] {1, 2, 3, 4};
        Arrays.toString(arr);

        // 자바에서 하위 패키지는 다른 패키지이다.
        // 하위 패키지라는 개념이 없다.
        // * -> 그 패키지 안의 모든 클래스
        // import 할 때 * 사용시 그 하위? 패키지는 import 안됨
        Logger l;

    }
}