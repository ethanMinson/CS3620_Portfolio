from django.contrib import admin

from .contactForm import ContactForm
from .models import Hobbies
from .models import Portfolio
from .models import Contact

admin.site.register(Hobbies)
admin.site.register(Portfolio)
admin.site.register(Contact)
# Register your models here.
