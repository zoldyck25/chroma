# Generated by Django 3.2.8 on 2021-11-14 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0015_polls_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polls',
            name='likes',
        ),
        migrations.AddField(
            model_name='polls',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='Like', max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.polls')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
