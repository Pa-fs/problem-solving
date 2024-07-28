import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        
        int[] person = {0, 0, 0};
        
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for(int i = 0; i < answers.length; i++) {
            if(answers[i] == a[i % 5]) person[0]++;
            if(answers[i] == b[i % 8]) person[1]++;
            if(answers[i] == c[i % 10]) person[2]++;
        }
        
        int max = 0;
        for(int i = 0; i < person.length; i++) {
            if(max < person[i]) {
                max = person[i];
            }
        }
        
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < person.length; i++) {
            if(max == person[i]) {
                list.add(i + 1);
            }
        }
        
        answer = new int[list.size()];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}