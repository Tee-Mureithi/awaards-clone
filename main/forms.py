from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Project,Rate,Profile,DESIGN_CHOICES,USABILITY_CHOICES,CONTENT_CHOICES



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
    
class RateForm(forms.ModelForm):

    design = forms.ChoiceField(choices=DESIGN_CHOICES,widget=forms.Select(),required=True)
    usability = forms.ChoiceField(choices=USABILITY_CHOICES,widget=forms.Select(),required=True)
    content = forms.ChoiceField(choices=CONTENT_CHOICES,widget=forms.Select(),required=True)
    class Meta:
        model = Rate
        fields = ['design','usability','content']



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