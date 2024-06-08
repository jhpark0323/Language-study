import java.util.HashSet;
import java.util.Set;

public class SetTest1 {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>();

        set.add("가");
        set.add("나");
        set.add("다");
        set.add("라");
        set.add("마");
        set.add("가");

        System.out.println(set);
        System.out.println(set.size());
    }
}
