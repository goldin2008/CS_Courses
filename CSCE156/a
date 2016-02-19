package unl.cse.labs.lab01;

import org.joda.time.DateTime;
import org.joda.time.Interval;
import org.joda.time.Period;

public class Birthday {

	public static void main(String args[]) {
		
		String name = "Java";
		
		int month = 5;
		int date  = 28;
		int year  = 1986;

		DateTime bday = new DateTime(year, month, date, 0, 0);
		DateTime today = new DateTime();

		Period age = new Period(bday, today);
		
		int years = age.getYears();
		int months = age.getMonths();
		int days = age.getWeeks() * 7 + age.getDays();

		DateTime next_bday = new DateTime(year + years + 1, month, date, 0, 0);
		Interval days_to_next_bday_i = new Interval(today, next_bday);
		double days_remaining = days_to_next_bday_i.toDurationMillis() / (1000 * 60 * 60 * 24) + 1;

		//TODO: write code to output results here
		System.out.println("Greetings, "+name+". Today you are "+years+", "+months+" months, and "+days+" days old.");
		
		if (days_remaining==365)
			System.out.println("Happy Birthday.");
		else
			System.out.println("Your friends have "+days_remaining+" shopping days until your next birthday.");
		
	}
}
