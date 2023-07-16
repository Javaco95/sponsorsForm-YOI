from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Form
from .resources import FormResource

# Register your models here.

@admin.register(Form)
class FormAdmin(ImportExportModelAdmin):
    resource_class = FormResource

