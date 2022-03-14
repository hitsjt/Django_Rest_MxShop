from django.shortcuts import render

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status,generics,mixins

from .models import Goods
from .serializers import GoodsSerializer

# Create your views here.
class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

