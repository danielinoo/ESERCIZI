public class Main{
    public static void main(String[] args) {

       Computer[] computers = new Computer[10];

       for (int i = 0; i < computers.length; i++){
           computers[i] = new Computer(0, 0, 0,0, 0 ,"Intel", 0 );

           System.out.println("-".repeat(30));
           System.out.println("|\t\tComputer " + (i + 1) + ":");
           System.out.println("-".repeat(30));
           //random valori
           computers[i].setPrezzo();
           computers[i].setPeso();
           computers[i].setLarghezza();
           computers[i].setAltezza();
           computers[i].setProfondita();
           computers[i].setAnno_produzione();

           if (i == 3 || i == 6){
               computers[i].setProduttore("HP");
           } else if (i % 2 == 0) {
               computers[i].setProduttore("Asus");
           }
           else{
               computers[i].setProduttore("Apple");
           }


           System.out.println(computers[i].toString());
       }
    }
}