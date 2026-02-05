from django.db import models

# The Author model stores basic information about a writer.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The Book model stores title and year, linked to an Author via a ForeignKey.
# This establishes a one-to-many relationship (One Author -> Many Books).
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title