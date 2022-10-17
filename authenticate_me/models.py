
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_doctor = models.BooleanField( default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class User_reg(models.Model):
    user = models.OneToOneField('User',on_delete=models.CASCADE, primary_key=True)
    fname = models.CharField(max_length=50,blank=False)
    lname = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    address = models.TextField(max_length=500,blank=False)
    gender = models.CharField(max_length=7, blank=False)
    phone = models.CharField(max_length=12,unique=True,blank=False)
    Username = models.CharField(max_length=100,blank=False,unique=True)
    Userpassword = models.CharField(max_length=100,blank=False)
    

    def __str__(self):
        return self.fname

class dr_reg(models.Model):
    user = models.OneToOneField('User',on_delete=models.CASCADE, primary_key=True)
    fname = models.CharField(max_length=50,blank=False)
    lname = models.CharField(max_length=50,blank=False)
    image = models.ImageField(upload_to="profile",default="bman.jpg")
    specialisation = models.CharField(max_length=100,blank=False)
    qualificaton =  models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=12,blank=False,unique=True)
    gender = models.CharField(max_length=7,blank=False)
    address = models.TextField(max_length=500,blank=False)
    state =  models.CharField(max_length=50,blank=False)
    city = models.CharField(max_length=50,blank=False)
    zip = models.CharField(max_length=50,blank=False)   
    email = models.EmailField(max_length=50,blank=False)
    dUsername = models.CharField(max_length=100,blank=False,unique=True)
    dPassword = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.fname

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     avatar = models.ImageField(default='#', upload_to='profile_images')
#     bio = models.TextField()

#     def __str__(self):
#         return self.bio

#     def save(self, *args, **kwargs):
#         super().save()

#         img = Image.open(self.avatar.path)

#         if img.height > 100 or img.width > 100:
#             new_img = (100, 100)
#             img.thumbnail(new_img)
#             img.save(self.avatar.path)

from django.db import models
from django.utils import timezone
from .models import User

# Create your models here.
class Appointment(models.Model):

    department =(
    ('Dentistry',"Dentistry"),
    ('gynaecology',"gynaecology"),
    ('obstetrics',"obstetrics"),
    ('neurology',"neurology"),
    ('cardiology',"cardiology"),
    ('orthopaedics',"orthopaedics"),
    (' eye-care'," eye-care"), 
)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=100)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    hospital_name = models.CharField(max_length=100)
    department = models.CharField(choices=department, max_length=100)
    qualification_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

class BookAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    message = models.TextField()
    phone_number = models.CharField(max_length=120)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name