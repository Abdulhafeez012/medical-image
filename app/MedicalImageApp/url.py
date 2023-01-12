from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'MedicalImageApp'

urlpatterns = [
                  path('', views.BaseView.as_view(), name='base'),
                  path('login/', views.LogInView.as_view(), name='login'),
                  path('home/', views.HomeView.as_view(), name='user_home'),
                  path('patient-detail/<int:pk>/', views.PatientDetails.as_view(), name='patient-detail'),
                  path('add-record/', views.AddRecordForPatient.as_view(), name="add_record"),
                  path('add-account/', views.AddAccount.as_view(), name='add_account'),
                  path('add-user/', views.AddUserView.as_view(), name='add_user')
              ] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
