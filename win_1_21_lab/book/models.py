from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.IntegerField()
    created_date_book = models.DateField(null=True)

    def __str__(self):
        return self.title
