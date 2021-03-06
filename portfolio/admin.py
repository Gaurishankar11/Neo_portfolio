from django.contrib import admin
from adminsortable.admin import SortableAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple	
from django.forms import CheckboxSelectMultiple
from django.db import models

# Register your models here.
from models import Project, Technology,ProjectImage, Category, Database, Library
class MyModelAdmin(SortableAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

#admin.site.register(Project, SortableAdmin)
admin.site.register([ProjectImage,Category,Database,Technology,Library])
admin.site.register(Project,MyModelAdmin)