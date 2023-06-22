public class SearchRotatedSortedArray {
    public static void main(String[] args) {
        int[] nums = new int[] {4,5,6,7,0,1,2};
        System.out.println(search(nums, 0));
    }

    public static int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left + 1) / 2;
            
            if (nums[mid] == target) return mid;
            //Left sorted
            else if (nums[left] <= nums[mid]) { 
                if (target > nums[mid] || target < nums[left]) left = mid + 1;
                else right = mid - 1;
            } 
            //Right sorted
            else {
                if (target < nums[mid] || target > nums[right]) right = mid - 1;
                else left = mid + 1;
            }
        }

        return -1;
    }
}
