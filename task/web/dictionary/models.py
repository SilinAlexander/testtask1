from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def _str_(self):
        return self.title


class Word(models.Model):
    title = models.CharField(max_length=120)
    category = models.TextField()
    level = models.TextField()
    theme = models.TextField()
    stw = models.TextField()
    example = models.TextField()
    transcription = models.TextField()
    user = models.ForeignKey('User', related_name='words', on_delete=models.CASCADE)

    def _str_(self):
        return self.title