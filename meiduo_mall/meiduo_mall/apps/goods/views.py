from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SKU, GoodsCategory
from .serializers import SKUSerializer, SKUIndexSerializer
from drf_haystack.viewsets import HaystackViewSet


class GoodCategorieView(APIView):
    def get(self, request, category_id):
        # 获取三级分类对象
        cat3 = GoodsCategory.objects.get(id=category_id)
        # 获取二级分类对象和一级分类对象
        cat2 = cat3.parent
        cat1 = cat2.parent

        return Response({
            'cat1': cat1.name,
            'cat2': cat2.name,
            'cat3': cat3.name,

        })


class SKUListView(ListAPIView):
    """
    sku列表数据
    """
    serializer_class = SKUSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('create_time', 'price', 'sales')

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return SKU.objects.filter(category_id=category_id, is_launched=True)


class SKUSearchViewSet(HaystackViewSet):
    """
    SKU搜索
    """
    index_models = [SKU]

    serializer_class = SKUIndexSerializer
