from behave import given, when, then
from app.models import Book

@given('a book titled "Clean Code" exists')
def step_impl(context):
    Book.objects.create(
        title="Clean Code",
        author="Robert C. Martin",
        published_date="2008-08-01",
        isbn="9876543210987",
        available=True
    )

@when('I delete the book')
def step_impl(context):
    book = Book.objects.get(title="Clean Code")
    book.delete()

@then('the book should not exist in the system')
def step_impl(context):
    assert not Book.objects.filter(title="Clean Code").exists()
