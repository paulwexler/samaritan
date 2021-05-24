from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    published = models.CharField(max_length=10)
    objects = models.Manager()

    class Meta:
        unique_together = (('author', 'title', 'published'))

    def __str__(self):
        return (
            f'{self.id}'
            f' {self.title}'
            f' {self.author}'
            f' {self.image}'
            f' {self.description[:10]}'
            f' {self.published}')

class Review(models.Model):
    book = models.ForeignKey(
            Book,
            on_delete=models.PROTECT)
    review = models.TextField()
