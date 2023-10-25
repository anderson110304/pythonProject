from django.db import models


class Book(models.Model):
    GENRE = (
        ('Роман', 'Роман'),
        ('Детектив', 'Детектив'),
        ('Фэнтези', 'Фэнтези'),
        ('Научная фантастика', 'Научная фантастика'),
        ('Документальная литература', 'Документальная литература'),
    )
    genre = models.CharField(max_length=100, choices=GENRE, default=GENRE[0], null=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.IntegerField()
    created_date_book = models.DateField(null=True)

    def __str__(self):
        return self.title
