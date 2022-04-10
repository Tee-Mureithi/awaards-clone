from django import forms
from .models import Project,Rate,Profile,DESIGN_CHOICES,USABILITY_CHOICES,CONTENT_CHOICES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class GreazeRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1','password2' ]

        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.TextInput(attrs = {'class':'form-control ','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.TextInput(attrs = {'class':'form-control', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }

class PostProjectForm(forms.ModelForm):
        class Meta:
            model = Project
            fields = ['title','image','description','link']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Project Title...'}),
            'image':forms.TextInput(attrs= {'class':'form-control ','placeholder':'In a word...','label':'Put a name'}),
            'description':forms.Textarea(attrs = {'class':'form-control','placeholder':"Write here..",'label':"Caption"}),
            'link':forms.URLInput(attrs={'class':'form-control'}),
        }

class RateForm(forms.ModelForm):

    design = forms.ChoiceField(choices=DESIGN_CHOICES,widget=forms.Select(),required=True)
    usability = forms.ChoiceField(choices=USABILITY_CHOICES,widget=forms.Select(),required=True)
    content = forms.ChoiceField(choices=CONTENT_CHOICES,widget=forms.Select(),required=True)
    class Meta:
        model = Rate
        fields = ['design','usability','content']

        # widgets = {
        #     'design': forms.SelectMultiple(attrs={'class':'form-control','name':'design'}),
        #     'usability': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Input value','name':'usability'}),
        #     'content': forms.SelectMultiple(attrs={'class':'form-control','name':'content'}),
        # }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio','gender','contact']

        widgets = {
            'profile_photo':forms.FileInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control ','placeholder':'Write here...','label':'Put a name'}),
        }





class UpdateProjectForm(forms.ModelForm):
        class Meta:
            model = Project
            fields = ['title','image','description','link']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Project Title...'}),
            'image':forms.TextInput(attrs= {'class':'form-control ','placeholder':'In a word...','label':'Put a name'}),
            'description':forms.Textarea(attrs = {'class':'form-control','placeholder':"Caption",'label':"Caption"}),
            'link':forms.URLInput(attrs={'class':'form-control'}),
        }
