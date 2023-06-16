public class ContainerWithMostWater {
    public static void main(String[] args) {
        int[] heights = new int[] {1,8,6,2,5,4,8,3,7};
        System.out.println(maxArea(heights));
    }

    public static int maxArea(int[] height) {
        int left = 0; 
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int currArea = (right - left) * Math.min(height[left], height[right]);
            maxArea = Math.max(maxArea, currArea);
            if (height[left] < height[right]) {
                left++;
                continue;
            }
            right--;
        }

        return maxArea;
    }
}
