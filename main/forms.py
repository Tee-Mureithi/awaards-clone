from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Project



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User 
        fields = ("username", "email","password1","password2")


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False )
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image','description','link']


    widgets = {

         
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Project Title...'}),
            'image':forms.TextInput(attrs= {'class':'form-control ','placeholder':'In a word...','label':'Put a name'}),
            'description':forms.Textarea(attrs = {'class':'form-control','placeholder':"Write here..",'label':"Caption"}),
            'link':forms.URLInput(attrs={'class':'form-control'}),
        }
    