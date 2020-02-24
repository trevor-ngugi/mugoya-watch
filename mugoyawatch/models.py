from django.db import models

# Create your models here.




class Profile(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    username = models.CharField(max_length =30)
    identification_card =  models.IntegerField(default=0)
    neighborhood = models.CharField(max_length =30)#foreign key
    bio = models.TextField()
    email = models.EmailField()
    contact =  models.IntegerField(default=0)


class Business(models.Model):
    business_name = models.CharField(max_length =30)
    business_descrpition = models.TextField()
    user = models.CharField(max_length =30)#foreign key
    neighborhood = models.CharField(max_length =30)#foreign key
    business_email = models.EmailField()


class Neighbourhood(models.Model):
    neighborhood_name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    house_number =  models.IntegerField(default=0)
    #admin foreging key
