# Generated by Django 3.2.4 on 2021-07-12 20:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Politic',
            new_name='Post',
        ),
    ]
