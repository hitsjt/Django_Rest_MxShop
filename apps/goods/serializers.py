from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Goods,GoodsCategory

class CategorySerializer(ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        #fields = ('name','click_num','market_price','add_time')
        fields = '__all__'