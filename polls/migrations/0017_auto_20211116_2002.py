# Generated by Django 3.2.8 on 2021-11-16 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20211114_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polls',
            name='option_one',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='option_one_count',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='option_two',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='option_two_count',
        ),
    ]