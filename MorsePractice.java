import java.util.Scanner;

public class MorsePractice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String symbol = "";
        boolean running = true;

        System.out.println("Enter press time in ms(pause or exit)");

        while (running) {
            String input = sc.nextLine();
            if (input.equals("exit")) {
                running = false;
            }else if (input.equals("pause")) {
                System.out.println("Letter Finished :" + symbol);
                symbol = "";
            }else {
                int time = Integer.parseInt(input);
                if (time < 200) {
                    symbol +=".";
                }else {
                    symbol += "-";
                }
                System.out.println("Current Morse: " + symbol);
            }
        }
        
        System.out.println("programme ended.");
        sc.close();
    }
}
