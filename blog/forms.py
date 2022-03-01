from django import forms
from .models import FeedBack

class FeedBackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'w-input', 'placeholder': 'Имя:'})
        self.fields['phone'].widget.attrs.update({'class': 'w-input', 'placeholder': 'Телефон:'})

    class Meta:
        model = FeedBack
        fields = ('name', 'phone')