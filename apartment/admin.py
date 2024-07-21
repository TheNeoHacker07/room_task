from django.contrib import admin
from .models import ApartmentModel, MyRentsModel

admin.site.register(ApartmentModel)
admin.site.register(MyRentsModel)