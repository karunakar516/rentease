# Generated by Django 4.1.2 on 2023-07-21 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login', '0004_current_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='userid',
            field=models.CharField(default=0, max_length=264),
            preserve_default=False,
        ),
    ]