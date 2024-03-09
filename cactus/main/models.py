from django.db import models
from django.contrib.auth.forms import AuthenticationForm


class Categories(models.Model):
    name = models.CharField(max_length = 150 , unique=True)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class products(models.Model):
    name = models.CharField(max_length = 150 , unique=True)
    text = models.CharField(max_length = 200)


# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = User
    # 15.6-1 весрия postgreSQL