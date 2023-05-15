import java.util.Arrays;
public class ProductOfArrayExceptSelf {
    public static void main(String[] args) {
        int[] nums = new int[] {1,2,3,4};
        System.out.println(Arrays.toString(productExceptSelf(nums)));
    }

    public static int[] productExceptSelf(int[] nums) {
        // Example: [1,2,3,4]
        int[] result = new int[nums.length];

        int pre = 1;
        int post = 1;

        //Find prefix products
        //Prefix Example: 
        //[1, 1, 2, 6]
        for (int i = 0; i < nums.length; i++) {
            result[i] = pre;
            pre *= nums[i];
        }

        //Find postfix products
        //Postfix Example:
        //[24,12,8,6]
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] *= post;
            post *= nums[i];
        }

        return result;
    }
}