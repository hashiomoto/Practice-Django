from django.contrib import admin

# Register your models here.

from .models import Post # 追加

admin.site.register(Post) # 追加