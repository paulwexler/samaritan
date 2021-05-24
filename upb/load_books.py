"""
This program inserts the results of the google API request
for Michael Crighton into the review_book table.
"""
import os

import requests

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upb.settings')
get_wsgi_application()

from review.models import Book # pylint: disable=wrong-import-position

class BookLoader:
    """
    Load the review_book table.
    """
    url = (
            'https://www.googleapis.com/'
            'books/v1/volumes?'
            'q=michael%20crighton&amp;'
            'key=AIzaSyB6Z5mdvSohshY0VhrRoKkD')

    def load_table(self):
        """
        load the Book table
        """
        count = 0
        rsp = requests.get(self.url)
        if rsp.ok:
            data = rsp.json()
            for item in data['items']:
                self.save_book(item['volumeInfo'])
                count += 1
            print(f'Inserted {count} books.')
        else:
            raise RuntimeError(
                    f'Unable to get.'
                    f' url={self.url}'
                    f' status_code={rsp.status_code}'
                    f' reason={rsp.reason}')

    @staticmethod
    def save_book(volume_info):
        """
        save a single book derived from `volume_info`
        """
        book = Book(
                title=volume_info['title'],
                author=volume_info['authors'][0],
                image=volume_info['imageLinks']['smallThumbnail'],
                description=volume_info['description'],
                published=volume_info['publishedDate'])
        try:
            book.save()
        except Exception as exc: # pylint: disable=broad-except
            raise RuntimeError(f'Unable to save {book}') from exc

if __name__ == '__main__':
    BookLoader().load_table()
