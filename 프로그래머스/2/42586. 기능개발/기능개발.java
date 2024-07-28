import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] time = new int[progresses.length];
        // 시간 측정
        for(int i = 0; i < progresses.length; i++) {
            int tmp = progresses[i];
            int completedDay = 1;
            while(tmp + speeds[i] < 100) {
                tmp += speeds[i];
                completedDay++;
            }
            time[i] = completedDay;
        }
        // 뒤에 있는 기능이 앞에 기능이 배포될 때 같이 배포
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < time.length; i++) {
            int std = time[i];
            if(std < 0) continue;
            int completed = 1;
            for(int j = i + 1; j < time.length; j++) {
                if(std >= time[j]) {
                    completed++;
                    time[j] = -1;
                }
                else break;
            }
            list.add(completed);
        }
        int[] answer = list.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}