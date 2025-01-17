from django import forms
from django.core.exceptions import ValidationError
from .models import Contact  # type: ignore


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-class',
                'placeholder': 'John'
            }
        ),
        label='Name',
        help_text='Help text for your user'
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'class-class',
        #     'placeholder': 'John'
        # })

    class Meta:
        model = Contact

        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': '',
        #             'placeholder': 'John'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            message_error = ValidationError(
                'The first name isn\'t equal the last name',
                code='invalid'
            )

            self.add_error('first_name', message_error)
            self.add_error('last_name', message_error)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Message of error clean_first_name',
                    code='invalid'
                )
            )

        return first_name
