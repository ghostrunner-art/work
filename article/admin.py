from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_time','readed_num','last_updated_time','is_deleted',)
    ordering = ('id',)

# Register your models here.
# admin.site.register(Article,ArticleAdmin)