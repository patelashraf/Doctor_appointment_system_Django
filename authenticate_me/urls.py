from re import template
from django.contrib.auth import views
from . import views
from django.urls import path
from authenticate_me.views import *
from appointment.views import AppointmentDeleteView,PatientDeleteView


from django.conf import settings
from django.conf.urls.static import static

app_name = "authenticate_me"

urlpatterns = [
   #path('login/', views.LoginView.as_view(), name='login'),
   path('login/', views.Login, name="login"),
   path('userreg/',views.register, name="user_register"),
   path('drreg/',views.dr_register, name="drregister"),
   path('logout/',views.signout, name="Logout"),
   path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
   # path('profile/',views.profile, name='users-profile')
   #path('password/', auth_views.PasswordChangeView.as_view())
   path('password/',PasswordsChangeView.as_view(template_name='change-password.html')),
   path('<pk>/delete/', AppointmentDeleteView.as_view(), name='delete-appointment'),
   path('<pk>/patient/delete', PatientDeleteView.as_view(), name='delete-patient'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)