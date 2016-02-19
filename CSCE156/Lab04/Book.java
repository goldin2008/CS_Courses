package unl.cse.library;

import org.joda.time.DateTime;
import org.joda.time.Period;

public class Book {

    private String title;
    private String isbn;
    private Author author;
    private DateTime publishDate;
    
    ///////////////////////////////////
    // TO DO
    public int getYears() {
    	int years = new Period(this.publishDate, DateTime.now()).getYears();
    	return years;
	}
/// CONSTRUCTOR
	public Book(String title, Author author, String isbn, String publishdate) {	
    	setTitle(title);
    	setISBN(isbn);
    	setAuthor(author);
    	setPublishDate(publishdate);
    	
    }
    
    ////////////////////////////////////

    /**
     * Getter method for author
     * @return
     */
    public Author getAuthor() {
        return this.author;
    }

    /**
     * Setter method for authors
     * @param author
     */
    public void setAuthor(Author author) {
        this.author = author;
    }

    /**
     * Getter method for call number.
     * @return
     */
    public String getISBN() {
        return this.isbn;
    }

    /**
     * Setter method for call number.
     * @param callNumber
     */
    public void setISBN(String isbn) {
        this.isbn = isbn;
    }

    /**
     * Getter method for title
     * @return
     */
    public String getTitle() {
        return this.title;
    }

    /**
     * Setter method for title
     * @param title
     */
    public void setTitle(String title) {
        this.title = title;
    }

    public String getPublishDate() {
    	return this.publishDate.toString("YYYY");
    }
    
    public void setPublishDate(String date) {
    	this.publishDate = DateTime.parse(date);
    }
    
}
