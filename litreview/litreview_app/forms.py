from django import forms
from litreview_app.models import Ticket

class LoginForm(forms.Form):
   email = forms.EmailField()
   password = forms.CharField(max_length=1000)
   

class RegisterForm(forms.Form):
   name = forms.CharField(required=False)
   birth = forms.DateField()
   email = forms.EmailField()
   password = forms.CharField(max_length=1000)
   confirm_password = forms.CharField(max_length=1000)

class TicketForm(forms.ModelForm):
   class Meta:
     model = Ticket
     fields = '__all__'