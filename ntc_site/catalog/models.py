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

class Product(BaseModel):
    title = models.CharField(
        verbose_name='Название',
        max_length=120
    )
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(
        verbose_name='Фото',
        blank=True,
        upload_to='catalog_images'
    )
    
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title