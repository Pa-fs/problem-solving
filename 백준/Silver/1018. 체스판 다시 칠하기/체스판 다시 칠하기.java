import java.util.Scanner;

public class Main {

    static int n, m;
    static String[][] tableW = new String[8][8];
    static String[][] tableB = new String[8][8];
    static char[][] board = new char[51][51];
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < n; i++) {
            board[i] = sc.next().toCharArray();
        }

        drawTables(tableW, "W");
        drawTables(tableB, "B");

        int cnt1 = Integer.MAX_VALUE, cnt2 = Integer.MAX_VALUE;
        for (int i = 0; i <= n - 8; i++) {
            for (int j = 0; j <= m - 8; j++) {
                int tmp1 = 0, tmp2 = 0;
                for (int k = i; k < i + 8; k++) {
                    for (int l = j; l < j + 8; l++) {
                        if(!tableW[k - i][l - j].equals(board[k][l] + "")) {
                            tmp1++;
                        }
                        if(!tableB[k - i][l - j].equals(board[k][l] + "")) {
                            tmp2++;
                        }
                    }
                }

                cnt1 = Math.min(cnt1, tmp1);
                cnt2 = Math.min(cnt2, tmp2);
            }
        }
        System.out.println(Math.min(cnt1, cnt2));
    }

    private static void drawTables(String[][] table, String str) {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if(i % 2 == 0) {
                    if (j % 2 == 0) {
                        table[i][j] = str.equals("W") ? "W" : "B";
                    } else {
                        table[i][j] = str.equals("W") ? "B" : "W";
                    }
                } else {
                    if(j % 2 == 0) {
                        table[i][j] = str.equals("W") ? "B" : "W";
                    }else {
                        table[i][j] = str.equals("W") ? "W" : "B";
                    }
                }
            }
        }
    }
}