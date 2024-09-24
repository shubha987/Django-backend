from django.db import models

# Create your models here.
class News(models.Model):
    heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    article_text = models.TextField()

    def __str__(self):
        return self.heading