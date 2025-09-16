from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class News(BaseModel):
    title = models.CharField(
        verbose_name='Название',
        max_length=120
    )
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(
        verbose_name='Фото',
        blank=True,
        upload_to='homepage_images'
    )
    
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
    


