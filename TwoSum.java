import java.util.Map;
import java.util.HashMap;
public class TwoSum {
    public static void main(String[] args) {
        int[] test = new int[] {3, 2, 4};
        int target = 6;
        int[] result = twoSum(test, target);

        System.out.println(result[0] + " " + result[1]);
    }

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[] {-1, -1};
    }
}