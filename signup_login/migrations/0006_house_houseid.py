# Generated by Django 4.1.2 on 2023-07-21 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login', '0005_house_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='houseid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
