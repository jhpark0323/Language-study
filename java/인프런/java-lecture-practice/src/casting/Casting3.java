package casting;

public class Casting3 {
    public static void main(String[] args) {
        int div1 = 3 / 2;
        System.out.println("div1 = " + div1);
        // 1
        
        double div2 = 3 / 2;
        System.out.println("div2 = " + div2);
        // 1.0
        
        double div3 = 3.0 / 2;
        System.out.println("div3 = " + div3);
        // 1.5
        
        double div4 = (double) 3 / 2;
        System.out.println("div4 = " + div4);
        // 1.5

        double div5 = (double) 3 / 2;
        System.out.println("div5 = " + div5);
        // 1.5

        int a = 3;
        int b = 2;
        double result = (double) a / b;
        System.out.println("result = " + result);
    }
}
