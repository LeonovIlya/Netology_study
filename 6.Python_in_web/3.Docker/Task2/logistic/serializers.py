from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        print(validated_data)
        positions = validated_data.pop('positions')
        print(positions)
        stock = super().create(validated_data)
        print(stock)
        for elem in positions:
            StockProduct.objects.create(stock=stock, **elem)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for elem in positions:
            obj, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=elem['product'],
                defaults={'stock': stock, 'product': elem['product'], 'quantity': elem['quantity'], 'price': elem['price']}
            )
        return stock
