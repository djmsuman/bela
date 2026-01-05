from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Item
from ..serializers import ItemSerializer


class ItemsView(APIView):
    """
    View to list all items and create a new item.
    """

    def get(self, request):
        """
        List all items.
        """
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new item.
        """
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
