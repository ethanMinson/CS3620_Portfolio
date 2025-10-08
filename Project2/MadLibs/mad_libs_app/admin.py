from django.contrib import admin

from mad_libs_app.models import FinishedStory
from mad_libs_app.models import Madlib

# Register your models here.
admin.site.register(FinishedStory)
admin.site.register(Madlib)