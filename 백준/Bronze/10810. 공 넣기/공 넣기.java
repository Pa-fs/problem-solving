import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] cart = new int[n + 1];

        for (int i = 0; i < m; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            int ball = sc.nextInt();

            for (int j = start; j <= end; j++) {
                cart[j] = ball;
            }
        }

        for (int i = 1; i <= n; i++) {
            System.out.print(cart[i] + " ");
        }
    }
}