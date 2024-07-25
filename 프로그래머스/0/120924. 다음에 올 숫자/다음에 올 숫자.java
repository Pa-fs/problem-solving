class Solution {
    public int solution(int[] common) {
        int answer = Integer.MAX_VALUE;
        boolean isSame = false;
        int prev = 0;
        for(int i = 1; i < common.length; i++) {
            answer = common[i] - common[i - 1];
            if(prev == answer) {
                isSame = true;
                break;
            }
            prev = answer;
        }

        if(isSame) {
            return answer + common[common.length - 1];   
        } else {
            return (common[1] / common[0]) * common[common.length - 1];
        }
    }
}