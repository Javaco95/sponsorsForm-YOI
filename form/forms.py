from django.forms import ModelForm
from .models import Form

class SponsorForm(ModelForm):
    class Meta:
        model = Form
        fields = ['sponsored', 'sponsor', 'amount', 'receipt',]
        