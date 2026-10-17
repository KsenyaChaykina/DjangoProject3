from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок"
    )

    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое"
    )

    image = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )

    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров"
    )

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ['-created_at']  # Сначала новые

    def __str__(self):
        return self.title
