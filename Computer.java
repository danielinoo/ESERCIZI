public class Computer {

    private double prezzo;
    private double peso;
    private double larghezza;
    private double altezza;
    private double profondita;
    private int anno_produzione;
    private String produttore;
    static int num_pc = 0;

    public Computer(double prezzo, double peso,double larghezza, double altezza, double profondita, String produttore, int anno_produzione) {
        this.prezzo = prezzo;
        this.peso = peso;
        this.larghezza = larghezza;
        this.altezza = altezza;
        this.profondita = profondita;
        this.produttore = produttore;

        this.anno_produzione = anno_produzione;
        num_pc ++;
    }

    public Computer(String s){}

    public double getPeso() {
        return peso;
    }
    public void setPeso() {
        this.peso = Math.random()*(200-100)+100;
    }
    public double getAnno_produzione() {
        return anno_produzione;
    }
    public void setAnno_produzione() {
        this.anno_produzione = (int) (Math.floor(Math.random() * 5) + 2000);
    }
    public double getPrezzo() {
        return prezzo;
    }
    public void setPrezzo() {
        this.prezzo = Math.random()*(2000-1000)+1000;
    }

    public String getProduttore() {
        return produttore;
    }
    public void setProduttore(String produttore) {
        this.produttore = produttore;
    }

    public double getLarghezza() {
        return larghezza;
    }

    public void setLarghezza() {
        this.larghezza = Math.random()*5.1;
    }

    public double getAltezza() {
        return altezza;
    }

    public void setAltezza() {
        this.altezza = Math.random()*5.1;
    }

    public double getProfondita() {
        return profondita;
    }

    public void setProfondita() {
        this.profondita = Math.random()*5.1;
    }


    public String toString(){
        return String.format("| Prezzo: %.2f $ \n| Peso: %.0f g. \n| Dimensioni: %.2f x %.2f x %.2f\n| Produttore: %s\n| Anno di produzione: %d ", prezzo, peso, larghezza, altezza, profondita,produttore, anno_produzione );
    }


}