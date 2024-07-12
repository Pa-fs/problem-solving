import java.util.*;

class Solution {
    public String[] solution(String myString) {
        List<String> list = new ArrayList<>();
        String[] arr = myString.split("x");
        for(String s : arr) {
            if(s.equals("")) continue;
            list.add(s);
        }
        Collections.sort(list);
        return list.stream().toArray(String[]::new);
    }
}