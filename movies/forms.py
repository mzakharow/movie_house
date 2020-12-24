from captcha.fields import CaptchaField
from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    # captcha = CaptchaField()

    class Meta:
        model = Review
        fields = ('name', 'email', 'text')
