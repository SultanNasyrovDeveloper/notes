##########
# DJANGO #
##########

# ============
# = SETTINGS =
# ============
# settings.py

# database configuration
# ------------------------
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '',
    'USER': '',
    'PASSWORD': '123456',
    'HOST': 'localhost',
    'PORT': '',
}

# templates configuration
# -------------------------
os.path.join(BASE_DIR,  'templates')

# static and media files configuration
# -------------------------------------
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# project_name/urls.py
# --------------------
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# ==========
# = MODELS =
# ==========
# Tips:
# - always use fields that most suits your data
# - make population scripts for creating test database model instances

# basic model setup
# -----------------
from django.db import models


class ModelName(models.Model):
    """Basic model"""
    pass


# MODEL FIELDS
# ============
# common kwargs
# --------------
    primary_key=True  # to make field used as id
    validators=[]
    widget=WidgetClass
    null=True # wheather the value can be None
    blank=True # - можно оставлять поле пустым
    choices=some_tuple_or_list # - варианты
    unique=True # must be unique
    default='Не указано'
    help_text='Введите ФИО'  # - текст подсказка
    verbose_name='Имя поля'  # - имя поля

# fields reference
# -----------------
# relation fileds
OneToOneField()
ForeignKey(SomeModel, on_delete=models.CASCADE, related_name='some_name')
ManyToManyField(SomeModel, verbose_name='Name')

# ids
AutoField()
UUidFiled(primary_key=True, default=uuid.uuid4, editable=False)

# bool fields
BooleanField()
NullBooleanField() # yes no or unknown

# integers
IntegerField() # от -2147483648 до 2147483647
BigIntegerField() # от -9223372036854775808 до 9223372036854775807
PositiveIntegerField() # от 0 до 2147483647
FloatFiled()  # python float
DecimalField(max_digits=18, decimal_places=12) # decimal_places = чисел после запятой
CommaSeparatedIntegerField()

# text fields
CharField(max_length=150)
EmailField()
TextField()
SlugField(max_length=20)
URLField(max_length=150)

# date time fields
TimeField()  # datetime.time()
DateField(auto_now=True, auto_now_add=False)  # datetime.date()
DateTimeField(auto_now_add=True)  # datetime.datetime()
DurationField()  # python timedelta

# file fields
ImageField(upload_to='/')
FileField(upload_to='/')
FilePathField()


# META CLASS OPTIONS
# ==================
class Meta:
    ordering = ["title", "-pubdate"]
    verbose_name = "BetterName"
    app_label = 'myapp'  # name of app this model belongs to
    proxy = True
    abstract = True

# MODEL METHODS
# =============
from django.shortcuts import reverse

def __str__(self):
    """ Returns model instance string representation """
    return self.name


def get_absolute_url ():
    """ Returns model instance absolute url """
    return reverse('model-detail-view', args=[str(self.id)])


# MODEL INSTANCE MANIPULATIONS
# ============================
# object creation
# ----------------
m = Model(field_name='Some name')
m.save()

# change field values
# -------------------
m.field_name = 'New name'
m.save()
# or
m.objects.filter(id=53).update(name='Alice')

# changing foreign key
# --------------------
fk_object = FkModel.objects.get()
m.foreign_key = fk_object
m.save()

# adding M2M fields
# ------------------
john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
entry.authors.add(john, paul)

# deleting related objects
# -------------------------
john = Author.objects.create(name="John")
entry.authors.remove(john)

# remove all related objects
# ---------------------------
entry.authors.clear()

# delete
# ------
m.delete()

# copy
# ----
m.pk == None
m.save()


# QUERYSETS
# =========
# queryset methods
# ----------------
exists()  # check if queryset is not empty
create()
get_or_create()
update_or_create()
bulk_create([]) # create set of model instances
update()

# get instances
# -------------
all() # - all objects
asc()  # ascending
desc()  # descending
distinct(filed1, field2)  # eliminates duplicate rows from query results
# must provide order_by
reverse()
get(id=some_id)
filter(field_name='some name')
exclude(field_name='some name') # Возвращает объекты исключающие параметры фильтрации
filter().order_by() # доп сортировка
reverse() # изменяет сортировку на обратную
values(*fields) # возвращет словарь результатов вместо объектов
values_list()  # returns list
defer('field_name') # не загружать поля
only('field_name') # загрузить только эти поля
count() #
first() #
last() #
union()  # used to combine results of two different querysets

# slices
# ------
all()[5:10]

# filtering querysets
# -------------------
filter(some_id=4)
filter(some_id__exact='Someting')
filter(some_id__iexact='Someting') # - регистронезависимый
filter(some_id__contains='Someting')
filter(some_id__icontains='Someting')
filter(field__in=[1, 2, 3])
filter(filed__gt=65)  # greater than
filter(field__gte=45)  #  less than
filter(field__lte=18)  #  less than or equal
filter(field__startswith='What')
filter(field__istartswith='what')
filter(field__endswith='?')
filter(field__iendswith='k')
filter(field__range=(start, end))
filter(field__year__gt=2005)
filter(field__month=12)
filter(field__day__lt=25)
filter(field__week_day=1)  # 1 Sunday
filter(field__is_null=True)
F('field_name') # ссылка на другое поле модели

SomeModel.objects.filter(item_number__gt=F('other_field'))

# aggregate/annotate
# ------------------
# агрегация высчитывает обобщенное значение для некоторого количества объектов
# возвращает словарь {поле__функция_агрегации: значение}
# aggregate завершающая функция
from django.db.models import F, Avg, Max, Count, Sum


SomeModel.objects.aggregate(Max('price'), Min('price'))
# {'price__max': 120, price__min: 22}

# aннотация высчитывает обобщенное значение для каждого объекта
# возвращает queryset
SomeModel.objects.annotate(Count('items_number', distinct=True),
                               Count('authors'), distinc=True)

Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
Book.objects.annotate(num_authors=Count('authors')).filter(num_authors__gt=1)


# MIGRATIONS
# ==========
# make migrations file that tracks all migration info
python manage.py makemigrations
    <app_name>  # create file only for ceryain app
    --empty  # make empty migrations file
    --name  # specify migrations file name


python manage.py migrate
# updates database or unapplies migrations
    <app_name>  # apply only for curtain app
    zero  # unapply all migrations
    <migration_number>  # unapply all migrations after given

python manage.py sqlmigrate
# displays sql statement for migration

python manage.py showmigrations
# lists projects migrations and their status


# MANAGERS
# =========
# -= extra manager =-
# define manager
class ModelNameManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(field_name='Some name')

# several querysets of one manager
class ForecastDayManager(models.Manager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def latest(self):
        return self.get_query_set().order_by('forecast_date')[0]

# connect it to the model
class ModelName(models.Model):

    objects = models.Manager()  # don't change default manager
    custom_manager_objects = ModelNameManager()

# use it
custom_set = ModelName.custom_manager_objects.all()


# =========== Population script header ===========
import os
import django
from rango.models import Category, Page

# set up environment to work with Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings')

# Setup django
django.setup()


# =========
# = FORMS =
# =========
# create form
# -----------
# forms.py
from django import forms

class SomeForm(forms.Form):
    name = forms.CharField()

# is_valid который выполняет проверку всех полей формы.
# Если все данные правильные, это метод:
# вернет True
# добавит данные формы в атрибут cleaned_data.

# process form in the views
# --------------------------
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})


# MODEL FORMS
# -----------
from django.forms import ModelForm
from .views import SomeModel

# Model form
class SomeModelForm(ModelForm):
    class Meta:
        model = SomeModel
        fields = ['field1', 'field2']
        exclude = []
        widgets = {'field_name': Widget()}
        labels = {'field_name': ''}
        error_messages = {}

# Change existing instance
some_model_instance = ModelName()
form = SomeModelForm(instance=some_model_instance, initial={'filed_name': ''})

# Quick model form
from django.forms import modelform_factory
form = modelform_factory(SomeModel, fields={'\'})


# =========
# = ADMIN =
# =========
# register model in the admin.py
# ------------------------------
from django.contrib import admin
from .models import ModelsName

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    pass

# admin model settings
# ---------------------
list_display = []  # field that will be displayed at list view
list_display_links = [] # fields that will be links from list to detail view
list_editable = [] # fields editable from list view
list_filter = []  # django will generate filters for this fields
inlines = []  # for nested models
search_fields = ('name')  # fields that django will search by
readonly_fields = []
ordering = ('name', 'creation_date')
fields = ('some_filed', 'other_field') # какие показывать поля
exclude = ('some_field') # не показывать
fieldsets = (('Group_name', {'fields': (('url', 'title'), 'content', 'sites')})) # группы полей
filter_horizontal = []


# =========
# = VIEWS =
# =========
from django.shortcuts import render
from django.views.generic import NameView

# FUNCTION BASED VIEWS
# ---------------------
def detail(request, id=1):
    """ Function based object detail view example """
    some_object = get_object_or_404(SomeClass, id=id)
    context = {'object': some_object}
    return render(request, 'template_name', context)


# CLASS BASED VIEWS
# ------------------
# -= Template View =-
class AboutView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        # view logic
        return HttpResponse('result')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # process form cleaned data
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

# ========
# = URLS =
# ========

# when a user requests:
# ---------------------
# - django finds root url config
# - looks for urlpatterns
# - stops at the first one that matches request
# - calls given view function with passed: http request, keywords from url

from django.urls import path, re_path


# path
# ----
#   угловые скобки - зафиксировать значение, можно использовать преобразователь путей
#       str - любая непустая строка
#       int - любой положительное целое число
#       slug - строка slug, состоящая из букв и цифр

urlpatterns = [
    path('catalog/', some_view, name='catalog'),
    path('catalog/<int:year>/', some_view, name='some_name'),
]

# re_path
# --------
#   Можно использовать регулярные выражения

urlpatterns = [
    re_path(r'^catalog/(?P<year[0-9]{4})/(?P<slug[\w-]+)/$', some_view, name='some_name'),
]


# =============
# = TEMPLATES =
# =============

# TEMPALTE TAGS
# ==============
# -= add =-
# {% value|add: "2" %} - 6 if value is 4

# -= url =-
# {% url %} - абсолютная ссылка(без имени домена)
# {% url 'name' argument %}
# {% url 'name' arg=some_arg %}

# -= lorem =-
# {% lorem count method(w, p) random %}


# =============================================================================
# xxxxxxxxxxx AUTH SYSTEM xxxxxxxxxxx

# =========== User ===========
# default user primary attributes:
# - username(required)
# - password(required)
# - email(optional)
# - first_name(optional)
# - last_name(optional)
# - groups(M2M to groups)
# - user_permissions(M2M to Permission)
# - is_superuser(bool)
# - is_staff(bool)
# - is_active(bool)
# - last_login(auto)
# - date_joined(auto)


from django.contrib.auth.models import User
user(username, password, email, first_name, last_name)

# creating user, saves to database
user = User.objects.create_user(username='', password='')

# change fields
user.first_name = 'First'
user.save()

# change password
user.set_password('new pass')


# =========== authenticating ===========
# authenticate means verify credentials
from django.contrib.auth import authenticate, login, logout

user = authenticate(username='', password='')
if user is not None:
    pass
else:
    print('pass is incorrect')

# =========== permissions ========
# Если django.contrib.auth указан в installed_apps
# для каждой модели будут создананы 4 разрешения:
# добавление(add), изменение(change), удаление(delete), просмотр(view)

# проверить разрешение
# catalog app product model
user.has_perm('catalog.add_product')
user.has_perm('catalog.delete_product')

user.user_permissions = [permission_list]
user.user_permissions.add(permission, permission, ...)
user.user_permissions.remove(permission, permission, ...)
user.user_permissions.clear()


# =========== groups ========
user.groups = [group_list]
user.groups.add(group, group, ...)
user.groups.remove(group, group, ...)
user.groups.clear()



# =========================================================================================
# xxxxxxxxxxx Testing xxxxxxxxxxx

# Testing algo
# - database flush
# - fixture is loaded to database
# - setUp()
# - tests
# - tearDown()

class SomeTest(TestCase):
    fixtures = ['some_file.json']

# TESTING TOOLS

# CLIENT
# - dummy web browser
# - simulates requests
# - you can see the chain of redirects
from django.test.client import Client

client = Client(enforce_csrf_checks=False,)

# methods
client.get(path, data=dict(some_data), secure=False)  # makes get request data dict contains get parametrs
# if secure==True: Https()

client.post(path, data=dict(some_data))
    content_type # application/json  - django will serialize data
client.head()
client.options()  # makes options request. usefull for RESTfull interfaces
client.put()
client.patch()
client.delete()
client.trace()
client.login()  # returns True/False
client.force_login()  # used when user needs to be logged but details not important
client.logout()


# TEST RESPONSE
# class Response
    client  # the client that was used to make a request
    content  # body of response as a string
    context  # template context
    json  # body of response parsed as json
    request  # request data
    wsgi_request  #
    status_code
    templates  # list of templates used to render content
    resolver_matches


# RUNNING
# python manage.py test
# python manage.py test --tag=tag_name --exclude-tag=tag_name
# python manage.py test module_name.submodule_name.ClassName.method_name


# FIXTURE(database state for your tests)


# CREATE
# from database
# this assumes fixtures folder was already created in target database
python manage.py dumpdata <app_name>
    --format=json(default)/ yaml


response = client.get('/url/example/')
status_code = response.content  # html template string

response = client.post('/url/example/', {'username': 'anton'})
status_code = response.status_code


from django.test import TestCase
from django.test import tag
from models import SomeModel


# MODELS
# model instance creation test
class SomeModelTest(TestCase):

    def create_some_model(self):
        return SomeModel.objects.create(field1='field1', field2='field2')

    @tag('some')
    def test_some_model_creation(self):
        model_instance = self.create_some_model()
        self.assertTrue(isinstance(model_instance, SomeModel))
        self.assertEqual(some_model_instance.__str__(), some_model_instance.field1)

# VIEWS
# view response status code test
class SomeViewTest(TestCase):
    def test_some_view(self):
        url = reverse('some_model.views.view_name')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

# FORMS
class SomeFormTest(TestCase):

    def test_valid_form(self):
        data = {'title': w.title, 'body': w.body, }
        form = WhateverForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'title': w.title, 'body': w.body, }
        form = WhateverForm(data=data)
        self.assertFalse(form.is_valid())

# API
class SomeApiTest(ResourceTestCase):

    def test_get_api_json(self):
        resp = self.api_client.get('/api/whatever/', format='json')
        self.assertValidJSONResponse(resp)

    def test_get_api_xml(self):
        resp = self.api_client.get('/api/whatever/', format='xml')
        self.assertValidXMLResponse(resp)


# ADVANCED TESTING TOPICS
# RequestFactory





# =========================================================================================
# xxxxxxxxxxx OTHER xxxxxxxxxxx

# =========== Emailing ===========
# =========== Middleware ===========
# Middleware - промежуточный слой
# код который исполняется после запроса но перед вызовом view

# middleware.py
from django.conf import settings


class SomeMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        this function will be launch just before view Function
        view_func - view fucntion that Django is going to call
        view_args - list of args for this Function
        view_kwargs - dict of keyword args for this function

        return None or HttpResponse
        """
        pass


# =========== Cache ===========
# =========== Static pages ===========
# =========== GEO ===========
# =========== Pagination ===========
# =========== Signals ===========
# =========== DB ===========


# =========================================================================================
