class Solution {
    int[] dy = {0, 1, 0, -1};
    int[] dx = {1, 0, -1, 0};
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int y = 0, x = 0;
        int dir = 0;
        int start = 1;
        while(start <= n * n) {
            answer[y][x] = start++;
            int ny = y + dy[dir];
            int nx = x + dx[dir];
            if(ny < 0 || ny >= n || nx < 0 || nx >= n || answer[ny][nx] != 0) {
                dir = (dir + 1) % 4;
                ny = y + dy[dir];
                nx = x + dx[dir];
            }
            y = ny;
            x = nx;
        }
        
        return answer;
    }
}