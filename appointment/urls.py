from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from appointment.views import HomePageView,TakeAppointmentView,AppointmentCreateView
from appointment.views import HomePageView,TakeAppointmentView,AppointmentCreateView,AppointmentDeleteView,PatientDeleteView,PatientListView,payment_gateway,payme

app_name = 'appointment'

urlpatterns = [
    path('', HomePageView.as_view(), name='home1'),
    path('patient-book-appointment/', TakeAppointmentView.as_view(), name='book-appointment'),
    path('create-appointment/', AppointmentCreateView.as_view(), name='doctor-appointment-create'),
    # path('<pk>/delete/', AppointmentDeleteView.as_view(), name='delete-appointment'),
    # path('<pk>/patient/delete', PatientDeleteView.as_view(), name='delete-patient'),
    path('payment-gateway', views.payment_gateway, name='paymentgateway'),
    path('patients-list/', PatientListView.as_view(), name='patient-list'),
    path('payme', views.payme, name='paymetogo'),
    path('paybook', views.paybook, name='paytobook'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)