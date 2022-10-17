import imp
from django import forms

from authenticate_me.models import Appointment,BookAppointment

class CreateAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "Full Name"
        # self.fields['image'].label = "Image"
        self.fields['department'].label = "Department"
        self.fields['start_time'].label = "Start Time"
        self.fields['hospital_name'].label = "Hospital Name"
        self.fields['qualification_name'].label = "Qualification"

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Full Name',
                'class' : 'form-control',
            }
        )

        self.fields['department'].widget.attrs.update(
            {
                'placeholder': 'Select Your Service',
                'class' : 'form-control',
            }
        )

        self.fields['start_time'].widget.attrs.update(
            {
                'placeholder': 'Ex : 9 AM',
                'class' : 'form-control',
            }
        )
        self.fields['end_time'].widget.attrs.update(
            {
                'placeholder': 'Ex: 5 PM',
                'class' : 'form-control',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'Ex : Uttara, Dhaka',
                'class' : 'form-control',
            }
        )

        self.fields['hospital_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Hospital Name',
                'class' : 'form-control',
            }
        )

        self.fields['qualification_name'].widget.attrs.update(
            {
                'placeholder': 'Ex : MBBS, BDS',
                'class' : 'form-control',
            }
        )


    class Meta:
        model = Appointment
        fields = ['full_name', 'department', 'start_time', 'end_time', 'location',
                  'hospital_name', 'qualification_name']

    def is_valid(self):
        valid = super(CreateAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(CreateAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class BookAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['appointment'].label = "Choose Your Doctor"
        self.fields['full_name'].label = "Full Name"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['message'].label = "Message"

        self.fields['appointment'].widget.attrs.update(
            {
                'placeholder': 'Choose Your Doctor',
                'class' : 'form-control',
            }
        )

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
                'class' : 'form-control',
            }
        )

        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
                'class' : 'form-control',
            }
        )
        self.fields['message'].widget.attrs.update(
            {
                'placeholder': 'Write a short message',
                'class' : 'form-control',
            }
        )

    class Meta:
        model = BookAppointment
        fields = ['appointment', 'full_name', 'phone_number', 'message']

    def is_valid(self):
        valid = super(BookAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(BookAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment