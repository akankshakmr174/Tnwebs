from django.contrib import admin
from blog.models import Post

class TinyMCEAdmin(admin.ModelAdmin):
	class Media:
		js = ('/static/admin/js/tiny_mce/tiny_mce.js', '/static/admin/js/tiny_mce/textareas.js',)

admin.site.register(Post, TinyMCEAdmin)

