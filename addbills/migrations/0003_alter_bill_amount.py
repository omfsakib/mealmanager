# Generated by Django 3.2 on 2021-04-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addbills', '0002_auto_20210428_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
