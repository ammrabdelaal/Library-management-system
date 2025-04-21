from behave import given, when, then
from app.models import Book

@given('a book titled "1984" by "George Orwell" with ISBN "1234567890123" exists')
def step_impl(context):
    Book.objects.create(
        title="1984",
        author="George Orwell",
        published_date="1949-06-08",
        isbn="1234567890123",
        available=True
    )

@when('I update the author to "Eric Arthur Blair"')
def step_impl(context):
    book = Book.objects.get(title="1984")
    book.author = "Eric Arthur Blair"
    book.save()

@then('the book should have "Eric Arthur Blair" as the author')
def step_impl(context):
    book = Book.objects.get(title="1984")
    assert book.author == "Eric Arthur Blair"
