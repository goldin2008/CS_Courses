package unl.cse.payroll;

import java.io.File;
import java.text.NumberFormat;
import java.util.Scanner;

/**
 * Class designed for testing and executing the correctness of
 * the three classes that you implemented Employee.java,
 * FullTimeEmployee.java, PartTimeEmployee.java
 */
public class Payroll {

	private Employee employees[];
	private int numEmployees = 0;
	private NumberFormat nf = NumberFormat.getCurrencyInstance();

	public Payroll() {
		this.employees = new Employee[100];
		loadFile();
	}
	
	private void loadFile() {

		try {
			String fileName = "data/employeeRecords.txt";
			File inFile = new File(fileName); 
			Scanner s = new Scanner(inFile);
			int i=0;
			while(s.hasNextLine())
			{
				String line = s.nextLine();
				String tokens[] = line.split(",");
				Integer id = Integer.parseInt(tokens[0]);
				String lastName = tokens[1];
				String firstName = tokens[2];
				String employeeType = tokens[3]; //Faculty or Staff
				//Faculty: Assistant-Professor, Associate-Professor, or Professor
				//Staff: full-time or part-time
				// TO DO
//				String position = tokens[4]; 
//				Double hoursPerWeek = null;
				String position = tokens[4];
				Double hoursPerWeek = 0.0;
				
				
				try {
					hoursPerWeek = Double.parseDouble(tokens[5]);
				} catch (Exception e) {}
				
				/////TO DO
				//Employee e = new Employee(id, firstName, lastName, employeeType, position);
				Employee e;
				if (employeeType.equalsIgnoreCase("Staff")) {
					e = new Staff(id, firstName, lastName, employeeType, position, hoursPerWeek);
					
				} else {
					e = new Faculty(id, firstName, lastName, employeeType, position);
				}
				///////////
				
				this.employees[i] = e;
				i++;
			}
			this.numEmployees = i;
		} catch (Exception e) {
			e.printStackTrace();
		}
	
	}
	
	public void printAnnualReport() {
		System.out.println(String.format("%-20s %10s %10s", "Employee Name", "Annual Pay", "FICA"));
		for(int i=0; i<this.numEmployees; i++) {
			Employee e = this.employees[i];
//			System.out.println(String.format("%-20s %10s %10s", "TODO",
//						                                        "TODO", 
//						                                        nf.format(e.getAnnualFica())));
			
			System.out.println(String.format("%-20s %10s %10s", e.getLastName() + ", "+ e.getFirstName(),
																nf.format(e.getAnnualPay()), 
                    											nf.format(e.getAnnualFica())));
			
			
		}
	}
	
    public static void main(String[] args) {
    	Payroll payroll = new Payroll();
    	payroll.printAnnualReport();
    }
}
