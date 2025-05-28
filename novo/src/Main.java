import java.util.Random;
import java.util.Vector;

//Riscala Miguel Fadel Neto, Augusto Trindade Schulze de Sousa

class Threads extends java.lang.Thread{
    private Double[] vetor;
    private int inicio;
    private int finalt;
    public int contador;

    public Threads(Double[] vetor, int inicio, int finalt){
        this.vetor = vetor;
        this.inicio = inicio;
        this.finalt = finalt;

    }

    public void run(){
       prencherRandom();
    }

    public void prencherRandom(){
        Random rand = new Random();
        for (int i = inicio; i < finalt; i++){
            double random = rand.nextDouble();
            vetor[i] = random;
            if (random >= 0.25 && random <= 0.75){
                contador++;
            }
        }
    }
}
public class Main {
    public static void main(String[] args) throws InterruptedException {
        long inicioTempo = System.currentTimeMillis();

        Double[] vetor = new Double[20_000_000];
        int vetorDividido = vetor.length / 4;
        int resto = vetor.length % 4;
        Threads thread1 = new Threads(vetor, 0, vetorDividido);
        Threads thread2 = new Threads(vetor, vetorDividido, vetorDividido * 2);
        Threads thread3 = new Threads(vetor, vetorDividido * 2, vetorDividido * 3);
        Threads thread4 = new Threads(vetor, vetorDividido * 3, (vetorDividido * 4) + resto);

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();
        thread1.join();
        thread2.join();
        thread3.join();
        thread4.join();

        System.out.println("Encerrou incialização");

        int contador = thread1.contador + thread2.contador + thread3.contador + thread4.contador;

        long finalTempo = System.currentTimeMillis();
        long duracao = finalTempo - inicioTempo;

        System.out.println(contador);
        System.out.println("Duração: " + duracao + " milisegundos");
    }
}