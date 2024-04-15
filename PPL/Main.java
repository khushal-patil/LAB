class NPTEL extends Thread{
       public void run(){
        System.out.println("I am from Run...");
    }
}

class Main {
    public static void main(String[] args) {
        
    NPTEL t= new NPTEL();
    t.start();
    }
}