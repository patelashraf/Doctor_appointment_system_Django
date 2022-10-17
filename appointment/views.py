from ast import Param
import imp

from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from authenticate_me.models import User
from .decorators import user_is_patient, user_is_doctor
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DetailView, DeleteView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import CreateAppointmentForm, BookAppointmentForm
from authenticate_me.models import Appointment, BookAppointment
#payment
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import random
from paytm import checksum
merchant_id = 'oltDRu11918147366097'

# Create your views here.

class TakeAppointmentView(CreateView):
    template_name = 'appointment/book-appointment.html'
    form_class = BookAppointmentForm
    extra_context = {
        'title': 'Take Appointment'
    }
    success_url = reverse_lazy('appointment:home1')

    @method_decorator(login_required(login_url=reverse_lazy('authenticate_me:login')))
    # @method_decorator(login_required(login_url=reverse_lazy('authenticate_me:login')))
    # @login_required(login_url=reverse_lazy('authenticate_me:login'))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authenticate_me:login')
        if self.request.user.is_authenticated and self.request.user.is_doctor:
            return reverse_lazy('authenticate_me:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TakeAppointmentView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        # return HttpResponse('Form not valid')

"""
creating appointment by doctor
"""

class AppointmentCreateView(CreateView):
    template_name = 'appointment/create-appointment.html'
    form_class = CreateAppointmentForm
    extra_context = {
        'title': 'Post New Appointment'
    }
    success_url = reverse_lazy('appointment:home1')

    @method_decorator(login_required(login_url=reverse_lazy('authenticate_me:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authenticate_me:login')
        if self.request.user.is_authenticated and self.request.user.is_user:
            return reverse_lazy('authenticate_me:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AppointmentCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PatientListView(ListView):
    model = BookAppointment
    # patients = BookAppointment.objects.all()
    # data ={
    #     'patients':patients
    # }
    template_name = "appointment/patient-list.html"
    context_object_name = 'patients'
    

    def get_queryset(self):
        return self.model.objects.filter(appointment__user_id=self.request.user.id).order_by('-id')

"""
homepage where appointment will be visible
"""

class HomePageView(ListView):
    paginate_by = 6
    model = Appointment
    context_object_name = 'home'
    template_name = "home1.html"

    def get_queryset(self):
        return self.model.objects.all().order_by('-id') 

class PatientDeleteView(DeleteView):
    model = BookAppointment
    # success_url = reverse_lazy('appointment:patient-list ')
    success_url ="/"

class AppointmentDeleteView(DeleteView):
    """ 
       For Delete any Appointment created by Doctor
    """
    model = Appointment
    # success_url = reverse_lazy('appointment:doctor-appointment')
    success_url ="/"


# class SearchView(ListView):
#     paginate_by = 6
#     model = Appointment
#     template_name = 'appointment/search.html'
#     context_object_name = 'appointment'

#     def get_queryset(self):
#         return self.model.objects.filter(location__contains=self.request.GET['location'],
#                                          department__contains=self.request.GET['department'])



#payment gateway
@csrf_exempt
def payment_gateway(request):
    return render(request, "payment/paytobook.html")

def payme(request):
    if request.method == 'POST':
        ammount = 200
        user = request.user
        order_id = random.randint(111111111, 999999999)
        param_dict = {
            'MID': 'oltDRu11918147366097',
            'ORDER_ID': '1234567',
            'TXN_AMOUNT': str(ammount),
            'CUST_ID': str(user),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/payment_gateway/', 
        }
        # param_dict['CHECKSUMHASH'] = checksum.generateSignature(param_dict, 'oltDRu11918147366097')
        param_dict['CHECKSUMHASH'] = checksum.generateSignature(param_dict,merchant_id)
        # context = {'param_dict':param_dict}
        return render(request, 'payment/buy.html', {'param_dict': param_dict})
        # return render(request, 'payment/buy.html',context)
    return render(request, "payment/paytobook.html")

def paybook(request):
    return render(request,"payment/paytobook.html")
