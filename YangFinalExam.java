import java.util.Scanner;

public class YangFinalExam
{
    public static void main(String[] args)
    {
        runProgram();
    }
    
    public static void runProgram()
    {
        Scanner in = new Scanner(System.in);
        String keep_going = "yes";
        while(keep_going.equalsIgnoreCase("yes"))
            {
                displayInfo();
                double payRate = getRate();
                double hoursWorked = getHours();
                double grossPay = calculateGrossPay(payRate, hoursWorked);
                displayRHGrossPay(payRate, hoursWorked, grossPay);
                System.out.println("");
                System.out.println("Would you like to run the program again? Enter yes or no: ");
                keep_going = in.next();
                System.out.println("");
            }
    in.close();
    System.out.println("Program terminated. Goodbye!");
    }
    public static void displayInfo()
    {
        System.out.println("");
        System.out.println("Davy Yang");
        System.out.println("12 DEC 2024");
        System.out.println("This program calculates employee pay");
        System.out.println("");
    }
    public static double getRate()
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter current pay rate per hour: ");
        return in.nextDouble();
    }
    public static double getHours()
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter number of hours worked: ");
        return in.nextDouble();
    }
    public static double calculateGrossPay(double rate, double hours)
    {
        return (rate * hours);
    }
    public static void displayRHGrossPay(double payRate, double hoursWorked, double grossPay)
    {
        System.out.println("");
        System.out.println("The pay rate is $" + payRate);
        System.out.println("The hours worked are " + hoursWorked);
        System.out.println("The gross pay is $" + grossPay);
    }
}