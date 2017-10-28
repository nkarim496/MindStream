from django.forms import ModelForm
from minder.models import Mind


class MindForm(ModelForm):
    class Meta:
        model = Mind
        fields = ['mind', 'mind_img']
