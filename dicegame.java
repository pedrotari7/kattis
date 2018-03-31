import java.util.Scanner;

public class dicegame {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] gunnar = sc.nextLine().split(" ");
        String[] emma = sc.nextLine().split(" ");;

        int gunnar_wins = 0;
        int emma_wins = 0;

        for(int g1 = Integer.parseInt(gunnar[0]); g1 <= Integer.parseInt(gunnar[1]); g1++) {
            for(int g2 = Integer.parseInt(gunnar[2]); g2 <= Integer.parseInt(gunnar[3]); g2++) {
                for(int e1 = Integer.parseInt(emma[0]); e1 <= Integer.parseInt(emma[1]); e1++) {
                    for(int e2 = Integer.parseInt(emma[2]); e2 <= Integer.parseInt(emma[3]); e2++) {
                        if (g1 + g2 > e1 + e2)
                            gunnar_wins += 1;
                        else if(e1 + e2 > g1 + g2)
                            emma_wins += 1;
                    }
                }
            }
        }

        if(gunnar_wins > emma_wins) {
            System.out.println("Gunnar");
        } else if(emma_wins > gunnar_wins){
            System.out.println("Emma");
        } else {
            System.out.println("Tie");
        }

        sc.close();
    }
}