class Solution {
    public String solution(String myString) {
        String answer = "";
        for(int i = 0; i < myString.length(); i++) {
            char ch = myString.charAt(i);
            if(ch == 'a') {
                answer = answer + (char)(ch - ('a' - 'A'));
            } else {
                if(ch >= 'B' && ch <= 'Z') {
                    answer = answer + (char)(ch + ('a' - 'A'));
                }
                else answer = answer + ch;
            }
        }
        return answer;
    }
}