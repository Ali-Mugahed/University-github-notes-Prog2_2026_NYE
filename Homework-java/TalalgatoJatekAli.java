import java.util.Random;
import java.util.Scanner;

public class TalalgatoJatekAli {
    public static void main(String[] args) {
//_____________________________input______________________________-\\
        Scanner input = new Scanner(System.in);
        Random veletlen = new Random();

        int szam_0 = veletlen.nextInt(100) + 1; 
        int szam_1 = 0;

        System.out.println("adja meg egy szam 1tol - 100ig");
        System.out.println("______________________________________________");

//____________________________whil__________________________________\\
        while (szam_1 != szam_0) {
            System.out.print("Kerem a egg szam: ");
            
            if (input.hasNextInt()) {
                szam_1 = input.nextInt();

                if (szam_1 < szam_0) {
                    System.out.println("Nagyobb szamot ");
                } else if (szam_1 > szam_0) {
                    System.out.println("Kisebb szamot ");
                } else {
                    System.out.println("Gratulalok!   ✨✨😃😃✨✨✨✨✨: " + szam_0);
                }
            } else {
                System.out.println("Hiba Kerlek szamot adj meg😒😒");
                input.next(); 
            }
        }

        input.close();
    }
}