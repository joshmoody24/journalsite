from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Entry(models.Model):
    date = models.DateField()
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    public = models.BooleanField()

    def __str__(self):
        return str(self.date)
