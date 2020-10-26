from django.contrib import admin
from .models import File
from .models import Recipe


admin.site.site_header = "Bewoc Foods Co."
admin.site.site_title = "Bewoc Admin Portal"
admin.site.index_title = "Welcome to Bewoc Foods Administration"

admin.site.register(File)
admin.site.register(Recipe)
