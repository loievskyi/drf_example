from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from core.models import Currency, Category, Transaction
from core.serializers import CurrencySerializer, CategorySerializer, ReadTransactionSerializer, WriteTransactionSerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.select_related("currency", "category")
    filter_backends = (filters.SearchFilter,)
    search_fields = ("description",)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        else:
            return WriteTransactionSerializer
