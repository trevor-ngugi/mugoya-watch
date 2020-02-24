from django.contrib import admin
from .models import Profile,Neighbourhood,Posts,Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Posts)
admin.site.register(Business)
