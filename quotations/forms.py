from django import forms

from .models import Quotation


class QuotationForm(forms.ModelForm):

    class Meta:
        model = Quotation

        fields = [
            'name',
            'phone',
            'email',
            'city',
            'lift_type',
            'building_type',
            'floors',
            'message'
        ]

        widgets = {

            'message': forms.Textarea(
                attrs={
                    'rows': 5
                }
            ),

        }
