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
    image = models.FileField(upload_to='', null=True)
    cost = models.IntegerField()
    created_date_book = models.DateField(null=True)

    def __str__(self):
        return self.title


class ReviewBook(models.Model):
    book_title = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book_title}"
