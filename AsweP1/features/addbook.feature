Feature: Add a book
  As a user
  I want to add a book to the system
  So that I can keep track of my library

  Scenario: Adding a new book
    Given I am on the add book page
    When I enter "The Alchemist" by "Paulo Coelho" published on "1988-01-01" with ISBN "9780061122415" and submit
    Then I should see "The Alchemist" in the list of books
