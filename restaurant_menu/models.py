from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MEAL_TYPE = (
	("starters", "Starters"),
	("salads", "Salads"),
	("main_dishes", "Main Dishes"),
	("desserts", "Desserts"),
)

STATUS = (
	(0, "Unavailable"),
	(1, "Available"),
)

class Item(models.Model):
	meal = models.CharField(max_length=1000, unique=True)
	description = models.CharField(max_length=2000) # Ingredients
	price = models.DecimalField(max_digits=10, decimal_places=2)
	meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
	
	# Mention the chef
	# If on deletion of chef all dishes by chef are to be deleted
	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	# If we want to keep the dishes but remove the chef
	# author = models.ForeignKey(User, on_delete=models.SET_NULL)
	# If we want dishes not to be deleted, i.e. not deleting the chef
	author = models.ForeignKey(User, on_delete=models.PROTECT)
	
	status = models.IntegerField(choices=STATUS, default=0)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.meal