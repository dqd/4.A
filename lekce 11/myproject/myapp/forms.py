from django.forms import ModelForm

from .models import MyModel


class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        exclude = ["user"]