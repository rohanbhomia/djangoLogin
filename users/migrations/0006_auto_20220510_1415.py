# Generated by Django 3.1.5 on 2022-05-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.BigIntegerField(default=None, null=True),
        ),
    ]