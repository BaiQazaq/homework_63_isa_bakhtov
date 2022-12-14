# Generated by Django 4.1.2 on 2022-11-24 16:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_like'),
        ('accounts', '0004_alter_account_avatar_alter_account_commented_posts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='commented_posts',
            field=models.ManyToManyField(blank=True, related_name='user_comments', to='posts.post', verbose_name='Прокомментированные публикации'),
        ),
        migrations.AlterField(
            model_name='account',
            name='liked_posts',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to='posts.post', verbose_name='Понравившиеся публикации'),
        ),
        migrations.AlterField(
            model_name='account',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]
