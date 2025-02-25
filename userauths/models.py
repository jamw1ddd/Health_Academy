from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPE = (
    ("Doctor","Доктор"),
    ("Patient","Пациент"),
)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,blank=True,null=True)
    user_type = models.CharField(max_length=50,choices=USER_TYPE,blank=True,null=True,default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def save(self,*args, **kwargs):
        email_username, _ = self.email.split('@')
        if self.username is None or self.username == "":
            self.username = email_username
        super(User,self).save(*args, **kwargs)