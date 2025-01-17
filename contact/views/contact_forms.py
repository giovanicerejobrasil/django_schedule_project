from django import forms
from django.shortcuts import render  # , get_object_or_404, redirect
# from django.db.models import Q
# from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from contact.models import Contact  # type: ignore


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


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )
