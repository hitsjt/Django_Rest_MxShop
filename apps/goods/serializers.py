from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Goods

class GoodsSerializer(ModelSerializer):
    class Meta:
        model = Goods
        #fields = ('name','click_num','market_price','add_time')
        fields = '__all__'