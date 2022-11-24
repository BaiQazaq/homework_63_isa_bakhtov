from django.db.models import TextChoices
from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

class GenderChoices(TextChoices):
    MAEL = 'male', 'мужчина'
    FEMALE = 'female', 'женшина'


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars/',
        verbose_name='Аватар'
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    
    liked_posts = models.ManyToManyField(
        verbose_name='Понравившиеся публикации',
        to='posts.Post',
        related_name='user_likes',
        blank=True
    )
    subscriptions = models.ManyToManyField(
        verbose_name='Подписки',
        to='accounts.Account',
        related_name='subscribers',
        blank=True
    )
    commented_posts = models.ManyToManyField(
        verbose_name='Прокомментированные публикации',
        to='posts.Post',
        related_name='user_comments',
        blank=True
    )
    user_info = models.CharField(
        verbose_name='Информация о пользователе',
        null=True,
        blank=True,
        max_length=200
    )
    phone_num = models.IntegerField(
        verbose_name = 'Номер телефона',
        null=True,
        blank=True,
        default=None
    )
    gender = models.CharField(
        verbose_name='Пол',
        choices=GenderChoices.choices,
        max_length=100,
        default='Gender did not choose')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
