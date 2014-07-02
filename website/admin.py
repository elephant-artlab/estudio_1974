from django.contrib import admin
from .models import Session

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Session, SessionAdmin)
