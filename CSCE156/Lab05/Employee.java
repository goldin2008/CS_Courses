package unl.cse.payroll;

///////////////TO DO
//public class Employee {

public abstract class Employee implements Payable, Person {

    private final String firstName;
    private final String lastName;
    private final int id;
    private final String type;
    private final String position; 

    /**
     * Constructor
     * @param firstName
     * @param lastName
     * @param id
     * @param type
     */
    public Employee(int id, String firstName, String lastName, String type,
            String position) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.id = id;
        this.type = type;
        this.position = position; 
    }

    /**
     * @return the id
     */
    public int getId() {
        return this.id;
    }

    /**
     * @return the type
     */
    public String getType() {
        return this.type;
    }
    
    public String getPosition() {
    	return this.position;
    }
    
    public Double getAnnualFica() {
    	/*///////////////TO DO
    	 * FICA is:
    	 *  - 6.20% up to 106800 per year for Social Security
    	 *  - 1.45% for Medicare on all income
    	 */
    	return this.getAnnualPay()*(.062 + 0.0145);
    }
    
    ///////////////TO DO
	@Override
	public abstract double getAnnualPay();
	//////////////TO DO
	@Override
	public String getFirstName() {
		// TODO Auto-generated method stub
		return this.firstName;
	}
	///////////////TO DO
	@Override
	public String getLastName() {
		// TODO Auto-generated method stub
		return this.lastName;
	}
    
    
    
}
