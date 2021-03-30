from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def basic_validators(self, postData):
        errors = {}
        
        if len(postData['title'])<2:
            errors['title'] = 'Title should be greater than 2 characters'
        if len(postData ['network'])<3:
            errors['network'] = 'Network should be greater than 3 characters'
        if len(postData['description'])<10:
            errors['description'] = 'Description should be more than 10 character'
        return errors 
    

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = ShowManager()
    