package operator;

public class Comp2 {
    public static void main(String[] args) {
        String str1 = "문자열1";
        String str2 = "문자열2";
        String str3 = "문자열1";

        boolean result1 = str1.equals(str2);
        System.out.println(result1);

        boolean result2 = str1.equals(str3);
        System.out.println(result2);

        boolean result3 = str1 == str3;
        System.out.println(result3);


    }
}
