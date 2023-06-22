public class Search2DMatrix {
    public static void main(String[] args) {
        int[][] matrix = new int[][] {{1,3,5,7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
        System.out.println(searchMatrix2(matrix, 3));
    }

    public static boolean searchMatrix2(int[][] matrix, int target) {
        if (matrix.length == 0) return false;

        int rows = matrix.length;
        int cols = matrix[0].length;

        int low = 0;
        int high = rows * cols;

        while (low < high) {
            int mid = (low + high) / 2;
            if (matrix[mid/cols][mid%cols] == target) {
                return true;
            } else if (matrix[mid/cols][mid%cols] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return false;
    }
}
