import java.util.Scanner;

public class AliTorta {
    public static void main(String[] args) {
        Scanner old = new Scanner(System.in);
        int eve;
        
        System.out.print("---------------------------------------------------\n");
        //--------------------------do whil------------------------------------------\\
        do {
            System.out.print("Hany eves vagy 1-20: \n");
            eve = old.nextInt();
        } while (eve < 1 || eve > 20);
        //_____________________________________________________________\\



        //--------------------------for------------------------------------------\\
        for (int stat = 0; stat < eve; stat++) 
            System.out.print("* ");
        System.out.println();

        
        for (int a = 0; a < eve; a++) 
            System.out.print("| ");
        System.out.println();


        for (int a1 = 0; a1 < eve * 2; a1++)
             System.out.print("-");
        System.out.println();
        //________________________________________\\


        System.out.print("_______________________________________________________________\n");
        //--------------------------------------------------------------------\\
    }
}