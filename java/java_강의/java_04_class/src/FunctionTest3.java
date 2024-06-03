public class FunctionTest3 {
    public static void main(String[] args) {
        System.out.println("아침에 일어난다");
        이동("교육장", "대중교통");
        교육();
        이동("집", "대중교통");
        System.out.println("과제");
        System.out.println("잠");

        System.out.println("아침에 일어난다");
        이동("교육장", "대중교통");
        교육();
        이동("집", "대중교통");
        System.out.println("과제");
        System.out.println("잠");
    }

    static void 이동(String 장소, String 탈것) {
        System.out.println(장소+"(으)로" + 탈것 + "(을)를 이용해 이동");
    }

    static void 교육() {
        System.out.println("오전 수업");
        System.out.println("점심");
        System.out.println("오후 수업");
    }

}
