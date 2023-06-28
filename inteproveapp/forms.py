
from django.forms import ModelForm
from django import forms
from .models import User,Investor,Updates

class LogInForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']

class RegisterForm(ModelForm):
    CATEGORY_CHOICES = [
        ('R', 'Researcher'),
        ('S', 'Supervisor'),
        ('I', 'Investor'),
    ]
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput)
    type = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = User
        fields = ['username','password','firstname','lastname','type']

class AddInvestorForm(ModelForm):
    profilename = forms.CharField(widget=forms.TextInput)
    profiletype = forms.CharField(widget=forms.TextInput)
    status = forms.CharField(widget=forms.TextInput)
    taskid = forms.CharField(widget=forms.TextInput)
    date = forms.DateField(widget=forms.DateInput)

    class Meta:
        model = Investor
        fields = ['profilename','profiletype','status','taskid','date']


class AddUpdatesForm(ModelForm):
    CATEGORY_CHOICES = [
        ('AUM', 'AUM'),
        ('Asset Allocation', 'Asset Allocation'),
        ('Managers', 'Managers'),
        ('Service Providers', 'Service Providers'),
        ('Contacts', 'Contacts'),
        ('General', 'General'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    notes = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=forms.DateInput)

    class Meta:
        model = Updates
        fields = ['notes','date','category']
