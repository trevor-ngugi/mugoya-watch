from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    neighborhood_name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    house_number =  models.IntegerField(default=0)
    #admin foreging key

    def __str__(self):
        return self.neighborhood_name




class Profile(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    username = models.CharField(max_length =30)
    identification_card =  models.IntegerField(default=0)
    neighborhood = models.ForeignKey(Neighbourhood)
    bio = models.TextField()
    email = models.EmailField()
    contact =  models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Business(models.Model):
    business_name = models.CharField(max_length =30)
    business_descrpition = models.TextField()
    user = models.ForeignKey(Profile)
    neighborhood = models.ForeignKey(Neighbourhood)
    business_email = models.EmailField()

    def __str__(self):
        return self.business_name



