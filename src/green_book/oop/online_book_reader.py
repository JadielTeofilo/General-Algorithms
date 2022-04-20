"""
Online Book Reader: Design the data structures for an online book reader system.


who is going to be able so publish a book to be sold

what kinds of books will it have

is it going to be free
    is there a subscription kind of service
    

where are the books coming from 

What formats will it support

will it allow highlights


BookReader
    has books
    has users
    has readings

    search_book()
    start_reading_book(user, book)

Book
    has pages
    

User
    has (or not) a membership

    create_membership()

Membership
    has an end_date
    

Page
    has text
Reading
    has highlights
    has page
    has book
    has user

    
-----------
Takeaways


When there is going to be a lot of responsability for the main Domain class, break those in other classes:
    BookReader will have - Library, UserManager, Display classes

This case can be identified when the desired system is a full web service


Display class
    Used to manage the view of the book pages
    has book, page
    has go_to_page, got_to_next
        




"""
