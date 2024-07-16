class Solution {
    public int solution(String[] strArr) {
        int[] lengths = new int[31];
        int answer = 0;
        for(String str : strArr) lengths[str.length()]++;
        for(int len : lengths) answer = Math.max(answer, len);
        return answer;
    }
}