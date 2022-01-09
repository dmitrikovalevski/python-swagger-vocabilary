from .serializer import CardSerializer
from .models import Card
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CardListApiView(ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer



