from cProfile import label
from django import forms
from .models import BribeReport,ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]


class BribeReportForm(forms.ModelForm):
    class Meta:
        model = BribeReport
        fields = ['ministry', 'institution', 'reason', 'amount',
                  'description', 'reporter_name', 'reporter_email']

        help_texts = {
            'institution': 'Enter the name of the institution or individual involved.',
            'description': 'Provide a detailed description of the incident.',
            'reason': 'Specify the reason for the bribe (e.g., "to expedite service", "to avoid a fine").',
        }

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'amount': forms.NumberInput(attrs={'step': '5'}),
            # add classes to style with CSS framework if needed
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'amount': 'Amount (ZMW, optional)',
            'reporter_name': 'Reporter Name ('
            'optional)',
            'reporter_email': 'Reporter Email (optional)',
            'reason': 'Reason for Bribe',
        }