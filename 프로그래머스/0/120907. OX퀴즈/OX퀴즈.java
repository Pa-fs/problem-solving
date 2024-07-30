import java.util.*;
class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        int pos = 0;
        for(String str : quiz) {
            String[] split = str.split(" ");
            int a = Integer.parseInt(split[0]);
            String op = split[1];
            int b = Integer.parseInt(split[2]);
            int c = Integer.parseInt(split[4]);
            int res = 0;
            
            res = op.equals("+") ? a + b : a - b;
            answer[pos++] = res == c ? "O" : "X";
        }
        return answer;
    }
}