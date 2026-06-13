class Solution {
    int largest = 0;
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if(grid.empty()) return 0;

        int r = grid.size();
        int c = grid[0].size();
        for(int i=0; i<r;i++){
            for(int j =0; j<c;j++){
                if(grid[i][j] == 1){
                    int res = bfs(i,j, grid, 0);
                    if(res > largest){
                        largest = res;
                    }
                }
            }
        }
        return largest;
    }

    int bfs(int r, int c, vector<vector<int>>& grid, int temp){
        queue<pair<int, int>> q;
        grid[r][c] = 0;
        temp++;
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
                if(i >= 0 && j>=0 && i<grid.size() && j<grid[0].size() && grid[i][j]==1){
                    q.push({i,j});
                    temp++;
                    grid[i][j] = 0;
                }
            }
        }
        return temp;
    }
};
