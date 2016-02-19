package unl.cse.labs.lab02;

public class ChildCredit {

	public static void main(String args[]) {
		Child tom = new Child("Tommy", 14);
		Child dick = new Child("Richard", 12);
		Child harry = new Child("Harold", 21);
		
		Child arr[] = new Child[3];
		arr[0] = tom;
		arr[1] = dick;
		arr[2] = harry;

		//TODO: write a loop to iterate over the elements in the child array 
		//      and output a table as specified
		final String HEADING_FMT_STR = "%-17s%s\n";
		final String DATA_FMT_STR = "%-17s%s\n";
		System.out.printf(HEADING_FMT_STR,"Child","Amount");
		double amount=0.00;
		double totalCredit=0.00;
		int n=1;
		for (Child s:arr) {
			if (s.getAge()<18 && n<=1) {
				amount=1000.00;
				n++;
			} else if (s.getAge()<18 && n>1) {
				amount=500.00;
				n++;
			}
			else {
				amount=0.00;
				n++;
			}
			
			System.out.printf(DATA_FMT_STR,s.toString(),"$"+amount);
			totalCredit+=amount;
		}
		System.out.printf(DATA_FMT_STR,"Total Credit:","$"+totalCredit);
		
	}
}
