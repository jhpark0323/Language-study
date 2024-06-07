import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SortTest {
    public static void main(String[] args) {
        List<String> names = new ArrayList<String>();

        names.add("EEE");
        names.add("AAA");
        names.add("CCC");
        names.add("BBB");
        names.add("DDD");

        System.out.println(names);

        Collections.sort(names);

        System.out.println(names);

    }
}
