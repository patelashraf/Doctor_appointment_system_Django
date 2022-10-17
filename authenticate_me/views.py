

from django.shortcuts import render
from django.contrib import messages
# from django.contrib.auth.models import get_user_model
from django.contrib.auth.models import User
from authenticate_me.models import User_reg, dr_reg
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import EditProfileForm, PasswordChangingForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView

#from dr_appointment import authenticate_me
User = get_user_model()

# Create your views here.
#def login(request,name):
    #return render(request, 'user/login.html')  

def Login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upass')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, 'login successful')
        return redirect('appointment:home1')
    return render(request, 'user/login.html')

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        address = request.POST.get('add')
        gender = request.POST.get('sex')
        phone = request.POST.get('phone')
        username = request.POST.get('uname')
        userpassword = request.POST.get('upass')

        myuser = User.objects.create_user(username, email, userpassword)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_user = True
        myuser.save()
        
        User_reg.objects.create(fname=fname,lname=lname,email=email,address=address,gender=gender,phone=phone,Username=username,Userpassword=userpassword,user=myuser)
        # register.save()

        messages.success(request, 'Register successful')
        return render(request,'user/login.html')
    else:
        return render(request, 'user/register.html')  

# def dr_login(request):
#     return render(request, 'doctor/login.html')  

def dr_register(request):
    if request.method == "POST":
        fname = request.POST.get('dfname')
        lname = request.POST.get('dlname')
        image = request.POST.get('img')
        qualification = request.POST.get('qualification')
        specialist = request.POST.get('specialisation')
        phone = request.POST.get('dphone')
        gender = request.POST.get('dsex')
        address = request.POST.get('dadd')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        email = request.POST.get('demail')
        dr_username = request.POST.get('duname')
        dr_password = request.POST.get('dpass')

        mydoctor = User.objects.create_user(dr_username, email, dr_password)
        mydoctor.first_name = fname
        mydoctor.last_name = lname
        mydoctor.is_doctor = True
        mydoctor.save()

        dr_reg.objects.create(fname=fname,lname=lname,image=image, qualificaton=qualification, specialisation = specialist, phone= phone, gender=gender, address=address, state=state, city=city, zip=zip, email=email, dUsername=dr_username, dPassword= dr_password,user=mydoctor)
        # dr_register.save()  
    
        messages.success(request, 'Registeration successful')
        return render(request, 'user/login.html')  

    else:
        return render(request, 'doctor/register.html')

@login_required
def signout(request):
    logout(request)
    return redirect('/')
    
    

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='users-profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#         context = {
#             'user_form': user_form,
#             'profile_form': profile_form
#         }

#         return render(request, 'user/edit-profile.html', context)

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'user/edit-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    

