from django.contrib import admin
from .models import Post, PythonTutorial, DjangoGuide, DeveloperTool

admin.site.register(Post)
admin.site.register(PythonTutorial)
admin.site.register(DjangoGuide)
admin.site.register(DeveloperTool)
