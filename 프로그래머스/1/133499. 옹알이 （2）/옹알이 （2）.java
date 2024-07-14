class Solution {
    int res;
    String[] arr = new String[]{"aya", "ye", "woo", "ma"};
    public void func(String target, String str, int lev, String lastAdd) {
        if(lev >= 10) return;
        if(str.equals(target)) {
            res++;
            return;
        }
        else {
            for(int i = 0; i < arr.length; i++) {
                if(lastAdd.equals(arr[i])) continue;
                func(target, str + arr[i], lev + 1, arr[i]);
            }
        }
    }
    
    public int solution(String[] babbling) {
        for(String str : babbling) {
            func(str, "", 0, "");
        }
        return res;
    }
}