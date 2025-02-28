from rest_framework import serializers
from .models import Fornecedor

class FornecedorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['cnpj','nome']