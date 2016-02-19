package unl.cse.payroll;

public class Faculty extends Employee {

	public Faculty(int id, String firstName, String lastName, String type,
			String position) {
		super(id, firstName, lastName, type, position);
		// TODO Auto-generated constructor stub
	}

	public double getAnnualPay() {
		
		double pay = 0.0;
		
		if ( this.getPosition().equals("Assistant-Professor") ) {
			
			pay = 75000;
		} else if ( this.getPosition().equals("Associate-Professor") ) {
			
			pay = 84000;
			
		} else if ( this.getPosition().equals("Professor") ) {
			
			pay = 93000;
			
		} 
		
		return pay; 
		
	}
	
	
}
