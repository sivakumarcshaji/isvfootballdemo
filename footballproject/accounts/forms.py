from django import forms
from . models import User_accounts

from phonenumber_field.formfields import PhoneNumberField


from phonenumber_field.widgets import PhoneNumberPrefixWidget

class personclass(forms.ModelForm):
    phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width: 500px;',},initial='IN'))
    class Meta:
        model=User_accounts
        fields=('username','emailid','phone_number',)
        widgets = {
            'username': forms.TextInput(attrs={"placeholder":"enter user name",'style': 'width: 500px;','class': 'form-control'}),
            'emailid': forms.TextInput(attrs={"placeholder":"enter mail id",'style': 'width: 500px;','class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'style': 'width: 500px;','class': 'form-control'}),

        }


class personlogin(forms.Form):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control', 'style': 'width: 500px;', }, initial='IN'))
    class Meta:

        fields=('phone_number',)