from django import forms
from .models import movieModel,ReviewModel
class MovieForm(forms.ModelForm):
    class Meta:
        model= movieModel
        fields="__all__"
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class ReviewForm(forms.ModelForm):
    class Meta:
        model= ReviewModel
        fields=['text','rating']
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })