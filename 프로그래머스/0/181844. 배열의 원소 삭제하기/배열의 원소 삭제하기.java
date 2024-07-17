import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < arr.length; i++) {
            boolean isFound = false;
            for(int j = 0; j < delete_list.length; j++) {
                if(arr[i] == delete_list[j]) {
                    isFound = true;
                }
            }
            
            if(!isFound) list.add(arr[i]);
        }
        return list.stream().mapToInt(i->i).toArray();
    }
}