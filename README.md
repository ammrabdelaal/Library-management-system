# 📚 Library Management System

A simple Django web application for managing a library using **Behavior-Driven Development (BDD)** principles.

---

## 🚀 Features

- ✅ Add a book  
- ✅ Update book details  
- ✅ Delete a book  
- ✅ Store book data (title, author, published date, ISBN, available status)  
- ✅ Test all features using BDD scenarios

---

## 🧪 Behavior-Driven Development (BDD)

This project uses [Behave](https://github.com/behave/behave) with `behave-django` to write and run test scenarios using **Gherkin syntax**.

You can run the BDD tests using:
python manage.py behave --no-capture



Tech stack:
Python 3.x

Django

SQLite

Behave

behave-django

###postman
You can test the app using Postman:

Add a book
POST http://127.0.0.1:8000/books

Body type: raw (json)

       { 
        "title": "New book",
        "author": "amr",
        "published_date": "2000-04-08",
        "isbn": "123",
        "available": true
       }

Update a book
put http://127.0.0.1:8000/books/<id>/
(Same fields as above)

Delete a book
Delete http://127.0.0.1:8000/books/<id>/

Books list
GET http://127.0.0.1:8000/books



