class Solution {
    public int[] solution(String myString) {
        int[] answer = {};
        int xCnt = 0;
        for(int i = 0; i < myString.length(); i++) {
            char ch = myString.charAt(i);
            if(ch == 'x') {
                xCnt++;
            }
        }
        
        answer = new int[xCnt + 1];
        
        int cnt = 0;
        int idx = 0;
        for(int i = 0; i < myString.length(); i++) {
            char ch = myString.charAt(i);
            if(ch == 'x') {
                answer[idx++] = cnt;
                cnt = 0;
            } else {
                cnt++;
            }
        }
        
        answer[answer.length - 1] = cnt;
        return answer;
    }
}