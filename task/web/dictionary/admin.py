from django.contrib import admin

# Register your models here.
from .models import User,  Word

admin.site.register(Word)
admin.site.register(User)
