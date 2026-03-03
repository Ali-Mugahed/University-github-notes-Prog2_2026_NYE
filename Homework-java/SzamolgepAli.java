import java.util.Scanner;

public class SzamolgepAli {
    public static void main(String[] args) {
        //_1)___________________________input_________________________________________\\
        Scanner input_0 = new Scanner(System.in);

        if (args.length < 3) {
            System.out.println("Adja meg ez : [add, sub, mul, div]");
            System.out.println("[add == +], [sub == -], [mul == *], [div == /] \n");
            System.out.println("_________________________________________________");

            String muvelet0_in = input_0.nextLine();

            System.out.print("aadj meg  egy szam: ");
            String szam1_in = input_0.nextLine();

            System.out.print(" adj meg  Masodik szam: ");
            String szam2_in = input_0.nextLine();

            args = new String[]{muvelet0_in, szam1_in, szam2_in};
        }
        //================================================================================\\


        //_2)______________________________OPeration____________________________________--\\
        System.out.println("_________________________________________________");

        String muvelet = args[0]; 
        double szam_1 = Double.parseDouble(args[1]); 
        double szam_2 = Double.parseDouble(args[2]); 
        double number_0 = 0;

        switch (muvelet.toLowerCase()) {

            case "add":
                number_0 = szam_1 + szam_2;
                break;

            case "sub":
                number_0 = szam_1 - szam_2;
                break;

            case "mul":
                number_0 = szam_1 * szam_2;
                break;

            case "div":
                if (szam_2 != 0) {
                    number_0 = szam_1 / szam_2;
                } else {
                    System.out.println("Hiba: Nullaval nem lehet !");
                    return;
                }
                break;

            default:
                System.out.println("Ez az opcio nem erheto el, kerjuk valasszon ujra!");
                return;
        }
        //===========================================================================================\\



        //_3)__________________________thee final result _________________________________________________________-\\
        System.out.println(" Eredmeny = " + number_0);
        System.out.println("_________________________________________________");
        input_0.close();
        //============================================================\\
    }
}