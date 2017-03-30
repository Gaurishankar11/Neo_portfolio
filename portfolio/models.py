from django.db import models
from ckeditor.fields import RichTextField
from adminsortable.models import SortableMixin


PROJECT_IMAGES_PATH = 'media'
DB_TYPES = (
    ('NoSql','NoSql'),
    ('RDBMS','RDBMS'),
    ("Other","Other"),)
# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=60)
    symbol = models.ImageField(upload_to=PROJECT_IMAGES_PATH,blank=True)
    class Meta:
        verbose_name_plural = "Technologies"
    def __unicode__(self):
        return unicode(self.name)

class ProjectImage(models.Model):
    images = models.ImageField(upload_to=PROJECT_IMAGES_PATH)
    def __unicode__(self):
        return unicode(self.images)

class Category(models.Model):
    name = models.CharField(max_length=20)
    status = models.BooleanField(max_length=20, default=False)
    class Meta:
        verbose_name_plural = "categeries"
    def __unicode__(self):
        return unicode(self.name)

class Library(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return unicode(self.name)

class Versioning(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Versioning"
    def __unicode__(self):
        return unicode(self.name)

class Database(models.Model):
    name = models.CharField(max_length=20)
    db_type = models.CharField(max_length=20,choices=DB_TYPES,default="Other")
    def __unicode__(self):
        return unicode(self.name)

from django.forms import CheckboxSelectMultiple
class Project(SortableMixin):
    name = models.CharField(max_length=60)
    description = RichTextField(default="Description of project")
    url = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=PROJECT_IMAGES_PATH,blank=True)
    client_name = models.CharField(max_length=60,null=True,blank=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    created_date = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    updated_date = models.DateTimeField(null=True,blank=True,auto_now=True)
    is_active = models.BooleanField(max_length=1,default=False,help_text="Select if the project is activeself.")
    technologies = models.ManyToManyField(Technology)#,widget=CheckboxSelectMultiple())
    images = models.ManyToManyField(ProjectImage)
    order_sequence = models.IntegerField(default=0)
    version_controll = models.ForeignKey(Versioning)    
    localization = models.BooleanField(default=False)
    third_party_library = models.ManyToManyField(Library,null=True,blank=True)
    production_link = models.CharField(max_length=100,null=True,blank=True)
    dev_link = models.CharField(max_length=100,null=True,blank=True)
    database_used = models.ManyToManyField(Database)
    class Meta:
        ordering = ['order_sequence']

    def __unicode__(self):
        return unicode(self.name)


