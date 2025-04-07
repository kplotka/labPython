from django.contrib import admin
from .models import ModelProfile, DirectorProfile, CastingOffer, Application

admin.site.register(ModelProfile)
admin.site.register(DirectorProfile)
admin.site.register(CastingOffer)
admin.site.register(Application)