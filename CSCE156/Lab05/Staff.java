package unl.cse.payroll;

public class Staff extends Employee {

	private double hours;
	
	public Staff(int id, String firstName, String lastName, String type,
			String position, double hours) {
		super(id, firstName, lastName, type, position);
		// TODO Auto-generated constructor stub
		this.hours = hours;
	}

public double getAnnualPay() {
		
		double pay = 0.0;
		
		if ( this.getPosition().equals("full-time") ) {
			
			pay = 41000;
		} else if ( this.getPosition().equals("part-time") ) {
			
			pay = 8.5*hours*52;
			
		}
		
		return pay; 
		
	}

}
