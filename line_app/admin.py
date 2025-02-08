from django.contrib import admin

# Register your models here.
from line_app.models import Performer,Type,Film,File
 
# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    # 指定要显示的属性
    list_display = ["id", "film_name", "performer", "film_type", "time", "film_url", "desc"]
admin.site.register(Performer)
admin.site.register(Type)
admin.site.register(Film,FilmAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display = ['id','upload_file','processed_file']

admin.site.register(File,FileAdmin)
