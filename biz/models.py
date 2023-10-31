from django.db import models

# Create your models here.
class Davinci002_Query_Log(models.Model):
    pre_prompt = models.CharField()
    prompt = models.CharField()
    post_prompt = models.CharField()
    response = models.CharField(null=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.response