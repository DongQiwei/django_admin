from rest_framework import serializers

from rest_api.models import Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        # 声明序列化对象的模型
        model = Banner
        # 指定模型需要序列化的字段
        fields = '__all__'
        # fields = ['id']