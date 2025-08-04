import java.util.Scanner;
class SumOfMultiples {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        int total = 0;
        scanner.close();

        for( int i =1; i<=n; i++){
            if ( i % 3 ==0 || i % 5 == 0 || i % 7 == 0){
                total += i;
            }
        }
        System.out.println(total);
    }
}

