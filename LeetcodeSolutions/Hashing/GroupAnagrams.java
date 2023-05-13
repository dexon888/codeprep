import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;
public class GroupAnagrams {
    public static void main(String[] args) {
        String[] strs = new String[] {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(groupAnagrams(strs).toString());
    }

    public static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        if (strs.length == 0) return result;

        HashMap<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            int[] hash = new int[26];
            for (char c: s.toCharArray()) {
                hash[c - 'a']++;
            }
            String key = Arrays.toString(hash);
            map.computeIfAbsent(key, k -> new ArrayList<String>());
            map.get(key).add(s);
        }
        result.addAll(map.values());
        return result;
    }


}