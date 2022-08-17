from dataclasses import fields
from django.forms import ModelForm

from myapp.models import TODO
class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields =['title', 'status', 'priority']