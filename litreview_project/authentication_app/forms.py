from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from litreview_app.models import Ticket, Review, UserFollows


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class SigupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'description', 'image']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        self.instance.user = self.user
        return super().save(*args, **kwargs)

class TicketReviewFrom(forms.ModelForm):
    review_title = forms.CharField(max_length=63, label='title')
    review_note = forms.IntegerField(min_value=0, max_value=5)
    review_coment = forms.CharField()

    class Meta:
        model = Ticket
        fields = ['name', 'description', 'image']
    
    def save(self, *args, **kwargs):
        ticket = super().save(*args, **kwargs)
        review = Review.object.create(ticket=ticket, title=self.cleaned_data['review_title'], note=self.cleaned_data['review_note'], coment=self.cleaned_data['review_coment'])
        return review

class SubForm(forms.Form):
    search = forms.CharField(max_length=63, label='search')

    def clean_search(self):
        User = get_user_model()
        data = self.cleaned_data['search']
        if User.objects.filter(username=data).exists():
            return User.objects.get(username=data)
        else : 
            raise forms.ValidationError("username not found.")
        
        
