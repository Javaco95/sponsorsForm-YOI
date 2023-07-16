from import_export import resources
from .models import Form

class FormResource(resources.ModelResource):
    class Meta:
        model = Form
