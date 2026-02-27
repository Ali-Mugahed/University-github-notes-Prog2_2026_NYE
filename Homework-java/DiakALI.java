public class DiakALI {
    // 1) _______________ alap _________________ \\
    String nev;
    double[] grades;
    // __________________________________________ \\


    // 2) ____________________ B _________________ \\
    public DiakALI(String nev, double[] grades)
     {
        this.nev = nev;
        this.grades = grades;
    }
    // __________________________________________ \\


    // 3) ________________ calculateAverage _______________ \\
    public double calculateAverage() {
        if (grades.length == 0) return 0.0; 

        double osszeg = 0;
        for (int a = 0; a < grades.length; a++) {
            osszeg += grades[a]; 
        }
        return osszeg / grades.length; 
    }
    // ____________________________________________________ \\


    public static void main(String[] args) {
        
        double[] jegy = {4.9, 4.6, 3.2, 5.0};

        
        DiakALI student = new DiakALI("ALI MUGAHED ", jegy);

        System.out.println("_____________________________________________");
        System.out.println("[[Diak adati]]\n");
        System.out.println("Diak neve: " + student.nev);
        System.out.println("atlagos osztaalyzat: " + student.calculateAverage());
        System.out.println("_____________________________________________");
    }
}