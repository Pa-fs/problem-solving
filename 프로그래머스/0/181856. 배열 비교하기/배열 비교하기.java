class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = arr1.length < arr2.length ? -1 : arr1.length > arr2.length ? 1 : 0;
        if(answer == 0) {
            int sum1 = 0, sum2 = 0;
            for(int i = 0; i < arr1.length; i++) sum1 = sum1 + arr1[i];
            for(int i = 0; i < arr2.length; i++) sum2 = sum2 + arr2[i];
            answer = sum1 < sum2 ? -1 : sum1 > sum2 ? 1 : 0;
        }
        return answer;
    }
}