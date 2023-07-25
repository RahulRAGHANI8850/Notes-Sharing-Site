from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# signUp model 
class signUp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact=models.CharField(max_length=10,null=True)
    branch=models.CharField(max_length=30)
    role=models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
    


# notes model
class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploadDate=models.DateField()
    branch=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    NotesFile=models.FileField(upload_to="docs")   
    type=models.CharField(max_length=30)
    Decription=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username+"   "+self.status
