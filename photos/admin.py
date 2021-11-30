from django.contrib import admin

from .models import Editor,Article,tags
from .models import photos, Category,Location



# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags) 
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(photos)