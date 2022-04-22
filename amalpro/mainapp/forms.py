from api.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CustomerForm(forms.ModelForm):
    ## change the widget of the date field.
    dobCustomer = forms.DateField(
        label='What is your birth date?', 
        # change the range of the years from 1980 to currentYear - 5
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))
    )
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Customer
        fields = ("__all__")


class ServiceproviderForm(forms.ModelForm):
    dobSP = forms.DateField(
        label='What is your birth date?', 
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))
    )
    def __init__(self, *args, **kwargs):
        super(ServiceproviderForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = ServiceProviders
        fields = ("__all__")

class BookingForm(forms.ModelForm):
    bookingDate = forms.DateField(
        label='When do you want to date an appointment?', 
        widget=forms.SelectDateWidget(years=range(2022, datetime.date.today().year-5))
    )
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = Booking
        fields = ("__all__")

class ListingForm(forms.ModelForm):
    ## change the widget of the date field.    
    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Listing
        fields = ("__all__")