from django.contrib import admin
from sodclan.forms import ArticleModelAdminForm
from sodclan.models import *
     
class ArticleAdmin(admin.ModelAdmin):
    	list_display = ('title', 'author', 'date',)
    	search_fields = ['title',]
    	date_hierarchy = 'date'
    	form = ArticleModelAdminForm
     
admin.site.register(Article, ArticleAdmin)


