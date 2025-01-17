from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact  # type: ignore


class ContactForm(forms.ModelForm):
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'class-class',
    #             'placeholder': 'John'
    #         }
    #     ),
    #     label='Name',
    #     help_text='Help text for your user'
    # )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
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
            'picture',
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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
    )

    email = forms.EmailField(
        required=True,
        min_length=3,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'A user with that e-mail already exists.',
                    code='invalid'
                )
            )

        return email
