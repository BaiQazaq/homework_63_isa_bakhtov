# Generated by Django 4.1.2 on 2022-10-31 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('accounts', '0002_alter_account_managers_account_changed_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='commented_posts',
            field=models.ManyToManyField(related_name='user_comments', to='posts.post', verbose_name='Прокомментированные публикации'),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('male', 'мужчина'), ('female', 'женшина')], default='Gender did not choose', max_length=100, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_num',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_info',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Информация о пользователе'),
        ),
    ]
