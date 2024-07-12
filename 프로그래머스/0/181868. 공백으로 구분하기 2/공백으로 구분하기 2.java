import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        String[] answer = my_string.split(" ");
        List<String> list = new ArrayList<>();
        for(String str : answer) {
            if(str.equals("")) continue;
            list.add(str);
        }
        return list.stream().toArray(String[]::new);
    }
}