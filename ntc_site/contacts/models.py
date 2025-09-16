from django.db import models

class Request(models.Model):
    first_name = models.CharField(
        max_length=120,
        verbose_name='Имя'
        )
    last_name = models.CharField(
        max_length=120,
        verbose_name='Фамилия',
        )
    email = models.CharField(
        max_length=120,
        verbose_name='e-mail',
    )
    phone_number = models.CharField(
        max_length=120,
        verbose_name='Номер телефона',
    )
    text = models.TextField(
        verbose_name='Текст обращения'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    class Meta:
        verbose_name = 'обращение'
        verbose_name_plural = 'Обращения'