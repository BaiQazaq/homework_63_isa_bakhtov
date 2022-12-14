# Generated by Django 4.1.2 on 2022-10-31 11:50

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='account',
            name='liked_posts',
            field=models.ManyToManyField(related_name='user_likes', to='posts.post', verbose_name='Понравившиеся публикации'),
        ),
        migrations.AddField(
            model_name='account',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]
