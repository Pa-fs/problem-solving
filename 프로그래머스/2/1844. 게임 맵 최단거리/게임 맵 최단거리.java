import java.util.*;

class Solution {
    int m,n;
    int[][] dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    public int solution(int[][] maps) {
        int answer = -1;
        m = maps.length;
        n = maps[0].length;
        
        int[][] visited = new int[m][n];
        Queue<int[]> q = new LinkedList<>();
        visited[0][0] = 1;
        q.offer(new int[]{0, 0});

        while(!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0];
            int y = curr[1];
            for(int[] dir : dirs) {
                int x1 = x + dir[0];
                int y1 = y + dir[1];
                if(x1 >= 0 && y1 >= 0 && x1 < m && y1 < n) {
                    if(maps[x1][y1] == 1 && visited[x1][y1] == 0) {
                        q.offer(new int[] {x1, y1, visited[x1][y1] = visited[x][y] + 1});   
                    }
                }
            }
        }
        if(visited[m-1][n-1] != 0)
            return visited[m-1][n-1];
            
        return answer;
    }
}