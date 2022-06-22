# Generated by Django 3.2.8 on 2021-11-12 05:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0010_auto_20211112_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post_like',
            field=models.ManyToManyField(default=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
