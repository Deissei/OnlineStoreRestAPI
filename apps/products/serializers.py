from rest_framework import serializers

from apps.products.models import ImageProduct, Product


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ('id', 'image')


class ProductSerializer(serializers.ModelSerializer):
    # images = ImageProductSerializer(many=True)

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('manufacturer', )


class ProductListSerializer(serializers.ModelSerializer):
    images = ImageProductSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'images')