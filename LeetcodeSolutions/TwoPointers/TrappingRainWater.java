public class TrappingRainWater {
    public static void main(String[] args) {
        int[] height = new int[] {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        System.out.println(trap(height));
    }

    public static int trap(int[] height) {
        //General Approach: Notice how rainwater can only be trapped if there exists a block of greater height, both on the left and the right side 
        //of the current block. Thus, the amount of water a block can hold is equal to the minimum of the max height on both the left and right
        //half minus the height of the current block

        if (height.length == 0) return 0;
        int left = 0;
        int right = height.length - 1;
        int leftMax = height[left];
        int rightMax = height[right];
        int trappedWater = 0;

        while (left < right) {
            if (leftMax < rightMax) {
                left++;
                leftMax = Math.max(leftMax, height[left]);
                trappedWater += leftMax - height[left];
            } else {
                right--;
                rightMax = Math.max(rightMax, height[right]);
                trappedWater += rightMax - height[right];
            }
        }

        return trappedWater;


    }
}
