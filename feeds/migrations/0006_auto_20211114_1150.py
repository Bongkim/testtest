# Generated by Django 3.2.7 on 2021-11-14 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0005_comment_parent_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_comments', through='feeds.CommentLike', to=settings.AUTH_USER_MODEL),
        ),
    ]