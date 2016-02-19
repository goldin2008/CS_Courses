package unl.cse.labs.lab03;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class DNA {

	public static void main(String args[]) {

		String fileName = "data/H1N1nucleotide.txt";
		Scanner s = null;
		try {
			s = new Scanner(new File(fileName));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		String dna = "";

		while(s.hasNext()) {
			dna += s.next().trim();
		}
		s.close();

		String subsequence = "gt";
		//String subsequence = "gatacatatgcagtgggattttcggagacaatccacgccctaat";

		int count = 0; 
		//write code to count the number of times subsequence appears in the dna string
		for (int i=0; i<dna.length()-subsequence.length(); i++ ) {
			if ( dna.charAt(i)==subsequence.charAt(0) ) {
				int pos = 1;
				for (int j=1; j<subsequence.length(); j++) {
					if (dna.charAt(i+j) == subsequence.charAt(j) ) {
						pos++;
						if (pos == subsequence.length() ) {
							count++;
						}
					}
				}
			}
		}

		System.out.println(subsequence + " appears " + count + " times");
		
	}
	
}
