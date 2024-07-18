import java.util.*;
class Solution {
    public String[] solution(String[] picture, int k) {
        List<String> list = new ArrayList<>();
        String[] answer = {};
        for (String str : picture) {
            String tmp = "";
            for (int i = 0; i < str.length(); i++) {
                for (int j = 0; j < k; j++) {
                    tmp = tmp + str.charAt(i);
                }
            }

            for (int i = 0; i < k; i++) {
                list.add(tmp);
            }
        }
        return list.stream().toArray(String[]::new);
    }
}