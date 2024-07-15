class Solution {
    public int solution(String myString, String pat) {
        String str = "";
        for(char ch : myString.toCharArray()) {
            if(ch == 'A') str = str + 'B';
            else str = str + 'A';
        }
        return str.indexOf(pat) != -1 ? 1 : 0;
    }
}