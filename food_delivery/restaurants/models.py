from django.db import models

# Create your models here.
class Cuisine(models.Model):

    CUISINE_CHOICES = [
        ('Thai','Thai'),
        ('Chinese','Chinese'),
        ('Japanese','Japanese'),
        ('Italian','Italian'),
        ('Mexican','Mexican'),
        ('TexMex','Tex-Mex'),
        ('Greek','Greek'),
        ('Pizza','Pizza'),
        ('Burger','Burger'),
        ('Fast-Food','Fast-Food'),
        ('Desserts','Desserts'),
        ('Indian','Indian'),
        ('Vegan','Vegan'),
        ('Breakfast','Breakfast'),
        ('Sandwiches','Sandwiches'),
        ('Gourmet','Gourmet'),
        ('Ice Cream','Ice Cream')
    ]

    cuisine_name = models.CharField(max_length=16,choices=CUISINE_CHOICES)

    def __str__(self):
        return f'{self.cuisine_name}'

class Restaurant(models.Model):

    time = [
        ('00','12 AM'),
        ('01','1 AM'),
        ('02','2 AM'),
        ('03','3 AM'),
        ('04','4 AM'),
        ('05','5 AM'),
        ('06','6 AM'),
        ('07','7 AM'),
        ('08','8 AM'),
        ('09','9 AM'),
        ('10','10 AM'),
        ('11','11 AM'),
        ('12','12 PM'),
        ('13','1 PM'),
        ('14','2 PM'),
        ('15','3 PM'),
        ('16','4 PM'),
        ('17','5 PM'),
        ('18','6 PM'),
        ('19','7 PM'),
        ('20','8 PM'),
        ('21','9 PM'),
        ('22','10 PM'),
        ('23','11 PM'),
    ]

    restaurant_name = models.CharField(max_length=128)
    opening_time = models.CharField(max_length=4,choices=time)
    closing_time = models.CharField(max_length=4,choices=time)
    restaurant_avg_rating = models.FloatField()
    restaurant_rated_by_number = models.FloatField()
    cuisines = models.ManyToManyField(Cuisine)
    photo = models.ImageField()
    avg_cost_for2 = models.IntegerField()

    def __str__(self):
        return f'{self.restaurant_name}'

class Address(models.Model):

    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    pin = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurant,related_name="address",on_delete=models.CASCADE)

class Dish(models.Model):
    dish_name = models.CharField(max_length=128)
    dish_description = models.CharField(max_length=1024)
    dish_cuisine = models.ManyToManyField(Cuisine)
    dish_price = models.FloatField()
    dish_restaurant = models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
    ordered_number = models.IntegerField()
    dish_avg_rating = models.FloatField()
    dishes_rated_by_number = models.FloatField()