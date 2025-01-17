from django import forms
from .models import Contact  # type: ignore
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone'
        )

    def clean(self):
        self.add_error(
            None,
            ValidationError(
                'Message of error',
                code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Message of error 2',
                code='invalid'
            )
        )
        return super().clean()
