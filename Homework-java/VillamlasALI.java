import java.util.Scanner;

public class VillamlasALI {
    public static void main(String[] args) {
        System.out.println("____________________________________________________________");
        
        Scanner thunder = new Scanner(System.in);
        int mega;
        //---------------------------do whilr------------------------------------------- \\

        
        do {
            System.out.print("Haany masodperccel a villámlas utan hallotta a dorgest????\n ");
            mega = thunder.nextInt();
            if (mega < 0) {
                System.out.println("Negativ ertek nem jo , ");
            }
        } while (mega < 0);

        int d = mega * 300;
        System.out.println("A villamlas kbb " + d + " meter tavolsagra volt.");


        //---------------------------------------------------------------------------------------\\
        System.out.println("___________________________________________________________-");
    }
}