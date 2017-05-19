from django.db import models

__all__ = [
    'Category'
]


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def article_count(self):
        return self.article_set.all().count()
