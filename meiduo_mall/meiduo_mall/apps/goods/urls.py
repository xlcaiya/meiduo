from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from . import views

urlpatterns = [

]

router = DefaultRouter()
router.register('skus/search', views.SKUSearchViewSet, base_name='skus_search')
urlpatterns += router.urls
