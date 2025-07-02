class DigitSum {
    public int addDigits(int num) {
        if (num == 0) return 0;
        return (num % 9 == 0) ? 9 : (num % 9);
    }
}

public class Main {
    public static void main(String[] args) {
        DigitSum digitSum = new DigitSum();
        System.out.println(digitSum.addDigits(38)); 
        System.out.println(digitSum.addDigits(0));
        System.out.println(digitSum.addDigits(9));
    }
}