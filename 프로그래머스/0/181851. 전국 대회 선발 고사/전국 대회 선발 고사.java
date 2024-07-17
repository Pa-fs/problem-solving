class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        for(int i = 0; i < attendance.length; i++) 
            if(!attendance[i]) rank[i] = Integer.MAX_VALUE;
        

        int rankIdx = 0;
        int[] confirmedRank = new int[3];
        for(int i = 0; i < rank.length; i++) {
            if(rankIdx >= 3) break;
            int min = Integer.MAX_VALUE;
            int minIdx = 0;
            for(int j = 0; j < rank.length; j++) {
                if(min > rank[j]) {
                    min = rank[j];
                    minIdx = j;
                }
            }
            confirmedRank[rankIdx++] = minIdx;
            rank[minIdx] = Integer.MAX_VALUE;
        }
        return 10000 * confirmedRank[0] + 100 * confirmedRank[1] + confirmedRank[2];
    }
}