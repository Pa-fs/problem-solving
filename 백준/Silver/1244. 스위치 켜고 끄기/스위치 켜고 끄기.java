import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int switch_count = sc.nextInt();
        int[] switchs = new int[switch_count];
        for (int i = 0; i < switch_count; i++) {
            switchs[i] = sc.nextInt();
        }
        int student_count = sc.nextInt();
        int[][] students = new int[student_count][2];

        for (int i = 0; i < student_count; i++) {
            students[i][0] = sc.nextInt();
            students[i][1] = sc.nextInt();
        }

        for (int i = 0; i < student_count; i++) {
            if(students[i][0] == 1) {
                calculateForMan(switchs, students[i][1]);
            } else {
                calculateForWoman(switchs, students[i][1]);
            }
        }

        for (int i = 0; i < switch_count; i++) {
            System.out.print(switchs[i] + " ");
            if( (i+1) % 20 == 0) {
                System.out.println();
            }
        }
    }

    private static void calculateForMan(int[] switchs, int multiple) {

        for (int i = 0; i < switchs.length; i++) {
            if ((i + 1) % multiple == 0) {
                convertSwitch(switchs, i);
            }
        }
    }

    private static void calculateForWoman(int[] switchs, int number) {
        int left = number - 1;
        int right = number - 1;
        convertSwitch(switchs, left);

        while (left > 0 && right < switchs.length - 1) {
            if (switchs[left - 1] == switchs[right + 1]) {
                left--;
                right++;
                convertSwitch(switchs, left);
                convertSwitch(switchs, right);
            } else {
                break;
            }
        }
    }

    private static void convertSwitch(int[] switchs, int i) {
        if(switchs[i] == 0) {
            switchs[i] = 1;
        } else {
            switchs[i] = 0;
        }
    }
}