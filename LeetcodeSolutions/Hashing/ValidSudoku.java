import java.util.HashSet;
public class ValidSudoku {
    public static void main(String[] args) {
        char[][] board = new char[][] {{3, 3, '.', '.', 7, '.', '.', '.', '.'}, 
                                       {6, '.', '.', 1, 9, 5, '.', '.', '.'},
                                       {'.', 9, 8, '.', '.', '.', '.', 6, '.'},
                                       {8, '.', '.', '.', 6, '.', '.', '.', 3},
                                       {4, '.', '.', 8, '.', 3, '.', '.', 1},
                                       {7, '.', '.', '.', 2, '.', '.','.', 6},
                                       {'.', 6, '.', '.', '.', '.', 2, 8, '.'},
                                       {'.', '.', '.', 4, 1, 9, '.', '.', 5},
                                       {'.', '.', '.', '.', 8, '.', '.', 7, 9}};
        System.out.println(isValidSudoku(board)); 
    }

    public static boolean isValidSudoku(char[][] board) {
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char number = board[i][j];
                if (number != '.') {
                    if (!set.add("Row: " + number + i ) ||
                        !set.add("Col: " + number + j) ||
                        !set.add("Block: " + number + i/3 + j/3)) {
                            return false;
                        }
                }
            }
        }

        return true;
    }
}
