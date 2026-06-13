class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        

        for (int i = 0; i< 9; i++){
            unordered_map<char, int> row;
            unordered_map<char, int> col;
            unordered_map<char, int> box;
            for (int j=0; j< 9; j++){
                
                if (board[i][j] != '.'){
                    if (++row[board[i][j]] > 1){
                        return false;
                    }
                }
                if (board[j][i] != '.'){
                    if (++col[board[j][i]] > 1){
                        return false;
                    }
                }

                int boxRow = 3 * (i / 3) + j / 3;
                int boxCol = 3 * (i % 3) + j % 3;
                if (board[boxRow][boxCol] != '.') {
                    if (++box[board[boxRow][boxCol]] > 1){
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
