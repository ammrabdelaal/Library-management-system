Feature: Delete a book
  As a user
  I want to delete a book from the library
  So that I can remove books that are no longer needed

  Scenario: Deleting a book
    Given a book titled "Clean Code" exists
    When I delete the book
    Then the book should not exist in the system
