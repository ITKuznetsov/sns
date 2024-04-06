# Generated by Django 5.0.3 on 2024-04-06 08:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('comments', models.TextField(max_length=300, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('disliked_by', models.ManyToManyField(related_name='disliked_posts', to=settings.AUTH_USER_MODEL)),
                ('liked_by', models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
