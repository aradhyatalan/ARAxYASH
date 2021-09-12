import java.io.*;
import java.util.Scanner;

class assgnment{
	public static void main(String args[]){//throws IOException{
        Scanner obj=new Scanner(System.in);
        System.out.println("Enter Grade: ");
        String grade=obj.nextLine();

        System.out.println("Percentage is:");

        if (grade.equals("F")){
            System.out.println("0 - 60 %");
        }
        else if(grade.equals("D")){
            System.out.println("61 - 70 %");
        }   
        else if(grade.equals("C")){
            System.out.println("71 - 80 %");
        }
        else if(grade.equals("B")){
            System.out.println("81 - 90 %");
        }
        else if(grade.equals("A")){
            System.out.println("91-100 %");
        }
    }
}


