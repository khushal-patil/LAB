class Nptel extends Thread {
    public void run() {
        System.out.println("Running");

    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Runnable t = new Nptel();
        Thread mythread = new Thread(t);
        mythread.start();
    }
}
