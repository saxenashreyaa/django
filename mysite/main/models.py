from django.db import models
from datetime import datetime


# Create your models here.
class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=100)
    category_summary = models.CharField(max_length=100)
    category_slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/img', default=0)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=100)
    series_summary = models.CharField(max_length=100)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name= "Category", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=100)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default= datetime.now())

    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name= "Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=100, default=1)

    def __str__(self):
        return self.tutorial_title
