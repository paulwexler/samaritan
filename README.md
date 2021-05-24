# samaritan

Code Challange.

The Django project is *upb*, the Django is app is *review*.

Install Django==3.0, sqlite3, requests.

    cd samaritan/upb
    python3 manage.py migrate
    python3 load_books.py # load the review_book table; do this only once.
    python3 manage.py runserver

Then point your browser to: *localhost:8000/review/*

