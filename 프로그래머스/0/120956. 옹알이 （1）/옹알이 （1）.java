class Solution {
    int res = 0;
    String[] arr = new String[]{"aya", "ye", "woo", "ma"};
    boolean[] visited = new boolean[arr.length];
    public void func(String target, String str, int lev) {
        if(lev > arr.length) return;
        if(str.equals(target)) {
            res++;
            return;
        }
        for(int i = 0; i < arr.length; i++) {
            if(visited[i]) continue;
            visited[i] = true;
            func(target, str + arr[i], lev + 1);
            visited[i] = false;
        }
    }
    public int solution(String[] babbling) {
        for(String str : babbling) {
            func(str, "", 0);
        }
        return res;
    }
}