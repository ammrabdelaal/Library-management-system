from behave import given, when, then
from django.test import Client
from app.models import Book

client = Client()

@given('I am on the add book page')
def step_impl(context):
    context.response = client.get('/book/new/')

@when('I enter "The Alchemist" by "Paulo Coelho" published on "1988-01-01" with ISBN "9780061122415" and submit')
def step_impl(context):
    context.response = client.post('/book/new/', {
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'published_date': '1988-01-01',
        'isbn': '9780061122415',
        'available': 'True'
    })

@then('I should see "The Alchemist" in the list of books')
def step_impl(context):
    assert Book.objects.filter(title="The Alchemist").exists()
