# Generated by Django 3.0.5 on 2020-04-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='plakat',
            field=models.ImageField(default=None, upload_to='plakaty'),
        ),
    ]