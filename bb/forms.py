from django.forms import ModelForm
from bb.models import BB

class BBForm(ModelForm):
    class Meta:
        model = BB
