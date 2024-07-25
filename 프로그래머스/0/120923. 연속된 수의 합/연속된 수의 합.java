class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        int number = total / num;
        int tmp = number;
        for(int i = (answer.length - 1) / 2; i >= 0; i--) {
            answer[i] = tmp--;
        }
        for(int i = (answer.length - 1) / 2; i < answer.length; i++) {
            answer[i] = number++;
        }
        
        return answer;
    }
}