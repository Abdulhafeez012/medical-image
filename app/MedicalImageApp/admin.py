from django.contrib import admin
from app.MedicalImageApp.models import *

admin.site.register(UserInformation)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalImage)
