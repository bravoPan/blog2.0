from django import forms
from django.core.exceptions import ValidationError


def words_validator(comment):
    if len(comment) == 0:
        raise ValidationError("Not enough words")


def non_pan(comment):
    if comment == "pan" or comment == "Pan":
        raise ValidationError("Your name can not be mine :( )")


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[non_pan])
    comment = forms.CharField(widget=forms.Textarea(), validators=[words_validator])
    # avatar = forms.CharField(widget=forms.HiddenInput(), required=False)
    email = forms.EmailField(required=True)
    parent = forms.IntegerField(widget=forms.HiddenInput(), required=False)
