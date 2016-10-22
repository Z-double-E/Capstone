from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Problem, ProblemSet


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class UserForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    password = forms.CharField(label="Password", widget=forms.PasswordInput({
                            'class': 'form-control',
                            'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"


class SearchProblem(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ["problemSP", "dp", "type"]

    def __init__(self, *args, **kwargs):
        super(SearchProblem, self).__init__(*args, **kwargs)
        self.fields['problemSP'].widget.attrs.update({'class' : 'form-control'})
        self.fields['dp'].widget.attrs.update({'class' : 'form-control'})
        self.fields['type'].widget.attrs.update({'class' : 'form-control'})
        #self.fields['status'].widget.attrs.update({'class' : 'btn btn-primary btn-select btn-select-light'})
        self.fields['problemSP'].required = False
        self.fields['type'].required = False
        self.fields['dp'].required = False
        self.fields['problemSP'].label = "Problem Solving Paradigms"
        self.fields['dp'].label = "Data Structures"
        self.fields['type'].label = "Algorithm"


# problem from class to creat and update problem sets
class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ["name", "status", "difficulty","problemSP", "dp", "type","url","hasSolution","surl","wused"]

    #this method intial the field by giving them classes
    def __init__(self, *args, **kwargs):
        super(ProblemForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['status'].widget.attrs.update({'class' : 'form-control'})
        self.fields['difficulty'].widget.attrs.update({'class' : 'form-control'})
        self.fields['problemSP'].widget.attrs.update({'class' : 'form-control'})
        self.fields['dp'].widget.attrs.update({'class' : 'form-control'})
        self.fields['type'].widget.attrs.update({'class' : 'form-control'})
        self.fields['hasSolution'].widget.attrs.update({'class' : 'checkbox',})
        self.fields['surl'].widget.attrs.update({'class' : 'form-control'})
        self.fields['wused'].widget.attrs.update({'class' : 'form-control'})
        self.fields['url'].widget.attrs.update({'class': 'form-control'})
        #self.fields['status'].widget.attrs.update({'class' : 'btn btn-primary btn-select btn-select-light'})
        self.fields['problemSP'].required = False
        self.fields['difficulty'].required = False
        self.fields['hasSolution'].required = False
        self.fields['surl'].required = False
        self.fields['type'].required = False
        self.fields['dp'].required = False
        self.fields['wused'].required = False
        self.fields['problemSP'].label = "Problem Solving Paradigms:"
        self.fields['dp'].label = "Data Structures:"
        self.fields['type'].label = "Algorithm:"
        self.fields['name'].label = "Name:"
        self.fields['difficulty'].label = "Difficulty:"
        self.fields['hasSolution'].label = "Solution Available:"
        self.fields['surl'].label = "Solution url:"
        self.fields['status'].label = "Status:"
        self.fields['wused'].label = "Place used:"
        self.fields['url'].label = "Problem url:"


# problem set from class to creat and update problem sets
class ProblemSetForm(forms.ModelForm):
    class Meta:
        model = ProblemSet
        fields = ["name", "problems", "wused"]

    def __init__(self, *args, **kwargs):
        super(ProblemSetForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['problems'].widget.attrs.update({'multiple class': 'form-control'})
        self.fields['wused'].widget.attrs.update({'class' : 'form-control'})
        self.fields['wused'].required = False
        self.fields['name'].label = "Name:"
        self.fields['problems'].label = "Mutiple select list(hold shift to select more than one problems):"
        self.fields['wused'].label = "Place used:"
