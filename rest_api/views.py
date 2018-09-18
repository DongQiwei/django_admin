from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_api.models import Banner
from rest_api.serializers import BannerSerializer


class BannerView(APIView):
    def get(self, request):
        banners = Banner.objects.filter(is_delete=False)
        # 第一个参数查询的数据 如果是多个对象需要使用many=True 默认单个
        serializer = BannerSerializer(banners, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        # 能获取所有请求的数据
        # request.data
        pass
