from django.db import models

# Create your models here.
class Devtool(models.Model):
    name = models.CharField(verbose_name='이름', max_length=50)
    kind = models.CharField(verbose_name='종류', max_length=100)
    description = models.TextField(verbose_name='설명')

    def __str__(self):
        return self.name

class Idea(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    image = models.ImageField(upload_to="poster", null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    interest = models.IntegerField(verbose_name='관심도')
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
