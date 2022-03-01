from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=250, allow_unicode=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass

class FeedBack(models.Model):
    name = models.CharField(max_length=40, verbose_name='')
    phone = models.CharField(max_length=40, verbose_name='')

    def __str__(self):
        return self.phone