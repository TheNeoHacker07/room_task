from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ApartmentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apart_user', blank=True)
    name = models.CharField(max_length=20)
    uniq_number_room = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    free_place_count = models.IntegerField()
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    

class MyRentsModel(models.Model):
    aparments = models.ForeignKey(ApartmentModel, related_name='apartment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, blank=True)
    rent_start = models.DateField(auto_now_add=True)
    rent_end = models.DateField()


    def __str__(self):
        return self.aparments