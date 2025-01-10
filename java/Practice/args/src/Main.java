public class Main {
    public static void main(String[] args) {
        System.out.println(args.length);
        System.out.println();

        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
        System.out.println();

        for (String arg : args) {
            System.out.println(arg);
        }
    }
}