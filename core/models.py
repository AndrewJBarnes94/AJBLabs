from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class ProjectField(models.Model):
    field = models.CharField(max_length=200)

    def __str__(self):
        return self.field

class Project(models.Model):
    field = models.ForeignKey(ProjectField, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    code_zip = models.FileField(upload_to='media/portfolio_code_zipped/')

    def __str__(self):
        return self.title
    
