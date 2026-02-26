import java.util.Scanner;

public class AliHomerseklet {
    public static void main(String[] args) {
        Scanner degrees = new Scanner(System.in);
        System.out.print("-------------------------------------------------");
        System.out.print("\n meg tudani a homerseklet most :\n");
        int fok = degrees.nextInt();
        
        //-------------------------------if----------------------------\\
        if (fok <= 0 && fok >=-100) {
            System.out.println("Fagypont alatti");
        } else if (fok < 30 && fok > 0  ) {
            System.out.println("Átlagos");
        } else if (fok>=30&&fok<=100 ) {
            System.out.println("Túl meleg");
        }
         else {
            System.out.println("ervénytelen  a szam ");

         }
         //-----------------------------------------\\
         System.out.print("-------------------------------------------------");
    }
}