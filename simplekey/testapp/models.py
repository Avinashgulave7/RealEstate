from django.db import models

from django.contrib.auth.models import User
from .validators import (
         validate_phonenumber)


# Create your models here.

class Buy(models.Model):
    Property_Choice=(('','Select'),('residential','Residential'),('commercial','commercial'))
    Type_Choice = (('','Select'),('flat', 'Flat'), ('bunglow', 'Bunglow'),('shop', 'Shop'),('office', 'Office'))
    Water_Choice=(('','Select'),('24/7','24/7'),('morning','Morning'),('night','Night'))
    Playground_Choice=(('','Select'),('Yes','Yes'),('No','No'),('in_future','In_Future'))
    Gym_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Hospital_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Mall_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    School_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Electricity_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'))
    Cinema_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Club_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Wifi_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Fire_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Lift_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'))
    Parking_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Security_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Temple_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Poll_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Living_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Hotel_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))

    Owner_name = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='Owner_name1')
    Contact=models.CharField(max_length= 15, validators= [validate_phonenumber])
    Property_name=models.CharField(max_length=40)
    Property=models.CharField(max_length=20,choices=Property_Choice,default='select')
    Type=models.CharField(max_length=20,choices=Type_Choice,default='select')
    Rooms=models.IntegerField()
    Baths=models.IntegerField()
    Area=models.IntegerField()
    Water=models.CharField(max_length=20,choices=Water_Choice,default='select')
    Playground=models.CharField(max_length=20,choices=Playground_Choice,default='select')
    Price=models.IntegerField()
    Description=models.TextField()
    Gym=models.CharField(max_length=20,choices=Gym_Choice,default='select')
    Hospital=models.CharField(max_length=20,choices=Hospital_Choice,default='select')
    School=models.CharField(max_length=20,choices=School_Choice,default='select')
    Mall=models.CharField(max_length=20,choices=Mall_Choice,default='select')
    Pincode=models.IntegerField()
    State=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Address=models.TextField()
    Img1=models.ImageField(upload_to='img/')

    Electricity=models.CharField(max_length=20,choices=Electricity_Choice,default='select')
    Parking=models.CharField(max_length=20,choices=Parking_Choice,default='select')
    Club=models.CharField(max_length=20,choices=Club_Choice,default='select')
    Fire=models.CharField(max_length=20,choices=Fire_Choice,default='select')
    Lift=models.CharField(max_length=20,choices=Lift_Choice,default='select')
    Wifi=models.CharField(max_length=20,choices=Wifi_Choice,default='select')
    Security=models.CharField(max_length=20,choices=Security_Choice,default='select')
    Temple=models.CharField(max_length=20,choices=Temple_Choice,default='select')
    Poll=models.CharField(max_length=20,choices=Poll_Choice,default='select')
    Living=models.CharField(max_length=20,choices=Living_Choice,default='select')
    Hotel=models.CharField(max_length=20,choices=Hotel_Choice,default='select')
    Cinema=models.CharField(max_length=20,choices=Cinema_Choice,default='select')
    Date=models.DateField()

class BuyImage(models.Model):
    buy = models.ForeignKey(Buy,default=None, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField()





class Rent(models.Model):
    Property_Choice=(('','Select'),('residential','Residential'),('commercial','commercial'))
    Type_Choice = (('','Select'),('flat', 'Flat'), ('bunglow', 'Bunglow'),('shop', 'Shop'),('office', 'Office'))
    Water_Choice=(('','Select'),('24/7','24/7'),('morning','Morning'),('night','Night'))
    Playground_Choice=(('','Select'),('Yes','Yes'),('No','No'),('in_future','In_Future'))
    Gym_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Hospital_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Mall_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    School_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Electricity_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'))
    Cinema_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Club_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Wifi_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Fire_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Lift_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'))
    Parking_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Security_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Temple_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Poll_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Living_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))
    Hotel_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'), ('in_future', 'In_Future'))

    Owner_name=models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='Owner_name')
    Contact = models.CharField(max_length=15, validators=[validate_phonenumber])
    Property_name=models.CharField(max_length=40)
    Property=models.CharField(max_length=20,choices=Property_Choice,default='select')
    Type=models.CharField(max_length=20,choices=Type_Choice,default='select')
    Rooms=models.IntegerField()
    Baths=models.IntegerField()
    Area=models.IntegerField()
    Water=models.CharField(max_length=20,choices=Water_Choice,default='select')
    Playground=models.CharField(max_length=20,choices=Playground_Choice,default='select')
    Price=models.IntegerField()
    Description=models.TextField()
    Gym=models.CharField(max_length=20,choices=Gym_Choice,default='select')
    Hospital=models.CharField(max_length=20,choices=Hospital_Choice,default='select')
    School=models.CharField(max_length=20,choices=School_Choice,default='select')
    Mall=models.CharField(max_length=20,choices=Mall_Choice,default='select')
    Pincode=models.IntegerField()
    State=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Address=models.TextField()
    Img1=models.ImageField(upload_to='img/')

    Electricity=models.CharField(max_length=20,choices=Electricity_Choice,default='select')
    Parking=models.CharField(max_length=20,choices=Parking_Choice,default='select')
    Club=models.CharField(max_length=20,choices=Club_Choice,default='select')
    Fire=models.CharField(max_length=20,choices=Fire_Choice,default='select')
    Lift=models.CharField(max_length=20,choices=Lift_Choice,default='select')
    Wifi=models.CharField(max_length=20,choices=Wifi_Choice,default='select')
    Security=models.CharField(max_length=20,choices=Security_Choice,default='select')
    Temple=models.CharField(max_length=20,choices=Temple_Choice,default='select')
    Poll=models.CharField(max_length=20,choices=Poll_Choice,default='select')
    Living=models.CharField(max_length=20,choices=Living_Choice,default='select')
    Hotel=models.CharField(max_length=20,choices=Hotel_Choice,default='select')
    Cinema=models.CharField(max_length=20,choices=Cinema_Choice,default='select')
    Date=models.DateField()


class RentImage(models.Model):
    rent = models.ForeignKey(Rent,default=None, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField()

class Land(models.Model):
    Property_Choice=(('','Select'),('private','Private'),('government','Government'))
    Property_type_Choice = (('','Select'),('residential', 'Residential'), ('commercial', 'commercial'),('forest', 'Forest'),('garden', 'Garden'),('appartments', 'Appartments'),('other', 'other'))
    Document_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'))
    Survey_Sketch_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'))
    Tax_Raciept_Choice = (('','Select'),('Yes', 'Yes'), ('No', 'No'))

    Owner_name = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='Owner_name2')
    Contact = models.CharField(max_length=15, validators=[validate_phonenumber])
    Property=models.CharField(max_length=20,choices=Property_Choice,default='select')
    Property_type=models.CharField(max_length=20,choices=Property_type_Choice,default='select')
    Price=models.IntegerField()
    Area=models.IntegerField()
    Description=models.TextField()
    Document=models.CharField(max_length=20,choices=Document_Choice,default='select')
    Tax_Raciept=models.CharField(max_length=20,choices=Tax_Raciept_Choice,default='select')
    Survey_Sketch=models.CharField(max_length=20,choices=Survey_Sketch_Choice,default='select')
    Pincode=models.IntegerField()
    State=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Address=models.TextField()
    Img1=models.ImageField(upload_to='img/')
    Date=models.DateField()

class LandImage(models.Model):
    land = models.ForeignKey(Land,default=None, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField()


class Agent(models.Model):
    Agent_type_choice=(('','Select'),('buy_Agent','Buy_Agent'),('rent_Agent','Rent_Agent'),('land_Agent','Land_Agent'))
    Agent_name=models.CharField(max_length=20)
    Contact = models.CharField(max_length=15, validators=[validate_phonenumber])
    Email=models.EmailField()
    Agent_type=models.CharField(max_length=10,choices=Agent_type_choice,default='select')
    Img1=models.ImageField(upload_to='img/')


class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

class Select_Property(models.Model):
    Appointment = models.DateTimeField(null=True)
    Agent=models.ForeignKey(Agent,on_delete=models.CASCADE,related_name='agent',default=None,null=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.IntegerField()
    date=models.DateField()
    property=models.CharField(max_length=100)
    msg=models.TextField()

    def __str__(self):
        return self.name