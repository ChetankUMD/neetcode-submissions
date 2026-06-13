class Solution {
    vector<vector<bool>> visit;
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.empty()) return 0;

        int r = grid.size();
        int c = grid[0].size();
        int result = 0;
        visit = vector<vector<bool>>(r, vector<bool>(c, false));

        for(int i=0; i<r;i++){
            for(int j =0; j<c;j++){
                if(grid[i][j] == '1' && visit[i][j] == false){
                    bfs(i,j, grid);
                    result++;
                }
            }
        }
        return result;
    }

    void bfs(int r, int c, vector<vector<char>>& grid){
        queue<pair<int, int>> q;
        visit[r][c] = true;
        q.push({r,c});

        while(!q.empty()){
            pair<int, int> p = q.front();
            q.pop();
            int row = p.first;
            int col = p.second;
            vector<vector<int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (vector<int> d : dir){
                int i = d[0] + row;
                int j = d[1] + col;
                if(i >= 0 && j>=0 && i<grid.size() && j<grid[0].size() && grid[i][j]=='1' && visit[i][j] == false){
                    q.push({i,j});
                    visit[i][j] =true;
                }
            }
        }
        return;
    }
};
