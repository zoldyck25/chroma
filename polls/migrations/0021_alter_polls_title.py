# Generated by Django 3.2.8 on 2021-12-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='title',
            field=models.TextField(max_length=50),
        ),
    ]
