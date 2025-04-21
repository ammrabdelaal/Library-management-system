Feature: Update a book
  As a user
  I want to update a book's information
  So that I can correct or improve book details

  Scenario: Updating the author of a book
    Given a book titled "1984" by "George Orwell" with ISBN "1234567890123" exists
    When I update the author to "Eric Arthur Blair"
    Then the book should have "Eric Arthur Blair" as the author
