class Solution {
    public String solution(String my_string, String alp) {
        for(int i = 0; i < my_string.length(); i++) {
            char c = alp.charAt(0);
            char ch = my_string.charAt(i);
            if(c == ch) {
                my_string = my_string.replace(ch, (char)(c - ('a' - 'A')));
            }
        }
        return my_string;
    }
}