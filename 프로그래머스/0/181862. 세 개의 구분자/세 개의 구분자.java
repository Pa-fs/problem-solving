import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        List<String> list = new ArrayList<>();
        String[] answer = myStr.split("a|b|c");
        for(String s : answer) {
            if(s.equals("")) continue;
            list.add(s);
        }
        return list.size() == 0 ? new String[]{"EMPTY"} : list.stream().toArray(String[]::new);
    }
}