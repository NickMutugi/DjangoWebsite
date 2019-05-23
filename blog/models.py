from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name

class Contact1(models.Model):
    name1=models.CharField(max_length=200)
    email1=models.EmailField()
    message1=models.TextField()
    def __str__(self):
        return self.name1
