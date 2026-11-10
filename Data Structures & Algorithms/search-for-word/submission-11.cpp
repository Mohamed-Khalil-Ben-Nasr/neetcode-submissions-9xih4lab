class Solution {
private:
    vector<vector<char>> board;
    string word;
    set<pair<int, int>> visited;
    vector<pair<int, int>> dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};

    bool backtrack(int row, int col, int i) {
        if (i == word.size()-1 && board[row][col] == word[i]) {
            return true;
        }

        if (board[row][col] != word[i]) {
            return false;
        }

        for(auto& [dr, dc] : dirs) {
            int r = row + dr;
            int c = col + dc;
            if (r < 0 or r >= board.size() or c < 0 or c >= board[0].size()
            or visited.find(pair{r, c}) != visited.end() or board[r][c] != word[i+1]) {
                continue;
            }
            visited.insert(pair{r, c});
            if ( backtrack(r, c, i+1)) {
                return true;
            }
            visited.erase(pair{r,c});
        }

        return false;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        this->board = board;
        this->word = word;
        int rows = board.size();
        int cols = board[0].size();

        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (board[r][c] == word[0]) {
                    visited.insert(pair{r, c});
                    if (backtrack(r, c, 0)){
                        return true;
                    }
                    visited.erase(pair{r,c});
                }
            }
        }
        return false;
    }
};
