from django.db import models

# Create your models here.
class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True)
    birth_year = models.IntegerField()

    def __str__(self):
        return f"Author (id={self.id}, last_name={self.last_name})"

class Book(models.Model):
    title = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book(id={self.id}, title={self.title}, author_id={self.author.id})"

    class Meta:
        ordering = ['author__last_name', 'title']
        verbose_name = "Book" # not necessary in this case because default is the model name and model + s
        verbose_name_plural = "Books"
        indexes = [
            models.Index(fields=['title', 'author'])
        ]