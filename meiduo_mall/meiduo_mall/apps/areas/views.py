from django.shortcuts import render
from rest_framework.generics import ListAPIView

# Create your views here.
from rest_framework_extensions.cache.mixins import CacheResponseMixin


from areas.serializers import AreaSerializer
from areas.models import Area
from rest_framework.permissions import IsAuthenticated


class AreasView(CacheResponseMixin, ListAPIView):
    """
        返回省数据
    """
    serializer_class = AreaSerializer
    queryset = Area.objects.filter(parent=None)  # 过滤后的查询集数据


class AreaView(CacheResponseMixin, ListAPIView):
    """
        返市级和区县数据
    """

    serializer_class = AreaSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']  #
        return Area.objects.filter(parent_id=pk)
