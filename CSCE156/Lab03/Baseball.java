package unl.cse.labs.lab03;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Baseball {

	public static void main(String args[]) {
		
		String fileName = "data/mlb_nl_2011.txt";
		Scanner s = null;
		try {
			s = new Scanner(new File(fileName));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		Team teams[] = new Team[16];

		//TODO: read in and process the data file, create teams and add them to the array
		int count=0;
		while ( s.hasNext() ) {
			String line = s.nextLine();
			String tokens[] = line.split(" ");
			//System.out.println( Integer.parseInt(baseball[2]));
			String name = tokens[0];
			int wins = Integer.parseInt(tokens[1]);
			int loss = Integer.parseInt(tokens[2]);
			
			Team team = new Team( name, wins, loss );
			teams[count]=team;
			count++;
			
		}

		
		
		
		System.out.println("Teams: ");
		for(Team t : teams) {
			System.out.println(t);
		}

		Arrays.sort(teams, new Comparator<Team>() {
			@Override
			public int compare(Team a, Team b) {
				return b.getWinPercentage().compareTo(a.getWinPercentage());
			}
			
		});
		
		System.out.println("\n\nSorted Teams: ");
		for(Team t : teams) {
			System.out.println(t);
		}
		
		//TODO: output the team array to a file as specified
		for (Team t: teams) {
			System.out.printf("%10s%6.2f\n", t.getName(), t.getWinPercentage()*100 );
		}
		
		String output = null;
		
		
		//File f = new File("data/mlb_nl_2011_results.txt");
		//PrintWriter pw = new PrintWriter(f);
		
		try {
			PrintWriter out = new PrintWriter("data/mlb_nl_2011_results.txt");
			for (Team t: teams) {
				out.printf("%10s%6.2f\n", t.getName(), t.getWinPercentage()*100 );
			}
			
			out.close();
		} catch (FileNotFoundException fnfe) {
			fnfe.printStackTrace();
		}
	}
	
}
