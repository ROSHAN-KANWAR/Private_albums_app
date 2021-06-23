from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    category=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.category

from django.core.exceptions import ValidationError

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

class Photo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='addphoto',validators=[validate_image],null=False,blank=False,help_text='Maximum file size allowed is 2Mb')
    dec=models.TextField(max_length=1000,null=False,blank=False)
