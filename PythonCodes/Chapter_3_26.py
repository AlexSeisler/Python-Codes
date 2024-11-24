import java.util.Scanner;
public class MyProgram
{
    public static void main(String[] args)
    {
        Scanner input= new Scanner(System.in);
        
        System.out.println("Please enter a number from 0-3,999: ");
        int integer=input.nextInt();
        
        if (integer==0)
            {
                System.out.println("NULLA");
            }
        if (integer>=1000)
        {
            int i=0;
            int amount=integer/1000;
            integer=integer%1000;
            for (i=0;i<amount;i++)
            {
            System.out.print("M");
            }
        }
        if (integer>=900)
        {
            integer=integer-900;
            System.out.print("CM");
        }
        if (integer>=500)
        {
            System.out.print("D");
            integer=integer%500;
        }
        if (integer>=400)
        {
            integer=integer-400;
            System.out.print("CD");
            
        }
        if (integer>=100)
        {
            int i=0;
            int amount=integer/100;
            integer=integer%100;
            for (i=0;i<amount;i++)
            {
            System.out.print("C");
            }
        }
        if (integer>=90)
        {
            integer=integer-90;
            System.out.print("XC");
        }
        if (integer>=50)
        {
            System.out.print("L");
            integer=integer-50;
        }
        if (integer>=40)
        {
            integer=integer-40;
            System.out.print("XL");
            
        }
        if (integer>=10)
        {
            int i=0;
            int amount=integer/10;
            integer=integer%10;
            for (i=0;i<amount;i++)
            {
            System.out.print("X");
            }
        }
        if (integer>=9)
        {
            integer=integer-9;
            System.out.print("IX");
            
        }
        if (integer>=5)
        {
            System.out.print("V");
            integer=integer-5;
        }
        if (integer>=4)
        {
            integer=integer-4;
            System.out.print("IV");
            
        }
        if (integer>=1)
        {
            int i=0;
            int amount=integer/1;
            integer=integer%1;
            for (i=0;i<amount;i++)
            {
            System.out.print("I");
            }
        }
        
        
    }
}