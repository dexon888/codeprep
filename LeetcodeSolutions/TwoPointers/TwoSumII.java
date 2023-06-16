import java.util.Arrays;
public class TwoSumII {
    public static void main(String[] args) {
        int[] numbers = new int[] {2, 7, 11, 15};
        System.out.println(Arrays.toString(twoSum(numbers, 9)));
    }

    public static int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            if (numbers[left] + numbers[right] == target) {
                return new int[] {left + 1, right + 1};
            } else if (numbers[left] + numbers[right] < target) {
                left++;
            } else {
                right--;
            }
        }

        return new int[] {left + 1, right + 1};
    }
}
