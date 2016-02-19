/******************************************************************************
 *
 * Filename :     CoursePlanner.java
 * Author:        Lei Yu
 * Date:          09/04/2012
 * Description:  This program computes the time a student spends in a college course.
 *
 ******************************************************************************/

import java.util.Scanner;


/* Provide a description of the class */
public class CoursePlanner 
{

    public static void main(String[] args) 
    {

    	// Welcome user, and explain the function and regulation of this program
    	System.out.println("Welcome to CoursePlanner.");
    	System.out.println("I will help you estimate the time you will spend in CSCE 155.");
    	System.out.println("All times should be entered in minutes.");
    	
    	
    	
        /* The following code enables the user to accept input from the keyboard. Keep this code as it is. */

        Scanner scanner = new Scanner(System.in);
        
        // Declare and initialize the variables as needed
        int numOfLectures;
        // Prompt the user with a descriptive message
        // Prompt the user to enter number of lectures in CSCE 155
    	System.out.print("Enter Number of Lectures in CSCE 155: ");
    	// Read the number (time in minutes) the user enters using "scanner.nextInt();"
    	numOfLectures = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int durationOfEachLecture;
    	// Prompt the user to enter the duration of each lecture
    	System.out.print("Enter the duration of each lecture: ");
    	durationOfEachLecture = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int outsideClass;
    	// Prompt the user to enter how long you plan to study outside of class per lecture
    	System.out.print("Enter how long you plan to study outside of class per lecture: ");
    	outsideClass = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int numOfAssignment;
    	// Prompt the user to enter Number of Assignments
    	System.out.print("Enter Number of Assignments: ");
    	numOfAssignment = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int eachAssignment;
    	// Prompt the user to enter how long you will take to complete each assignment
    	System.out.print("Enter how long you will take to complete each assignment: ");
    	eachAssignment = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int prepareFirstMidterm;
    	// Prompt the user to enter how much time you will spend preparing for the first midterm exam
    	System.out.print("Enter how much time you will spend preparing for the first midterm exam: ");
    	prepareFirstMidterm = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int completeFirstMidterm;
    	// Prompt the user to enter how much time you will spend completing the first midterm exam
    	System.out.print("Enter how much time you will spend completing the first midterm exam: ");
    	completeFirstMidterm = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int prepareSecondMidterm;
    	// Prompt the user to enter how much time you will spend preparing for the second midterm exam
    	System.out.print("Enter how much time you will spend preparing for the second midterm exam: ");
    	prepareSecondMidterm = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int completeSecondMidterm;
    	// Prompt the user to enter how much time you will spend completing the second midterm exam
    	System.out.print("Enter how much time you will spend completing the second midterm exam: ");
    	completeSecondMidterm = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int prepareFinal;
    	// Prompt the user to enter how much time you will spend preparing for the final exam
    	System.out.print("Enter how much time you will spend preparing for the final exam: ");
    	prepareFinal = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int completeFinal;
    	// Prompt the user to enter how much time you will spend completing the final exam
    	System.out.print("Enter how much time you will spend completing the final exam: ");
    	completeFinal = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int numLabs;
    	// Prompt the user to enter Number of Labs
    	System.out.print("Enter Number of Labs: ");
    	numLabs = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int eachLab;
    	// Prompt the user to enter how long you will take to complete each lab
    	System.out.print("Enter how long you will take to complete each lab: ");
    	eachLab = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int numIC2;
    	// Prompt the user to enter Number of IC2 activities
    	System.out.print("Enter Number of IC2 activities: ");
    	numIC2 = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int eachIC2;
    	// Prompt the user to enter how long you will take to complete each IC2 activity
    	System.out.print("Enter how long you will take to complete each IC2 activity: ");
    	eachIC2 = scanner.nextInt();
    	
    	// Declare and initialize the variables as needed
    	int pat;
    	// Prompt the user to enter how long you will take to complete the PAT
    	System.out.print("Enter how long you will take to complete the PAT: ");
    	pat = scanner.nextInt();
    	
    	// Compute the total commitment for the course
    	// Calculate and output the total time in minutes you will spend in CSCE 155
    	int totalInMinutes = numOfLectures*durationOfEachLecture + numOfLectures*outsideClass + numOfAssignment*eachAssignment +
    			prepareFirstMidterm + completeFirstMidterm + prepareSecondMidterm + completeSecondMidterm +
    			prepareFinal + completeFinal + numLabs*eachLab + numIC2*eachIC2 + pat;
    	
    	System.out.println("Total in minutes: "+totalInMinutes);
    	
    	// Convert the units from minutes to weeks
    	int weeks = totalInMinutes / (7*24*60);
    	// Convert the units from minutes to days
    	int days = (totalInMinutes - weeks*7*24*60) / (24*60);
    	// Convert the units from minutes to hours
    	int hours = (totalInMinutes - weeks*7*24*60 - days*24*60) / 60;
    	// Calculate the remainder time in minutes
    	int minutes = totalInMinutes - weeks*7*24*60 - days*24*60 - hours*60;
    	
    	// Display the commitment using a descriptive message
    	// Output the result in desired expression
    	System.out.println("The total time you will spend in CSCE 155 is "+weeks+" weeks, "+days+" days, "+hours+" hours, and "+
    	minutes+" minutes.");
    	


    }
}
