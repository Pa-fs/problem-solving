import java.util.*;
class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        Arrays.fill(answer, -1);
        int cnt = 0;
        for(int i = 0; i < arr.length; i++) {
            if(cnt == k) break;
            boolean isExist = false;
            for(int j = 0; j < answer.length; j++) {
                if(arr[i] == answer[j]) {
                    isExist = true;
                    break;
                }
            }
            if(isExist) continue;
            else answer[cnt++] = arr[i];
        }
        return answer;
    }
}