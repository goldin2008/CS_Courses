package unl.cse.library;

public class Author {
	
	private String firstName;   
	private String lastName;

////////CONSTRUCTOR
	public Author(String firstName, String lastName) {
		
		setFirstName(firstName);
		setLastName(lastName);
	}
	
	
	public String getFirstName() {
		return firstName;
	}
	public void setFirstName(String firstName) {
		if (firstName == null)
			System.out.println("Your input is invalid.");
		else
			
			this.firstName = firstName;
	}
	
	public String getLastName() {
		return lastName;
	}
	public void setLastName(String lastName) {
		if (lastName == null)
			System.out.println("Your input is invalid.");
		else
			this.lastName = lastName;
	}
	

	
}
