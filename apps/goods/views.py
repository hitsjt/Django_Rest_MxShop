from django.shortcuts import render

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status,generics,mixins

from .models import Goods
from .serializers import GoodsSerializer
from rest_framework.pagination import PageNumberPagination

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100

# Create your views here.
class GoodsListView(generics.ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

