# Generated by Django 2.2.5 on 2019-09-29 14:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restapi', '0004_movie_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('user', 'name')},
        ),
    ]
