from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []

class PollDeleteForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ("question",)

    def clean_title(self):
        if self.instance.question != self.cleaned_data.get("question"):
            raise ValidationError("Название опроса не соответствует")
        return self.cleaned_data.get("question")

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('option',)
        exclude = []

class ChoiceDeleteForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ("option",)

    def clean_title(self):
        if self.instance.option != self.cleaned_data.get("option"):
            raise ValidationError("Название варианта не соответствует")
        return self.cleaned_data.get("option")

class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label="Найти опрос")

