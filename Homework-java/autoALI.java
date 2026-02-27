public class autoALI {
   //1)_____________alap__________________\\
    String mark;
    String modell;
    int year;
   //_______________________________________\\




    //2)____________________B___________________________________\\
    public autoALI(String mark, String modell, int year) {
        this.mark = mark;
        this.modell = modell;
        this.year = year;
    }
    //__________________________________________________________\\




//3)______________________________informacio_______________________________________\\

    public void displayInfo() {
        System.out.println("______________________________________");
        System.out.println("[[informacio]]");
        System.out.println("Auto adatai: " + year + " " + mark + " " + modell + "\n");
    }
    //_______________________________________________________________________\\




//4)________________________inditasa__________________________________\\
    
    public void startEngine() {
        System.out.println("______________________________________");
        System.out.println("[[[inditasa]]]");
        System.out.println("A auto indul\n");
    }
//________________________________________________________\\




//5______________________leallitasa___________________________________--\\
    
    public void stopEngine()
     {
        System.out.println("______________________________________");
        System.out.println("[[[leallitasa]]]");
        System.out.println("A auto megall\n");
        System.out.println("______________________________________");
    }
 //___________________________________________________________________________________\\






public static void main(String[] args) {
        
        autoALI aliCar = new autoALI("**BMW**", "**xx4**", 2010);
        

        aliCar.displayInfo();
        aliCar.startEngine();
        aliCar.stopEngine();
    

    }

}
