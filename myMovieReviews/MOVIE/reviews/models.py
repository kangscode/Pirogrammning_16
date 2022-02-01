from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    year = models.IntegerField(verbose_name='개봉년도')
    genre = models.CharField(verbose_name='장르', max_length=50)
    rating = models.CharField(verbose_name='별점', max_length=10)
    runningTime = models.IntegerField(verbose_name='러닝타임')
    review = models.TextField(verbose_name='리뷰')
    director = models.CharField(verbose_name='감독', max_length=50)
    actor = models.CharField(verbose_name='배우', max_length=100)

    def __str__(self):
        return self.title