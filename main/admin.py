from django.contrib import admin
from .models import Projects, Contact, About, IndexImage
# Register your models here.

admin.site.register(Projects)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(IndexImage)