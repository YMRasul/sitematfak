from django.db import models
from django.urls import reverse

from PIL import Image
from django_resized import ResizedImageField
from django.core.validators import FileExtensionValidator

# Здесь мы определим модели
class photo(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")  # ,второй аргумент используется Админ панеле
    content = models.TextField(blank=True,verbose_name="Контент")  # ,второй аргумент используется Админ панеле
    #photo = models.ImageField(upload_to="photos/%Y/%m",verbose_name="Фото")

    photo = ResizedImageField(size=[1000, 1000], upload_to="photos/%Y/%m", blank=True, null=True,verbose_name="Фото")
    # ResizedImageField Изменение до сохранение

    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True,verbose_name="Время Изменения")
    cat = models.ForeignKey('categ',on_delete=models.PROTECT,null=True,verbose_name="Категория")
    # для ImageField необходимо определит и настроит  MEDIA_ROOT и MEDIA_URL
    def __str__(self):
        return self.title
    #--------------------------
    '''
    def save(self):
        # переопределение метода save()  
        # изменеия размера после сохранения
        super().save()
        img = Image.open(self.photo.path)
        # чтение сохраненного изображение
        raz = 1000
        print(self.photo.path,img.height,img.width,raz)
        if img.height > raz or img.width > raz:
           output_size = (raz, raz)
           img.thumbnail(output_size)
           img.save(self.photo.path) # сохранит заново
    '''
    #--------------------------

    def get_absolute_url(self):                                # Админ панеле появится
        return reverse('post',kwargs={'post_id': self.pk})     #  кнопка 'смотреть на сайте'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии' # Множественное число
        ordering = ['time_create', 'title']

class categ(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name="Категория")  # ,второй аргумент используется Админ панеле

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #print(reverse('category', kwargs={'cat_id': self.pk}))
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'   # Множественное число
        ordering = ['id']
#-----------------------------------------------------------------------
class first(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")  # ,второй аргумент используется Админ панеле
    content = models.TextField(blank=True,verbose_name="Контент")  # ,второй аргумент используется Админ панеле
    #photo = models.ImageField(upload_to="photos",verbose_name="Фото")

    photo = ResizedImageField(size=[1000, 1000], upload_to="photos", blank=True, null=True,verbose_name="Фото")
    # ResizedImageField Изменение до сохранение

    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True,verbose_name="Время Изменения")
    # для ImageField необходимо определит и настроит  MEDIA_ROOT и MEDIA_URL
    def __str__(self):
        return self.title

#    def get_absolute_url(self):                                # Админ панеле появится
#        return reverse('post',kwargs={'post_id': self.pk})     #  кнопка 'смотреть на сайте'

    class Meta:
        verbose_name = 'фотография главной страницы'
        verbose_name_plural = 'Фотография основной страницы' # Множественное число
