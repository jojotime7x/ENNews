from django.db import models

class FavoriteArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=500)
    url_to_image = models.URLField(max_length=500)

    def __str__(self):
        return self.title
