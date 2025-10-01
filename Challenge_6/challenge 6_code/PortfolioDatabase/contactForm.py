from django import forms

from PortfolioDatabase.models import Contact
from PortfolioDatabase.models import Portfolio


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Name*", max_length=100)
    email = forms.EmailField(required=True, label="Email*")
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 80}))

    def log_data(self):
        print(self.cleaned_data.get('name'))
        print(self.cleaned_data.get('email'))
        print(self.cleaned_data.get('message'))

class ContactModelForm(forms.ModelForm):
    template_name = 'PortfolioDatabase/form_snippit.html'
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter your name",'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': "Enter your email",'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': "Enter your message",'class': 'form-control','rows': 5, 'cols': 50}),
        }

class PortfolioAdd(forms.ModelForm):
    template_name = 'PortfolioDatabase/form_snippit.html'
    class Meta:
        model = Portfolio
        fields = ('name', 'description', 'image', 'slug')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter project name",'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': "Enter project description",'class': 'form-control','rows': 5, 'cols': 50}),
        }

class PortfolioEdit(forms.ModelForm):
    template_name = 'PortfolioDatabase/form_snippit.html'
    class Meta:
        model = Portfolio
        fields = ('name', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter project name",'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': "Enter project description",'class': 'form-control','rows': 5, 'cols': 50}),
        }