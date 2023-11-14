from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# вспомогательный клас для отображения в админ панеле полей  ('id', 'title', 'time_create', 'photo') #
# после определение этого класса его в 'admin.site.register(students)' добавим вторым аргументом
class photoAdmin(admin.ModelAdmin):  # students должень совпадат с модели 'students' а Admin для админ панели
    list_display = ('id', 'title','content', 'time_create', 'get_html_photo') # список полей
    list_display_links = ('id', 'title')                            # поля которые мы можем кликнут
    search_fields = ('title',)                                      # поля для поиска
    list_filter = ('time_create',)                                  # поля для фильтрации
    save_on_top = True                                              # если True  наверху повторится кнопки
    #x Это функция для отображения миниатюра на админ панеле в место пути
    #x в list_display вместо 'photo' пропишем 'get_html_photo'
    fields = ('title','content','cat','photo','get_html_photo','time_create')
    readonly_fields = ('time_create','get_html_photo')

    def get_html_photo(self,object):
        '''
        Возврашает HTML страницы Если существует путь к фотографии

        '''
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"

class categAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)

#   Эти регистрации для того чтобы модели нашего приложения видно было в Админ панеле (photo,categ)
#   второй параметр добавим после определение классов (photoAdmin,categAdmin)

#------------------------------------------------------------------------------------
class firstAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','content', 'time_create', 'get_html_photo') # список полей
    list_display_links = ('id', 'title')                            # поля которые мы можем кликнут
    save_on_top = True                                              # если True  наверху повторится кнопки
    #x Это функция для отображения миниатюра на админ панеле в место пути
    #x в list_display вместо 'photo' пропишем 'get_html_photo'
    fields = ('title','content','photo','get_html_photo','time_create')
    readonly_fields = ('time_create','get_html_photo')

    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"

#-------------------------------------------------------------------------------------
admin.site.register(photo, photoAdmin)  # photo да туриб  <Alt>+<Enter> ни боссак import чикади
admin.site.register(categ,categAdmin)
admin.site.register(first,firstAdmin)

admin.site.site_title = 'Админ панель сайта'                # из appmatfak82/templates/base_site.htm переопределили
admin.site.site_header = 'Админ панель сайта однакурсников' # site_title   и site_header

