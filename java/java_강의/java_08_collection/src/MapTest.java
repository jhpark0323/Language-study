import java.util.HashMap;
import java.util.Map;

public class MapTest {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();

        map.put("1", "가");
        map.put("2", "나");
        map.put("3", "다");
        map.put("4", "라");
        map.put("5", "마");
        map.put("6", "가");

        System.out.println(map);

        System.out.println(map.get("1"));

        map.put("2", "바");
        System.out.println(map);

        System.out.println(map.containsKey("3"));
        System.out.println(map.containsValue("다"));
        System.out.println(map.containsKey("7"));

        for (String key: map.keySet()) {
            System.out.printf("%s : %s \n", key, map.get(key));
        }

        for (Map.Entry<String, String> entry : map.entrySet()) {
            System.out.println(entry.getKey()+" : "+entry.getValue());
        }

    }
}
