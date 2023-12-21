from django.db import models
from core.models import CustomUser
from internship.models import Item
User = CustomUser()
# Create your models here.
def upload_resume(instance, filename):
    return f"resumes/{instance.name}_{filename}"

class NewRequestModel(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=254)
    major=models.CharField(max_length=250)
    phone=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    resume=models.FileField(upload_to=None, max_length=100)
    on_hold=models.BooleanField(default=True)
    is_accepted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    #to add the creator and delete te model once the creator deleted
    requested_by=models.ForeignKey(User, related_name='request',on_delete=models.CASCADE)    
    #same thing for the category
    # requested_to=models.ForeignKey(Item, related_name='request', on_delete=models.CASCADE)

    class Meta :
        ordering=('name',) 
    def __str__(self):
        return self.name