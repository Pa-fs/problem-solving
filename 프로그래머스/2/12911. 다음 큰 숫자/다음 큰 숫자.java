import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int cnt = 0;
        String str = Integer.toBinaryString(n);
        for(int i = 0; i < str.length(); i++) {
            if(str.charAt(i) == '1') cnt++;
        }
        for(int i = n + 1; i <= 1000000; i++) {
            String tmp = Integer.toBinaryString(i);
            int count = 0;
            // for(int j = 0; j < tmp.length(); j++) {
            //     if(tmp.charAt(j) == '1') count++;
            // }
            for(char ch : tmp.toCharArray()) {
                if(ch == '1') count++;
            }
            
            if(cnt == count) {
                return i;
            }
        }
        return answer;
    }
}