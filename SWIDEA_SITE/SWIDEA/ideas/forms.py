from django import forms
from .models import Idea,Devtool

class IdeaForm(forms.ModelForm):
    
    class Meta:
        model = Idea
        fields = '__all__'

class DevtoolForm(forms.ModelForm):
    
    class Meta:
        model = Devtool
        fields = '__all__'