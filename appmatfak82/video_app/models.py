from django.core.validators import FileExtensionValidator
from django.db import models
from django_resized import ResizedImageField

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #image = models.ImageField(upload_to='image/')

    #image = models.ImageField(upload_to="photos/%Y/%m",verbose_name="Фото")

    image = ResizedImageField(size=[200, 200], upload_to='image/', blank=True, null=True,verbose_name="Фото")
    # ResizedImageField Изменение до сохранение


    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
