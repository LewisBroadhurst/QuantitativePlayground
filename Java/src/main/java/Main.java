import java.util.concurrent.atomic.AtomicInteger;

public class Main {

    // So any main class is runnable and instantiates a Java runner...
    // From this runner we can link out to other resources and processes in our application
    // e.g. For a Spring Project, we create a bunch of endpoints that we can request resources from
    public static void main(String args[]) {

        AtomicInteger integer = new AtomicInteger();

        new Thread(() -> {
            while (true) {
                integer.getAndIncrement();
                System.out.println(integer.get());
            }
        }).start();
    }
}
