from rest_framework import serializers
from store.models import Store


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
