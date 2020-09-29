from django.forms import ModelForm
from autos.models import Make

# Si es que no se usan generic views para forms, se debe definir manualmente.
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'