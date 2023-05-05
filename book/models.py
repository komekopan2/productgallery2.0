from django.db import models
from .consts import MAX_RATE
# Create your models here.


# class SampleModel(models.Model):
#     title = models.CharField(max_length=100)
#     number = models.IntegerField()
CATEGORY = (("web", "web"), ("mobile", "mobile"),
            ("xr", "XR"), ("game", "game"), ("other", "other"))

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE+1)]


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY
    )
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    # class Meta:
    #     verbose_name_plural = "Book"

    def __str__(self):
        # selfはインスタンスのこと
        return self.title  # title = models.CharField(max_length=100)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name_plural = "Book"

    def __str__(self):
        return self.title
