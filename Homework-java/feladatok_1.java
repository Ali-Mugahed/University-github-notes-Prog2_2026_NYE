
import java.util.Scanner;

public class feladatok_1 {
    public static void main(String[] args) {
        int a=21;
        String m= "szia";
    
        System.out.println( m+  "  mugahed vagyok  es jemenbol jetem  es "+ a +" eves");
        
        
        //--------------------------the account--------------------------------\\
        System.out.println("------------------------------------------");

        float a1=12,b1=5;
        a1++;
        b1--;
        float c=a1-b1;
        float c1= a1*b1;
        float c2 =a1/b1;
        float c3 =a1+b1;
        System.out.println("kivonás "+a+"-"+b1+"="+c);
           System.out.println("szofrzs "+a+"*"+b1+"="+c1);
           System.out.println("osztas "+a+"/"+b1+"="+c2);
           System.out.println("összeadás "+a+"+"+b1+"="+c3+"\n");



               //-------------if------------------------------\
               System.out.println("---------------if---------------------------");
           Scanner nev = new Scanner(System.in);

           String nevs;
           int eves;
          


           System.out.println("addj meg a neved ");
           nevs= nev.nextLine();
           
           System.out.println("adj meg  evs");
           eves=nev.nextInt();

            if (eves >=18 && eves < 130)
           {
            System.out.println("te felnott vagy "); 
           }

           if (eves >=0 && eves <=17)
           {
            System.out.println("te fiatalkoru vagy");

           }
           else
           {
            System.out.println("hiba van eletor megadasaban");
           }

           System.out.println("szia "+ nevs + " es eletkorod = " + eves + " eve \n " );
           //..................................................\\





           //....................loop ....for........................\\
           System.out.println("------------------------------------------");
           
           Scanner loop = new Scanner(System.in);
           String szot ;
           int szam;
           
           System.out.println("melyik szot szeretned leirnl ");
           szot=loop.nextLine();

            System.out.println("hanyszor ? ");
            szam=loop.nextInt();
            System.out.println(" ");

            for (int i = 0; i < szam; i++)

                {
                    System.out.println((i+1)+"- " + szot);
                }
            //-------------------------while------------------------------\\
                System.out.println("------------------------------------------");
    
        int m1=0;
        while( m1<szam)
            {
                   System.out.println((m1+1)+"- " + szot); 
                   m1++;
            }
         System.out.println("------------------------------------------");
         //-----------------------------------------------------------------------\\








            


           


 

    }
}
