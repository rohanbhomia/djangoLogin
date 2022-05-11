from django.db import models
from users.models import CustomUser

# Create your models here.


class Todos(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.DO_NOTHING, db_column="user_id")
    created_on = models.DateTimeField(auto_now_add=True)
