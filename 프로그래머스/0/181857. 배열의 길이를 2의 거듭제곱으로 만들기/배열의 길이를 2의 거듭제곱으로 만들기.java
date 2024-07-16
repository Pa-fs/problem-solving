class Solution {
    public int[] solution(int[] arr) {
        if(arr.length == 1) return new int[]{arr[0]};
        int len = arr.length;
        int n = 2;
        while(n < len) n = n * 2;
        int[] answer = new int[n];
        for(int i = 0; i < arr.length; i++) answer[i] = arr[i];
        return answer;
    }
}