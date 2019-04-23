#########################
# DJANGO REST FRAMEWORK #
#########################
# WHAT IS API
# ============

# API - програмный интерфейс приложения
# REST
# используется в веб приложениях для передачи данных/ коммуникации
# использует HTTP для вызовов меду машина
# GET используется для получения данных
# PUT изменить состояние, обновить ресурс
# PATCH
# POST создать ресур
# DELETE удалить ресур
# REST API нужно для соединения вашего Джанго проекта с любой третьей прогрммой
# Api endpoint Create, Retrieave, Update, Delete. CRUD


# DJANGO REST FRAMEWORK
# =====================

# ARCHITECTURE
rest_framework.serializers  # сериализаторы данных
rest_framework.views  # APIView,
rest_framework.generics  # generic view
rest_framework.mixins  #
rest_framework.status  # Http status codes
rest_framework.response  # Response()
rest_framework.permissions  #


# PREREQUISITES
# Add REST_FRAMEWORK settings dictionary to your settings file
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),

    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}


# REQUESTS
# DRF Request object extends HttpRequest
# has support for parsing and authentication
    request.data
    request.query_params



# SERIALIZERS

# Data types and validation
# Converts data to python objects/json( work very similiar to Django's Form, ModelForm)
# makes data validation

# 2 most common serializer classes
# Serializer/ ModelSerializer
# BaseSerializer can be used for creating custom realizations

from rest_framework import serializers


class SomeSerializer(serializers.Serializer):

    field1 = serializer.EmailField()
    field2 = serializer.Charfield(max_length=200)


# data validation
# whole data validation
if serializer.is_valid():
    data_dict = self.validated_date
else:
    errors_dict = serializer.errors

# field level validation
# can add validate_<field_name> method

# Model Serializer
# shortcut for automatically create model serializer
# extends Serializer class with:
    # auto fields generation
    # auto validators generator
    # simple create and update methods implementation

class SomeSerializer(serializers.ModelSerializer):
    some_extra_field = serializers.URLField()

    class Meta:
        model = SomeModel
        fields = ('fields', 'to be', 'serialized')/ '__all__'
        exclude = ()
        depth = 1  # насколько далеко должен заходить при сериализации связных объектов
        read_only_fields = ()

# HyperLinkModelSerializer - использует url для представления связных моделей



# VIEWS
# Base view class is APIView which is subclass of View
# Различия
# - Request will be REST Request() instances not Django HttpRequest
# - Response будет объект REST Response() instead od Django HttpResponse()
# - Входящие запросы будут аутентифицированы

from rest_framework import generic
    get_object_or_404()
    GenericAPIView(APIView)   # all generic classes base view
        queryset=None  #
        serializer_class=None  #
        pagination_class=
        permission_classes=()
        authentication_classes=()
    CreateAPIView  #
    ListAPIView  # list queryset
    DestroyAPIView  #
    UpdateAPIView  #
    ListCreateAPIView  #
    RetrieveUpdateAPIView  #
    RetrieveDestroyAPIView
    RetrieveUpdateDestroyAPIView

from rest_framework import mixins
    CreateModelMixin  # contains create method
    ListModelMixin   # list method
    RetrieveModelMixin  # retrieve method
    UpdateModelMixin  # update method
    DestroyModelMixin  # desytoy/delete model instance



# VIEWSET
# provide actions instead of usual method handlers
# (list, create, retrieve, update, partial_update, destroy)
# why use viewsets:
# combine logic in one class
# no need to write urls

from rest_framework import viewset


class TestViewSet(viewset.ModelViewSet):

    serializer_class = Serializer  # serializer class
    queryset = SomeModel.objects.all()
    permission_classes = []
    parser_classes = []
    authentication_classes = []

    # attrs available while dispatch
    self.basename  # базовое название для использование в URL
    self.action  # current action
    self.detail  # if True its a detail

    self.get_extra_actions()


    @action(detail=True, methods=['post', 'delete'], url_path='custom-method', url_name='custom-method')
    def custom_method(self):
        print('Custom method is here')



# Routers
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)


urlpatterns = [
    path('test', some_view),
    path('', include(router.urls)),
]


urlpatterns += router.urls



# AUTHENTICATION
# associating an incoming request object with a set of credentials
# always runs at the very start of the view

    request.user  # typically returns Django user instance
    request.auth  # authentication context

# Token Authentication
#


# PERMISSIONS
# Permissions are used to grant or deny access different classes of users
# to different parts of the API.

    AllowAny  # allows access, reguardless of if the request is authenticated or not
    IsAuthenticated  # will deny any unauthenticated user request
    IsAdminUser  # allow to user if user.is_staff = True
    IsAuthenticatedOrRadOnly  # permit only "safe methods" GET HEAD OPTIONS


# FILTERING
# The simplest way to filter the queryset of any view that
# subclasses GenericAPIView is to override the .get_queryset() method.



# TESTING
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'}, format='json')
