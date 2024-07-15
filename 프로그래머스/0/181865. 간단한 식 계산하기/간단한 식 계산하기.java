class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String s = binomial.replace(" ", "");
        char op = ' ';
        char[] charr = s.toCharArray();
        for(char ch : charr) {
            if(ch == '+') op = ch;
            else if(ch == '-') op = ch;
            else if(ch == '*') op = ch;
        }
        String[] integers = s.split("\\" + op);
        int a = Integer.parseInt(integers[0]);
        int b = Integer.parseInt(integers[1]);
        if(op == '+') {
            answer = a + b;
        } else if(op == '-') {
            answer = a - b;
        } else {
            answer = a * b;
        }
        return answer;
    }
}