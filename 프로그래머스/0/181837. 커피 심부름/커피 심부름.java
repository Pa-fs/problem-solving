class Solution {
    public int solution(String[] order) {
        int answer = 0;
        // contains 메소드
        for(String str : order) {
            if(str.contains("americano") || str.contains("anything")) {
                answer = answer + 4500;
            } else if(str.contains("cafelatte")) {
                answer = answer + 5000;
            }
        }
        return answer;
    }
}