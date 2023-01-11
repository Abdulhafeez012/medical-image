from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'MedicalImageApp'

urlpatterns = [
                  path('', views.BaseView.as_view(), name='base'),
                  path('login/', views.LogInView.as_view(), name='login'),
                  path('logout/', views.log_out, name='logout'),
              ] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
