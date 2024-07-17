class Solution {
    public int solution(double flo) {
        return Integer.parseInt((flo + "").split("\\.")[0]);
    }
}