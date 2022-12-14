from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices


class Post(models.Model):
    description = models.CharField(verbose_name='Описание', null=False, blank=False, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=False, upload_to='posts/')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)


class Comment(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='posts.Post', related_name='comments', null=False,
                             blank=False, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Текст', null=False, blank=False, max_length=200)
    # created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    # changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    # deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    # is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    
    def __str__(self):
        return self.text[:30]

class StatusChoices(TextChoices):
    LIKE = 'Like'
    DISLIKE = 'Dislike'


class Like(models.Model):
    mark = models.CharField(verbose_name='Mark', choices=StatusChoices.choices, max_length=100, default=StatusChoices.LIKE)
    liked_by = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='likes', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='posts.Post', related_name='likes', null=False,
                             blank=False, on_delete=models.CASCADE)
    



