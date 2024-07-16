class Solution {
    public int[] solution(int[] arr) {
        int len = arr.length;
        int n = 1;
        while(n < len) n = n * 2;
        int[] answer = new int[n];
        for(int i = 0; i < arr.length; i++) answer[i] = arr[i];
        return answer;
    }
}