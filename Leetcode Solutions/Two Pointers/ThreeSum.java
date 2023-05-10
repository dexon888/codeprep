import java.util.ArrayList;
import java.util.Arrays;
public class ThreeSum {
    public static void main(String[] args) {
        int[] nums = new int[] {-1, 0, 1, 2, -1, -4};
        ArrayList<ArrayList<Integer>> result = threeSum(nums);
        System.out.println(result.toString());
    }

    public static ArrayList<ArrayList<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                int left = i + 1;
                int right = nums.length - 1;
                int complement = 0 - nums[i];

                while (left < right) {
                    if (nums[left] + nums[right] == complement) {
                        ArrayList<Integer> list = new ArrayList<>();
                        list.add(nums[left]);
                        list.add(nums[i]);
                        list.add(nums[right]);
                        result.add(list);
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (nums[left] + nums[right] > complement) {
                        right--;
                    } else {
                        left++;
                    }
                }
            }
        }
        return result;
    }
}