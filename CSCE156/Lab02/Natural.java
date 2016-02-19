package unl.cse.labs.lab02;

public class Natural {

	public static void main(String args[]) {
		if(args.length != 1) {
			System.err.println("ERROR: expecting a single integer argument");
			System.exit(1);
		}
		
		Integer n = null;
		try {
			n = Integer.parseInt(args[0]);
		} catch (NumberFormatException nfe) {
			System.err.println("ERROR: expecting a single integer argument");
			System.exit(1);
		}
		
		String zeroToTen[] = new String[11];
		zeroToTen[0] = "zero";
		zeroToTen[1] = "one";
		zeroToTen[2] = "two";
		zeroToTen[3] = "three";
		zeroToTen[4] = "four";
		zeroToTen[5] = "five";
		zeroToTen[6] = "six";
		zeroToTen[7] = "seven";
		zeroToTen[8] = "eight";
		zeroToTen[9] = "nine";
		zeroToTen[10] = "ten";

		//TODO: write a for-loop to compute the sum of 1..n
		int sum1=0;
		for (int i=0; i<=n; i++) {
			sum1+=i;
		}
		System.out.println("sum1 = "+sum1);

		//TODO: write a while-loop to compute the sum of 1..n
		int sum2=0;
		int i=0;
		while (i<=n) {
			sum2+=i;
			i++;
		}
		System.out.println("sum2 = "+sum2);

		//TODO: write an enhanced for-loop to iterate over the zeroToTen array 
		for (String s:zeroToTen) {
			System.out.printf(s+" ");
			
		}


	}
}
