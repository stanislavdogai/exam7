from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice, Answer

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)