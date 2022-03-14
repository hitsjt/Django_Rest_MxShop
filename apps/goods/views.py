from django.shortcuts import render

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status,generics,mixins,viewsets

from .models import Goods
from .serializers import GoodsSerializer
from .filters import GoodsFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100

# Create your views here.
class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsFilter

